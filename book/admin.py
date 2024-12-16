from django.contrib import admin

from.models import Book
from .models import Student, Address,ImageModel

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Address)
admin.site.register(ImageModel)