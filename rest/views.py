from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from payment.models import Payment
from .serializers import PaymentSerializer


class PaymentAPIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        """
        Return a list of all users.
        """

        payments = Payment.objects.filter(person__identity_num=kwargs['identity_number'],
                                          institution__account_number=kwargs['account_number'])
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
