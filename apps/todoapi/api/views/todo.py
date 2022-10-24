import json

from django.core import serializers
from django.http import JsonResponse
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from ..serializers import TodoSerializer
from ..models import Todo
from ..mixins import TodoJson


class TodoList(APIView, TodoJson):

    JSON = "json"

    def get(self, request):
        todos = Todo.objects.all()
        # todo: solution 1
        # data = [self.to_json(obj) for obj in todos]
        # todo: solution 2
        # return JsonResponse(
        #     {
        #         "data": json.loads(
        #             serializers.serialize(format=self.JSON, queryset=todos)
        #         )
        #     }
        # )
        # todo: solution 3
        objs = TodoSerializer(todos, many=True)
        return JsonResponse(objs.data, safe=False)

    def post(self, request):
        todo = TodoSerializer(data=request.data)
        # print(repr(serializer))
        if todo.is_valid():
            item = todo.save()
            item.is_completed = True
            # request=request: more meta data about request --> /api/1 to https://host/api/v1
            item.url = reverse("todo:single-todo", kwargs={"todo_id": item.pk}, request=request)
            item.save()
            return JsonResponse(data={"todo": todo.data})

        return JsonResponse(data=todo.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Todo.objects.all().delete()
        return JsonResponse({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)


class SingleTodo(APIView):
    def get(self, request, todo_id):
        todo = Todo.objects.filter(pk=todo_id)
        if todo:
            return JsonResponse(TodoSerializer(todo.first()).data)
        return JsonResponse({"message": f"obj with id <{todo_id}> not found"})
