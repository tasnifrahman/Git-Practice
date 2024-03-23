from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request, 'index.html')

def faculty(request):
    return render(request, 'faculty.html')

def login(request):
    return render(request, 'login.html')

def course(request):
    return render(request, 'course.html')

def payment(request):
    return render(request, 'payment.html')

def student(request):
    return render(request, 'student.html')