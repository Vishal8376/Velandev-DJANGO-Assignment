# Velandev-DJANGO-Assignment

---

```markdown
# 🎓 University Portal – Role-Based Authentication System (Django)

A Django-based web application for managing different user roles in a university system: **Students**, **Teachers**, and **Admins**. Each role has specific permissions and dashboard access.

---

## 🔐 Features

- Custom user model with role-based access
- Role-specific dashboards:
  - `/student/dashboard/`
  - `/teacher/dashboard/`
  - `/admin/dashboard/`
- Login and logout functionality
- Authorization using decorators:
  - `@login_required`
  - `@user_passes_test()`
- Clean, modular project structure
- Easily extendable to support additional features (e.g., assignments, grading, notifications)

---

## 👥 User Roles

| Role    | Permissions                                                  |
|---------|--------------------------------------------------------------|
| Student | View own profile, submit assignments                        |
| Teacher | View & grade student assignments                            |
| Admin   | Manage user accounts and global system settings             |

---

## 🧱 Tech Stack

- **Backend**: Django 5.x
- **Frontend**: HTML (templated)
- **Database**: SQLite (default, easy to switch to PostgreSQL/MySQL)

---

## 📁 Project Structure



LoginPro/
├── LoginApp/
│   ├── models.py          # CustomUser model with roles
│   ├── views.py           # Login, Logout, Dashboards
│   ├── urls.py            # Role-based route mapping
│   ├── templates/
│   │   ├── login.html
│   │   ├── student\_dashboard.html
│   │   ├── teacher\_dashboard.html
│   │   └── admin\_dashboard.html
├── LoginPro/
│   ├── settings.py        # AUTH\_USER\_MODEL, Templates, etc.
│   ├── urls.py            # Root URL config

````

---

## ⚙️ Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/university-portal.git
   cd university-portal
````

2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv env
   source env/bin/activate      # On Windows: env\Scripts\activate
   ```

3. **Install requirements**

   ```bash
   pip install django
   ```

4. **Apply migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (admin)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**

   ```bash
   python manage.py runserver
   ```

7. **Access the app**

   * Login: [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)
   * Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) *(if included)*

---

## ✅ Default User Creation (optional)

```python
# Run in Python shell (python manage.py shell)
from LoginApp.models import CustomUser
CustomUser.objects.create_user(username='student1', password='pass123', role='student')
CustomUser.objects.create_user(username='teacher1', password='pass123', role='teacher')
CustomUser.objects.create_user(username='admin1', password='pass123', role='admin')
```

---

## 📌 Notes

* Be sure to set `AUTH_USER_MODEL = 'LoginApp.CustomUser'` in `settings.py`.
* Templates must be correctly referenced using `TEMPLATES['DIRS']`.

---
