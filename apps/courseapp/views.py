from django.shortcuts import render, HttpResponse, redirect
from models import Courses, Description,Comments
import datetime
# Create your views here.
def index(request):
    context = {
        'courses':Courses.objects.all(),
        'description': Description.objects.all(),
    }
    return render(request, "courseapp/index.html", context)
def add(request):
    if request.method == "POST":
        course1 = Courses.objects.create(name = request.POST['name'])
        course1.save()
        description1 = Description.objects.create(course = course1, description = request.POST['description'])
        description1.save()
        return redirect('/')
    return redirect('/')
def destory(request):
    if request.method == "POST":
        return redirect('courses/destory/'+request.POST['course_id'])
    return redirect('/')
def confirm(request,id):
    course_de = Courses.objects.filter(id = id)
    context2 = {
        'courses':course_de
    }
    return render(request, "courseapp/destory.html",context2)
def nodelete(request):
    return redirect('/')
def delete(request):
    if request.method =="POST":
        courseid = request.POST['courseid']
        Courses.objects.filter(id = courseid).delete()
        return redirect('/')
def addcomment(request):
    if request.method == "POST":
        id = int(request.POST['course_id'])
        coursecomment = Courses.objects.get(id = id)
        Comments.objects.create(course = coursecomment, comment = request.POST['comment'])
        return redirect('/courses/addcomment/'+request.POST['course_id'])
    return redirect('/')
def comment(request,id):
    commentonmessage = Comments.objects.filter(course__id = id)
    course = Courses.objects.filter(id = id)
    context = {
        "comments":commentonmessage,
        "courses":course,
    }
    return render(request,"courseapp/comment.html",context)
