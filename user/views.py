from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Course, Student

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'

class StudentListView(ListView):
    template_name = 'student_list.html'

    def get_queryset(self):
        self.course = get_object_or_404(Course,)
        return self.course.students.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.course
        return context
