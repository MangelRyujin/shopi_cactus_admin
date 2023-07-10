from rest_framework import serializers
from apps.Order.models import Items_Order, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
        def to_representation(self, instance):
            return {
                'user_id': instance.user_id,
                'cost': instance.cost,
            }
            
        def validate_cost(self,value):
            if value < 0:
                raise serializers.ValidationError("El costo debe de ser mayor que 0")
            return value
        
class Items_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_Order
        fields = '__all__'
        
        def to_representation(self, instance):
            return{
                'plant': instance.plant,
                'order': instance.order,
                'cost': instance.cost,
                'qty': instance.qty,
            }
            
        def validate_cost(self,value):
            if value < 0:
                raise serializers.ValidationError("El costo debe de ser mayor que 0")
            return value   