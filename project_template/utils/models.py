from __future__ import unicode_literals
from django.utils.timezone import now
from django.db import models


class DateTimeBase(models.Model):

    class Meta:
        abstract = True

    created = models.DateTimeField(null=True, editable=False)
    updated = models.DateTimeField(null=True, editable=False)

    def save(self, *args, **kwargs):
        _now = now()
        self.updated = _now
        if not self.id:
            self.created = _now
        super(DateTimeBase, self).save(*args, **kwargs)

