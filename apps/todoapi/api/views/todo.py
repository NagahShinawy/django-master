import json

from django.core import serializers
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from ..serializers import TodoSerializer
from ..models import Todo
from ..mixins import TodoJson, NotFoundObj


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
        return JsonResponse(objs.data, safe=False, status=status.HTTP_200_OK)

    def post(self, request):
        todo = TodoSerializer(data=request.data)
        # print(repr(serializer))
        if todo.is_valid():
            item = todo.save()
            item.is_completed = True
            # request=request: more meta data about request --> /api/1 to https://host/api/v1
            item.url = reverse(
                "todo:single-todo", kwargs={"todo_id": item.pk}, request=request
            )
            item.save()
            return JsonResponse(data={"todo": todo.data}, status=status.HTTP_201_CREATED)

        return JsonResponse(data=todo.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Todo.objects.all().delete()
        return JsonResponse({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)


class SingleTodo(APIView):
    @staticmethod
    def is_exist(todo_id):
        todo = Todo.objects.filter(pk=todo_id)
        return todo.first() if todo else None

    def get(self, request, todo_id):
        todo = self.is_exist(todo_id)
        if todo is not None:
            return JsonResponse(TodoSerializer(todo).data, status=status.HTTP_200_OK)
        return Response(
            {"message": NotFoundObj.MESSAGE.format(id=todo_id)},
            status=status.HTTP_404_NOT_FOUND,
        )

    def patch(self, request, todo_id):
        task = self.is_exist(todo_id)
        # title = request.data.get("title")
        # if task is not None and title:
        #     task.title = title
        #     task.save()
        if task is None:
            return Response(
                {"message": NotFoundObj.MESSAGE.format(id=todo_id)},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TodoSerializer(data=request.data, instance=task, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, todo_id):
        task = self.is_exist(todo_id)
        if task is not None:
            task.delete()
            return Response("", status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"message": NotFoundObj.MESSAGE.format(id=todo_id)},
            status=status.HTTP_404_NOT_FOUND,
        )
