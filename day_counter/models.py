from django import forms
from django.contrib.auth.models import User
from django.db.models import Model, DateTimeField, DateField, TimeField, BooleanField, CharField, ImageField, UUIDField
from django.db.models import ForeignKey, IntegerField, CASCADE, UniqueConstraint, Q
from datetime import datetime, timedelta, date
import uuid
from crispy_forms.helper import FormHelper


class Counter(Model):
    id = IntegerField('id', primary_key=True)
    title = CharField('Title', max_length=255, null=False, blank=False)
    image = ImageField(upload_to='images', null=True, blank=True)
    create_date = DateTimeField(auto_now_add=True)
    modify_date = DateTimeField(auto_now=True)
    end_date = DateField('End date', null=False)
    end_time = TimeField('End time', null=True, blank=True)
    guid = UUIDField('Unique Id', default=uuid.uuid4, unique=True)
    is_guest = BooleanField(default=True)
    user = ForeignKey(User, null=True, blank=True, on_delete=CASCADE)

    def __str__(self):
        return f'{self.id}: {self.title}'

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'title'], condition=Q(is_guest=False), name='unique_title_for_user')
        ]
