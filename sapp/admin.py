from django.contrib import admin
from .models import register,dept,course,order
# Register your models here.
admin.site.register(register)
admin.site.register(dept)

admin.site.register(course)
admin.site.register(order)
