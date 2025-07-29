from django.urls import path
from . import views

urlpatterns = [
    path('job-list/', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_details, name='job_detail'),
    path('<int:job_id>/details/', views.dashboard_job_details, name='dashboard_job_details'),

    path('<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('applied-jobs/<int:job_id>/edit/', views.edit_apply, name='edit_apply'),
    path('applied-jobs/<int:job_id>/delete/', views.delete_apply, name='delete_apply'),
    path('<int:job_id>/applicants/', views.job_applicants, name='job_applicants'),
    path('apply/<int:job_id>/', views.view_apply, name='view_apply'),
    path('view-resume/<int:application_id>/', views.view_resume, name='view_resume'),


    path('post/', views.post_job, name='post_job'),
    path('post/<int:job_id>/edit/', views.edit_job, name='edit_job_post'),
    path('post/<int:job_id>/delete/', views.delete_job, name='delete_job_post'),


    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('applicant-dashboard/', views.applicant_dashboard, name='applicant_dashboard'),
]