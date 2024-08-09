from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phoenix.urls')),  # Ensure 'phoenix.urls' is correctly included 
]
