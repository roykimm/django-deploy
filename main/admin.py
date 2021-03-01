from django.contrib import admin
from .models import Memo

# Register your models here.
@admin.register(Memo)
class MemoModel(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)