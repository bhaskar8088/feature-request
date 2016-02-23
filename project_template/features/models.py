from __future__ import unicode_literals
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.db import models

from utils.models import DateTimeBase


class Client(DateTimeBase):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.name


class FeatureRequest(DateTimeBase):
    '''
    A model to store feature requests
    '''

    PRODUCT_AREA_CHOICE_POLICIES = 1
    PRODUCT_AREA_CHOICE_BILLING = 2
    PRODUCT_AREA_CHOICE_CLAIMS = 3
    PRODUCT_AREA_CHOICE_REPORTS = 4

    PRODUCT_AREA_CHOICES = (
        (PRODUCT_AREA_CHOICE_POLICIES, "Policies"),
        (PRODUCT_AREA_CHOICE_BILLING, "Billing"),
        (PRODUCT_AREA_CHOICE_CLAIMS, "Claims"),
        (PRODUCT_AREA_CHOICE_REPORTS, "Reports"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    client = models.ForeignKey(Client)
    target_date = models.DateField()
    ticket_url = models.URLField()
    product_area = models.IntegerField(choices=PRODUCT_AREA_CHOICES)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return u"%s" % self.title

    @property
    def slug(self):
        return slugify(self.title)[:20]



class ClientPriority(DateTimeBase):
    client = models.OneToOneField(Client)
    data = JSONField()

    def __unicode__(self):
        return u"%s" % self.client.name


