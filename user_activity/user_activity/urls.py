from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('activity/', include('user_activity_details.urls')),
    path('admin/', admin.site.urls),
]