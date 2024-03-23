from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name="first"),
    path('faculty/', views.faculty, name="faculty"),
    path('login/', views.login, name="login"),
    path('course/', views.course, name="course"),
    path('payment/', views.payment, name="payment"),
    path('student/', views.student, name="student"),

]
