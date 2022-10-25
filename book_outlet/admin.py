from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug") #these feature makes the field read-only in the admin form
    prepopulated_fields = {"slug":("title",)} #this field just pre-populates the mentioned fieldwith the given one
    list_filter = ("author","title",)
    list_display = ("title","author",)
admin.site.register(Book, BookAdmin) # telling django to add/register the newly created model into admin section
