from django.shortcuts import render, redirect, HttpResponse
from .models import Courses, Descriptions, Comments

# Create your views here.
def index(request):
    context= {
        "courses": Courses.objects.all(),
    }
    print context['courses']
    print Comments.objects.all()
    return render(request, 'course/index.html', context)

def add(request):
    if request.method == "POST":
        if not request.POST["name"]:
            print "name empty"
            return redirect('/')
        course = Courses(name=request.POST["name"])
        course.save()
        if request.POST["content"]:
            desc = request.POST["content"]
            print "*" * 50
            description = Descriptions(course_id=course, content=desc)
            description.save()
    return redirect('/')

def show(request, id):
    course = {
        "course":Courses.objects.get(id=id)
    }
    print course    
    return render(request, 'course/destroy.html', course)

def delete(request, id):
    print request.method
    if request.method=="POST":
        if request.POST["method"] == "delete":
            Courses.objects.get(id=id).delete()   
            return redirect('/')

def message(request, id):
    course = {
        "course":Courses.objects.get(id=id),
        "comments":reversed(Comments.objects.filter(course_id__pk=id))
    }
    print course
    
    return render(request, 'course/message.html', course)

def create(request, id):
    if request.method == "POST":
        course=Courses.objects.get(id=id)
        comment=Comments(course_id=course, content=request.POST["content"])
        comment.save()
        return redirect("/comments/{}".format(id))



