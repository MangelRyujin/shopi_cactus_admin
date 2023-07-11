from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from apps.Order.api.serializers.order_serializers import OrderSerializer,Items_OrderSerializer

# Create order
@api_view(['POST'])
def create_order_api_view(request):
    if request.method == 'POST':
        order_serializers = OrderSerializer(data = request.data)
        items = request.data['items']
        if order_serializers.is_valid():
            order_serializers.save()
            return Response({'message':'Corectly created order!!!','order_id':order_serializers.data['id'],'items':items}, status=status.HTTP_201_CREATED)
        return Response({'errors':order_serializers.errors}, status= status.HTTP_400_BAD_REQUEST)
    
# Create items order
def create_items_order_api_view(request):
    if request.method == 'POST':
        items = request.data
        if items:
            return Response({'message':items}, status=status.HTTP_200_OK)
        return Response({'message':'mal'}, status=status.HTTP_400_BAD_REQUEST)
        # items_serializers = Items_OrderSerializer(data = request.data,many = True)
        # if items_serializers.is_valid():
        #     items_serializers.save()
        #     return Response({'message':'Corectly created items!!!'}, status=status.HTTP_201_CREATED)
        # return Response({'errors':items_serializers.errors}, status= status.HTTP_400_BAD_REQUEST)