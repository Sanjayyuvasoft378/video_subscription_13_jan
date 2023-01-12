from django.shortcuts import render
from membership.models import UserMembership
# Create your views here.
from .models import Courses
from django.views import View

from django.views.generic import ListView, DetailView
class CourseListView(ListView):
    model = Courses

class CourseDetailView(DetailView):
    model = Courses

class LessonDetailView(View):
    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course_qs = Courses.objects.filter(slug=course_slug)
        if course_qs.exists():
            course = course_qs.first()
        lesson_qs = course.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists():
            lesson = lesson_qs.first()
        
        # user_membership =  UserMembership.objects.filter(user=request.user).first()
        # user_membership_type = user_membership.membership.membership_type

        # course_allowed_mem_types = course.allowed_membership.all() 
        # context = {
        #     'object':None
        # }

        # if course_allowed_mem_types.filter(membership_type = user_membership_type).exists():
            context = {
                "object":lesson
            }
        return render(request,"course_app/lesson_detail.html",context )