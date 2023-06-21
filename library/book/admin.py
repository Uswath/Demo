from django.contrib import admin

from book.models import book, student


#To register table name in admin
admin.site.register(book)
admin.site.register(student)
