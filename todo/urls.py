from django.urls import path

from todo.views import add_todo, delete_todo, todos,update_todo
app_name='todo'
urlpatterns = [
    path('', todos,name='todos'),
    path('add_todo', add_todo,name='add_todo'),
    path('update/<int:pk>/', update_todo, name='update_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
]

