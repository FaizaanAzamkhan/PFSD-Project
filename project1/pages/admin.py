from django.contrib import admin

# Register your models here.
from .models import Register,RoomAllocation

admin.site.register(Register)

admin.site.register(RoomAllocation)

