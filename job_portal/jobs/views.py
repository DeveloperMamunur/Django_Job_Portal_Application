from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Job, Application
from .forms import JobForm, ApplicationForm
import os
from django.http import FileResponse, Http404


# Create your views here.
@login_required
def employer_dashboard(request):
    if request.user.profile.role != 'employer':
        messages.error(request, 'Access denied. Employers only.')
        return redirect('home')
    
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'jobs/employer_dashboard.html', {'jobs': jobs})

@login_required
def applicant_dashboard(request):
    if request.user.profile.role != 'applicant':
        messages.error(request, 'Access denied. Applicants only.')
        return redirect('home')
    
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'jobs/applicant_dashboard.html', {'applications': applications})

@login_required
def post_job(request):
    if request.user.profile.role != 'employer':
        messages.error(request, 'Access denied. Employers only.')
        return redirect('home')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('employer_dashboard')
    else:
        form = JobForm()
    
    return render(request, 'jobs/post_job.html', {'form': form})

def job_list(request):
    query = request.GET.get('q', '')
    jobs = Job.objects.all()
    
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company_name__icontains=query) |
            Q(location__icontains=query)
        )
    
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'query': query})


def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.user != job.posted_by:
        messages.error(request, 'Access denied. You are not the owner of this job.')
        return redirect('job_list')
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully!')
            return redirect('employer_dashboard')
    else:
        form = JobForm(instance=job)
    
    return render(request, 'jobs/edit_post_job.html', {'form': form})


def job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    has_applied = False
    
    if request.user.is_authenticated and request.user.profile.role == 'applicant':
        has_applied = Application.objects.filter(job=job, applicant=request.user).exists()
    
    return render(request, 'jobs/job_detail.html', {'job': job, 'has_applied': has_applied})

def dashboard_job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.user.is_authenticated and request.user.profile.role == 'applicant':
        has_applied = Application.objects.filter(job=job, applicant=request.user).exists()
        context = {
            'job': job,
            'has_applied': has_applied,
        }
    else:
        context = {
            'job': job,
        }
    
    return render(request, 'jobs/dashboard_job_details.html', context)

def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.user != job.posted_by:
        messages.error(request, 'Access denied. You are not the owner of this job.')
        return redirect('job_list')
    
    job.delete()
    messages.success(request, 'Job deleted successfully!')
    return redirect('job_list')

@login_required
def apply_job(request, job_id):
    if request.user.profile.role != 'applicant':
        messages.error(request, 'Access denied. Applicants only.')
        return redirect('home')
    
    job = get_object_or_404(Job, id=job_id)
    
    if Application.objects.filter(job=job, applicant=request.user).exists():
        messages.error(request, 'You have already applied for this job.')
        return redirect('job_detail', job_id=job_id)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('dashboard_job_details', job_id=job_id)
    else:
        form = ApplicationForm()
    
    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})

@login_required
def edit_apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    try:
        application = Application.objects.get(job=job, applicant=request.user)
    except Application.DoesNotExist:
        messages.error(request, "You haven't applied to this job yet.")
        return redirect('job_detail', job_id=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application updated successfully.')
            return redirect('dashboard_job_details', job_id=job_id)
    else:
        form = ApplicationForm(instance=application)

    return render(request, 'jobs/edit_apply.html', {
        'form': form,
        'job': job,
        'edit': True,
    })


def view_apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    application = get_object_or_404(Application, job=job, applicant=request.user)
    return render(request, 'jobs/view_apply.html', {'application': application})

def view_resume(request, application_id):
    from .models import Application
    app = Application.objects.filter(id=application_id, applicant=request.user).first()
    if not app or not app.resume:
        raise Http404("Resume not found")

    resume_path = app.resume.path
    if not os.path.exists(resume_path):
        raise Http404("File does not exist")

    response = FileResponse(open(resume_path, 'rb'), content_type='application/pdf')
    response['X-Frame-Options'] = 'ALLOWALL'  # Allow it to be shown in <iframe>
    return response  

def delete_apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    application = get_object_or_404(Application, job=job, applicant=request.user)
    
    application.delete()
    messages.success(request, 'Application deleted successfully!')
    return redirect('applicant_dashboard')

@login_required
def job_applicants(request, job_id):
    if request.user.profile.role != 'employer':
        messages.error(request, 'Access denied. Employers only.')
        return redirect('home')
    
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    applications = Application.objects.filter(job=job)
    
    return render(request, 'jobs/job_applicants.html', {'job': job, 'applications': applications})