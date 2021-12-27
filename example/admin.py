from django.contrib import admin
from .models import Example

# Register your models here.
admin.site.register(Example) # 등록시 관리자 페이지에서 모델관리 가능