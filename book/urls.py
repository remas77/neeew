from django.urls import path
from. import views
urlpatterns =[

path('book/',views.simple_query,name='simple_query'),
path('',views.complex_query,name='complex_query'),
path('lab8/task1/', views.task1_view, name='task1'),
path('lab8/task2/', views.task2_view, name='task2'),
path('lab8/task3/', views.task3_view, name='task3'),
path('lab8/task4/', views.task4_view, name='task4'),
path('lab8/task5/', views.task5_view, name='task5'),
path('students/', views.students, name='students'),
path('books/lab9_part1/last_list', views.list_books, name='list_books'),
path('books/lab9_part1/addbook', views.add_book, name='add_book'),
path('books/lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
path('books/lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
path('studentlist/', views.student_list, name='student_list'),
path('add/', views.student_add, name='student_add'),
path('update/<int:pk>/', views.student_update, name='student_update'),
path('delete/<int:pk>/', views.student_delete, name='student_delete'),
path('upload/', views.upload_image, name='upload_image'),
path('images/', views.image_list, name='image_list'),
  ]