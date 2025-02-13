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



# Existing views...

# Existing views...

def track_progress(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    topics = course.topic_set.all()
    completed_topics = topics.filter(completed=True).count()
    total_topics = topics.count()
    remaining_topics = total_topics - completed_topics
    progress_percentage = (completed_topics / total_topics) * 100 if total_topics > 0 else 0

    return render(request, 'track_progress.html', {
        'course': course,
        'completed_topics': completed_topics,
        'total_topics': total_topics,
        'remaining_topics': remaining_topics,
        'progress_percentage': progress_percentage
    })

