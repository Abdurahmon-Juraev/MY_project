from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.common.models import Common


class CommonListAPIView(generics.ListAPIView):
    queryset = Common.objects.all()
    # serializer_class = CommonListSerializer
    permission_classes = [AllowAny]

