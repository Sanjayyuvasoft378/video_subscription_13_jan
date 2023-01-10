from django.shortcuts import render

# Create your views here.
from .models import Courses

from django.views.generic import ListView, DetailView
class CourseListView(ListView):
    model = Courses

class CourseDetailView(DetailView):
    model = Courses



