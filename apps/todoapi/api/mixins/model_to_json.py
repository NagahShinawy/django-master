from abc import ABC, abstractmethod


class JsonModelMixin(ABC):
    @abstractmethod
    def to_json(self, obj):
        pass


class TodoJson(JsonModelMixin):
    def to_json(self, todo):
        return {
            "id": todo.pk,
            "title": todo.title,
            "is_completed": todo.is_completed,
            "url": todo.url,
            "order": todo.order,
        }
