from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import CustomUser

# =========================
#        Role Checks
# =========================
def is_student(user):
    return user.role == 'student'

def is_teacher(user):
    return user.role == 'teacher'

def is_admin(user):
    return user.role == 'admin'

# =========================
#        Login View
# =========================
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Safe key access
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Role-based redirection
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'teacher':
                return redirect('teacher_dashboard')
            elif user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                messages.error(request, "Unknown role assigned.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


# =========================
#        Logout View
# =========================
def logout_view(request):
    logout(request)
    return redirect('login')


# =========================
#    Dashboard Views
# =========================

@login_required
@user_passes_test(is_student)
def student_dashboard(request):
    return render(request, 'student_dashboard.html')


@login_required
@user_passes_test(is_teacher)
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# =========================
# (Optional) Register View
# =========================
from .forms import CustomUserCreationForm  # Only if you created this form

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please login.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
