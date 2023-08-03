from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User
from .forms import TeacherSignUpForm, StudentSignUpForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import teacher_required, student_required


class StudentSignupView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'auth/student_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student-home')


class TeacherSignupView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'auth/school_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('school-home')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if not user.is_authenticated:
            return reverse('login')
        if user.is_teacher:
            return reverse('school-home')
        elif user.is_student:
            return reverse('student-home')


def welcome(request):
    return render(request, 'welcome.html')


@login_required
@teacher_required
def school_home(request):
    return render(request, 'school/school_home.html')


@login_required
@student_required
def student_home(request):
    return render(request, 'student/student_home.html')
