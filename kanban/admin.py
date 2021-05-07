from django.contrib import admin
from .models import List

admin.site.register(List)

from .models import Card

admin.site.register(Card)

# Register your models here.
