from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def landing(request):
    return render(request,'index.html')

def teacher_list(request):
    teachers=Teachers.objects.all()
    return render(request,'index.html',{'teachers':teachers})

def students_list(request):
    students=Students.objects.all()
    return render(request,'index2.html',{'students':students})





def add_teacher(request):
    if request.method=='POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        image=request.FILES.get('image')

        teacher=Teachers(name=name,subject=subject,contact=contact,email=email,image=image if image else None)
        teacher.save()
        return redirect('home')
    return render(request,'index.html')

def add_student(request):
    if request.method=='POST':
        name=request.POST.get('name')
        grade=request.POST.get('grade')
        section=request.POST.get('section')
        contact=request.POST.get('contact')
        image=request.FILES.get('image')
        
        student=Students(name=name,grade=grade,section=section,contact=contact,image=image if image else None)
        student.save()
        return redirect('students_list')
    return render(request,'index2.html')
        
def edit_teacher(request,id):
    teacher=Teachers.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        image=request.FILES.get('image')
        teacher.name = name
        teacher.subject = subject
        teacher.contact = contact
        teacher.email = email
        if image:
            teacher.image=image
        teacher.save()
        return redirect('home')
    return render(request,'index.html',{'teacher':teacher})

def edit_student(request,id):
    student=Students.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        grade=request.POST.get('grade')
        section=request.POST.get('section')
        contact=request.POST.get('contact')
        image=request.FILES.get('image')
        student.name=name
        student.grade=grade
        student.section=section
        student.contact=contact
        if image:
            student.image=image
        student.save()
        return redirect('students_list')
    return render(request,'index2.html',{'student':student})

def delete_teacher(request,id):
    teacher=Teachers.objects.filter(id=id)
    teacher.delete()
    return redirect('home')

def delete_student(request,id):
    student=Students.objects.filter(id=id)
    student.delete()
    return redirect('students_list')