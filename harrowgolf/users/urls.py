from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("student", views.student_home, name='student-home'),
    path("school", views.school_home, name="school-home"),
    path("login", views.LoginView.as_view(), name="login"),
    path("signup/student", views.StudentSignupView.as_view(), name="student-signup"),
    path("signup/school", views.TeacherSignupView.as_view(), name="school-signup"),
    path("logout", auth_views.LogoutView.as_view(
        template_name="users/logout.html"), name="logout"
    ),
]
