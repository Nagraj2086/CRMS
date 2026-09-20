from django.urls import path
from .views import *
from . import views

urlpatterns=[
    # path('',views.landing,name='home'),
    path('',views.teacher_list,name='home'),
    path('add-teacher/',views.add_teacher,name='add_teacher'),
    path('update-teacher/<int:id>/',views.edit_teacher,name='edit_teacher'),
    path('delete-teacher/<int:id>',views.delete_teacher,name='delete_teacher'),


    path('students-list/',views.students_list,name='students_list'),
    path('add-student/',views.add_student,name='add_student'),
    path('edit-student/<int:id>',views.edit_student,name='edit_student'),
    path('delete-student/<int:id>',views.delete_student,name='delete_student'),

]