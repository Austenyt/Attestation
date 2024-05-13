from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from retailer.models import Supplier, Product, Contact
from .permissions import IsActiveStaff
from .serializers import ContactSerializer, SupplierSerializer, ProductSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('contact__country',)  # Фильтрация по стране
    permission_classes = (IsActiveStaff,)

    @action(detail=True, methods=['post'])
    def clear_debt(self, request, pk=None):
        """Метод для очистки задолженности, доступный только активным пользователям """
        supplier = self.get_object()
        supplier.debt = 0
        supplier.save()
        return Response({'status': 'debt cleared'}, status=status.HTTP_200_OK)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
