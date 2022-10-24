from django.urls import path
from apps.todoapi.api.views.todo import TodoList, SingleTodo


app_name = "todo"

urlpatterns = [
    path("todolist", TodoList.as_view(), name="todo-list"),
    path("todo", SingleTodo.as_view(), name="single-todo"),
]



