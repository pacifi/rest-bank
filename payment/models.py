from uuid import uuid4

from django.db import models

from setup.models import Person, Institution


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid4)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    amount = models.DecimalField(u"Amount", max_digits=6, decimal_places=2)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    created_at = models.DateTimeField(u"Created at", auto_now_add=True)
    updated_at = models.DateTimeField(u"Updated at", auto_now=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return "%s" % self.person
