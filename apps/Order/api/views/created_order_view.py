from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from apps.Order.api.serializers.order_serializers import OrderSerializer

# Create order
@api_view(['POST'])
def create_order_api_view(request):
    
    
    if request.method == 'POST':
        order_serializers = OrderSerializer(data = request.data)
        if order_serializers.is_valid():
            order_serializers.save()
            return Response({'message':'Corectly created order!!!'}, status=status.HTTP_201_CREATED)
        return Response({'errors':order_serializers.errors}, status= status.HTTP_400_BAD_REQUEST)