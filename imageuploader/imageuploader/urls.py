
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

