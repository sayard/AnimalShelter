from django.core.exceptions import ValidationError
from django.db import models
from django.core.mail import EmailMessage
from .secret import secret_email


def send_email_notification():
    email = EmailMessage('Important Animal Shelter Notification',
                         'It seems that there are few places left in your animal sheler, consider relesing some '
                         'animals.',
                         to=[secret_email])
    email.send()


def validate_available_places(obj):
    model = obj.__class__
    if model.objects.count() > 19 and obj.id != model.objects.get().id: #send email notification
        send_email_notification()
    elif model.objects.count() > 24 and obj.id != model.objects.get().id: #shelter is full
        raise ValidationError("Shelter is full. Release some animals" % model.__name__)


class Animal(models.Model):
    name = models.CharField(max_length=80)
    color = models.CharField(max_length=30)
    species = models.CharField(max_length=40)
    description = models.TextField(default='')
    description.null = False
    age = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def clean(self):
        validate_available_places(self)

    def __str__(self):
        return self.name
