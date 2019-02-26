from uuid import uuid4

from django.db import models

DNI = "DNI"
FOREIGN_CARD = "FOREIGN_CARD"

IDENTY_TYPE_CHOICES = (
    (DNI, DNI),
    (FOREIGN_CARD, FOREIGN_CARD),
)


class Person(models.Model):
    u"""
    Model Person
    """
    first_name = models.CharField(u"First Name", max_length=150)
    last_father_name = models.CharField(u"Last Father Name", max_length=150)
    last_mother_name = models.CharField(u"Last Mother Name", max_length=150)
    identity_type = models.CharField(U"Identity Type", max_length=150, choices=IDENTY_TYPE_CHOICES)
    identity_num = models.CharField(u"Identity Num", max_length=15, unique=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_father_name, self.identity_num)


class Institution(models.Model):

    name = models.CharField(u"Name", max_length=50)
    identity_num = models.CharField(max_length=15, unique=True)
    detail_acount = models.CharField(u"Detai account", max_length=150)
    account_number = models.CharField(u"Account number", max_length=50, unique=True)

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"

    def __str__(self):
        return "%s %s" % (self.name, self.account_number)
