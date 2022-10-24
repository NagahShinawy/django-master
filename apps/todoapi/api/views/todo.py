from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from ..serializers import TodoSerializer
from ..models import Todo
from ..mixins import TodoJson


class TodoList(APIView, TodoJson):

    def get(self, request):
        todos = Todo.objects.all()
        data = [self.to_json(todo) for todo in todos]
        return JsonResponse({"data": data})

    def post(self, request):
        todo = TodoSerializer(data=request.data)
        # print(repr(serializer))
        if not todo.is_valid():
            return JsonResponse(data=todo.errors, status=status.HTTP_400_BAD_REQUEST)

        todo.save()
        return JsonResponse(data={"todo": todo.data})


class SingleTodo(APIView):
    def get(self, request, todo_id):
        return JsonResponse({"todo": {
            "id": todo_id,
            "title": "back end",
            "is_completed": False
        }})