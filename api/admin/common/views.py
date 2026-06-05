from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from apps.common.models import Category, Product, Car
from .serializer import ProductModelSerializer, CategoryModelSerializer, CarModelSerializer


# class CommonListAPIView(generics.ListAPIView):
#     queryset = Common.objects.all()
#     serializer_class = CommonListSerializer
#     permission_classes = [AllowAny]


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductModelSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer




