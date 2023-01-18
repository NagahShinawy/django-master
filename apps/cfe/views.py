from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import status, generics, mixins, permissions
from rest_framework import authentication
from rest_framework.decorators import api_view
from .models import Product, Color
from .serializers import ProductSerializer, ColorSerializer
from apps.cfe.permissions import OnlyAccessColor


class UpdateProductMixin:
    @staticmethod
    def update_save(request, serializer):
        user = request.user if request.user.is_authenticated else None
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content")
        content = title if not content else content
        serializer.save(user=user, content=content)


def to_json(product: Product):
    return {
        "id": product.pk,
        "title": product.title,
        "content": product.content,
        "price": product.price,
    }


@api_view(["POST"])
def cfh(request, *args, **kwargs):
    products = [to_json(product) for product in Product.objects.all().order_by("-id")]
    # products = model_to_dict(Product.objects.all().last(), fields=["id", "title", "price"])
    if products:
        return JsonResponse({"products": products})
    return JsonResponse({"products": []})


def products_list(request, *args, **kwargs):
    objs = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(data=objs, safe=False)


@api_view(["POST"])
def create_product(request, *args, **kwargs):
    product = ProductSerializer(data=request.data)
    if product.is_valid(raise_exception=True):
        product.save()
        return JsonResponse({"product": product.data}, status=status.HTTP_201_CREATED)
    return JsonResponse({"message": product.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductCreateAPIView(generics.CreateAPIView, UpdateProductMixin):
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        self.update_save(self.request, serializer)


class ProductListCreateAPIView(generics.ListCreateAPIView, UpdateProductMixin):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [OnlyAccessColor]
    # permission_classes = [
    #     permissions.DjangoModelPermissions
    # ]  # allow user to access specific model with custom actions

    def perform_create(self, serializer):
        self.update_save(self.request, serializer)

    # def get_queryset(self):
    #     Product.objects.exclude(user__id=self.request.user.id).delete()
    #     return super().get_queryset()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    lookup_field = "pk"
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = "pk"
    serializer_class = ProductSerializer


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            return self.retrieve(request, args, kwargs)
        return self.list(request, args, kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ColorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAdminUser]
    # permission_classes = [permissions.DjangoModelPermissions]
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    ]


class BikeListAPIView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
