from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.db import models

from utils.models import DateTimeBase

import pickle


class Client(DateTimeBase):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s" % self.name


class ClientPriority(DateTimeBase):
    client = models.OneToOneField(Client)
    data = models.TextField()

    def __unicode__(self):
        return u"%s" % self.client.name

    @property
    def data_dict(self):
        return pickle.loads(self.data)


    def save(self, *args, **kwargs):
        if not self.data:
            self.data = pickle.dumps({})
        return super(ClientPriority, self).save(*args, **kwargs)


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

    def reorder_client_priority(self, order):
        client_priority_obj, created = ClientPriority.objects.get_or_create(
            client=self.client)

        data = client_priority_obj.data_dict

        if not data:
            data = {}

        current_requests_str = data.keys()
        current_requests_int = [int(x) for x in current_requests_str]

        current_requests_int.sort()

        if order < 1:
            if current_requests_int:
                order = current_requests_int[-1] + 1
            else:
                order = 1


        current_requests_int_reversed = [x for x in current_requests_int]
        current_requests_int_reversed.reverse()

        if order in current_requests_int_reversed:
            i = 0
            for x in current_requests_int_reversed:
                if i == 0:
                    data[str(x+1)] = data[str(x)]
                if x > order:
                    if str(x-1) in data and str(x) in data:
                        data[str(x)] = data[str(x-1)]

            data[str(order)] = self.id

        elif current_requests_int:
            data[str(current_requests_int[-1]+1)] = self.id
        else:
            data[str(1)] = self.id

        client_priority_obj.data = pickle.dumps(data)
        client_priority_obj.save()

    @property
    def client_priority(self):
        data = {}
        try:
            data = ClientPriority.objects.get(
                client=self.client).data_dict
        except ClientPriority.DoesNotExist:
            data = {}
        if data:
            id = self.id
            for k, v in data.items():
                if id == v:
                    return k

        return None

















