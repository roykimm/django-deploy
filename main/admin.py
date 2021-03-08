from django.contrib import admin
from .models import Memo, Book

# Register your models here.
@admin.register(Memo)
class MemoModel(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)

@admin.register(Book)
class BookModel(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)