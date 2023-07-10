
from apps.Order.api.serializers.order_serializers import OrderSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class OrderViewSet(viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    
    def get_queryset(self,pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()
    
    def list(self,request, *args,**kargs):
        orders = self.get_queryset()
        if orders.exists():
            orders_serializers = self.serializer_class(orders, many = True)
            return Response(orders_serializers.data, status=status.HTTP_200_OK)
        return Response({'message':"Orders don't exist"}, status= status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk = None):
        order = self.get_queryset(pk)
        if order:
            order_serializer = self.serializer_class(order)
            return Response(order_serializer.data, status= status.HTTP_200_OK)
        return Response({'message':"Order don't exist"}, status= status.HTTP_404_NOT_FOUND)    
