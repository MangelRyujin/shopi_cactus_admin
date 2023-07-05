
from apps.Order.api.serializers.order_serializers import Items_OrderSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class Items_OrderViewSet(viewsets.GenericViewSet):
    serializer_class = Items_OrderSerializer
    
    def get_queryset(self,pk = None):
        if pk is not None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()
    
    def list(self,request, *args,**kargs):
        items = self.get_queryset()
        if items.exists():
            items_serializer = self.serializer_class(items, many = True)
            return Response(items_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':"Items don't exist"}, status= status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk = None):
        item = self.get_queryset(pk)
        if item:
            item_serializer = self.serializer_class(item)
            return Response(item_serializer.data, status= status.HTTP_200_OK)
        return Response({'message':"Item don't exist"}, status= status.HTTP_404_NOT_FOUND)    
