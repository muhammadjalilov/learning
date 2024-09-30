from rest_framework import serializers
from apps.transactions.models import Earnings

class EarningsSerializer(serializers.ModelSerializer):
    net_revenue = serializers.SerializerMethodField()

    class Meta:
        model = Earnings
        fields = ['instructor', 'gross_revenue', 'net_revenue']

    def get_net_revenue(self, obj):
        return getattr(obj, 'net_revenue', None)
