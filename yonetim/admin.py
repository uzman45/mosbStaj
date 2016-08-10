from django.contrib import admin
from .models import User
# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
	list_display=["adi","soyadi","telNo",'eMail']
	search_fields=["adi","soyadi","telNo",'eMail']
	class Meta:
		model=User
admin.site.register(User,UserModelAdmin)