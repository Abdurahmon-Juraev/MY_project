from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.common.models import Product, Category, Car


# class CommonListSerializer (ModelSerializer):
#     class Meta:
#         model=Common
#         fields= '__all__'



class ProductModelSerializer(ModelSerializer):
    user_info = SerializerMethodField()
    class Meta:
        model= Product
        fields= (
            'id',
            'name',
            'price',
            'image',
            'category',
            'user_info'
        )

    def get_user_info(self, obj):
        if not obj.user:
            return None
        return {
            'name': obj.user.name,
            'phone_number': obj.user.phone_number,
        }


class CarModelSerializer(ModelSerializer):
    car_info =SerializerMethodField()
    class Meta:
        model=Car
        fields =(
            'id',
            'name',
            'price',
            'image',
            'car_info'
        )

    def get_car_info(self,car):
        if not car:
            return None
        return {
            'name': car.name,
            'image':car.image.url,
            'price':car.price,
        }



class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



