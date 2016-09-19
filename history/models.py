from __future__ import unicode_literals

from django_mongoengine import Document, fields
from django.db import models

# Create your models here.

class LogHistory(Document):
    description = fields.StringField()