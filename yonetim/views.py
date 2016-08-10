from django.shortcuts import render
from .models import User
# Create your views here.
def hello(req):
	return render(req,"sablon/home.html",{})
def users(req):
	users=User.objects.all().order_by('adi')
	return render(req,"sablon/users.html",{'kisiler':users})