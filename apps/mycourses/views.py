from django.shortcuts import render,redirect
from .models import Course,Desc

def index(request):
    context={
        'courses':Course.objects.all()
    }
    print context
    return render(request,'mycourses/index.html',context)

def add(request):
    if request.method=="POST":
        name=request.POST['name']
        desc=request.POST['desc']
        print name
        print desc
        newcourse=Course(name=name)
        newcourse.save()
        newdesc=Desc(desc=desc,course=newcourse)
        newdesc.save()
        return redirect('/')
    else:
        return redirect('/')

def detail(request,id):
    context={
        'course':Course.objects.filter(id=id)
    }
    print Course.objects.get(id=id).name
    return render(request,'mycourses/detail.html',context)

def delete(request,id):
    course=Course.objects.get(id=id)
    course.desc.delete()
    course.delete()
    return redirect('/')
