from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    person_name = serializers.SerializerMethodField()
    number_transaction = serializers.SerializerMethodField()
    institution_name = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        exclude = ()

    def get_person_name(self, obj):
        return "%s %s %s" % (obj.person.first_name, obj.person.last_father_name, obj.person.last_mother_name)

    def get_number_transaction(self, obj):
        return "%s" % (obj.id)

    def get_institution_name(self, obj):
        return "%s" % (obj.institution.name)
