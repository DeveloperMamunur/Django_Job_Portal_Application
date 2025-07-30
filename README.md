# Django Job Portal Application

A web-based job portal built with Django, allowing users to register, search for jobs, apply for positions, and manage job postings. The portal supports user authentication, resume uploads, and an admin dashboard for managing users and job listings.

## Features
- User registration and authentication
- Job listing and search functionality
- Resume upload and management
- Job application tracking
- Admin dashboard for managing jobs and users
- Custom template tags and static files for UI enhancements

## Project Structure
```
job_portal/
├── accounts/         # User authentication and profile management
├── jobs/             # Job listings, applications, and related logic
├── job_portal/       # Project settings and URLs
├── media/            # Uploaded resumes and media files
├── static/           # Static files (CSS, JS, images)
├── templates/        # Shared HTML templates
├── manage.py         # Django management script
└── db.sqlite3        # SQLite database (default)
```

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd Django_Job_Portal_Application
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   *(Create `requirements.txt` with Django and any other dependencies if not present)*

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (admin):**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Access the application:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
   - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Fixtures
- Sample data is available in `fixtures/`.
- Load fixtures with:
  ```sh
  python manage.py loaddata fixtures/user.json
  python manage.py loaddata fixtures/profile.json
  python manage.py loaddata fixtures/jobdata.json
  ```

## Media & Static Files
- Uploaded resumes are stored in `media/resumes/`.
- Static files are in `static/`.

## UI Screenshots

Below are some UI screenshots of the Django Job Portal Application:


<table>
  <tr>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 105636.png" alt="Home Page" width="350" /><br>Home Page
    </td>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 105700.png" alt="Job List" width="350" /><br>Job List
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 105717.png" alt="Login Page" width="350" /><br>Login Page
    </td>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 105732.png" alt="Register Page" width="350" /><br>Register Page
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 110450.png" alt="Employer Job Post List" width="350" /><br>Employer Job Post List
    </td>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 112956.png" alt="Employer Create Post for Job" width="350" /><br>Employer Create Post for Job
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 113020.png" alt="View all applications in job post" width="350" /><br>View all applications in job post
    </td>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 120445.png" alt="View cover letter by Employer" width="350" /><br>View cover letter by Employer
    </td>
  </tr>
    <tr>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 113236.png" alt="Applicant Applications List" width="350" /><br>Applicant Applications List
    </td>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 113257.png" alt="Update application by applicant" width="350" /><br>Update application by applicant
    </td>
  </tr>
    <tr>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 113308.png" alt="Job details applicant applied job" width="350" /><br>Job details applicant applied job
    </td>
    <td align="center">
      <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 113324.png" alt="View applications by applicant" width="350" /><br>View applications by applicant
    </td>
  </tr>
    <tr>
        <td align="center">
        <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 105952.png" alt="Application submission in dark mode" width="350" /><br>Application submission in dark mode
        </td>
        <td align="center">
        <img src="./job_portal/static/Screenshoot/Screenshot 2025-07-30 121217.png" alt="Update application by Employer in dark mode" width="350" /><br>Update application by Employer in dark mode
        </td>
      </tr>
</table>

## License
This project is for educational purposes.
