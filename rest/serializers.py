from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        exclude = ()
        depth = 1


