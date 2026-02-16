from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "Backend is working ✅"})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]
