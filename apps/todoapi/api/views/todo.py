from django.http import JsonResponse
from rest_framework.views import APIView


class TodoList(APIView):

    def get(self, request):
        return JsonResponse({"data": [{
            "title": "study and work hard",
            "is_completed": True,

        }]})


class SingleTodo(APIView):
    def get(self, request, todo_id):
        return JsonResponse({"todo": {
            "id": todo_id,
            "title": "back end",
            "is_completed": False
        }})