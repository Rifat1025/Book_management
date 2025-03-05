from django.contrib import admin
from demo.models import Demo,Book

admin.site.register(Demo)
class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','description','published_year']

admin.site.register(Book,BookAdmin)

