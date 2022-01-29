from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),
    # allauth has default routing
    path('accounts/', include('allauth.urls')),
]
