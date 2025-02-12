from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Topic

# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        Course.objects.create(name=name)
        return redirect('course_list')
    return render(request, 'add_course.html')

def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    topics = course.topic_set.all()
    return render(request, 'course_detail.html', {'course': course, 'topics':topics})

def add_topic(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:

            Topic.objects.create(course=course, name=name)
            return redirect('course_detail', course_id=course.id)
    return render(request, 'add_topic.html', {'course': course})

def toggle_completion(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.completed = not topic.completed
    topic.save()
    return redirect('course_detail', course_id=topic.course.id)

def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    course_id = topic.course.id
    topic.delete()
    return redirect('course_detail', course_id=course_id)

def progress_view(request):
    courses = Course.objects.all()
    progress_data = []
    for course in courses:
        total_topics = course.topic_set.count()
        complete_topics = course.topic_set.filter(completed=True).count()
        progress_data.append((course.name, complete_topics, total_topics))

    return render(request, 'progress.html', {'progress_data': progress_data})