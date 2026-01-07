from django.contrib import admin
from django.urls import path, include  # importe include

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, reverse, include


urlpatterns = [
    path("secret-admin/", admin.site.urls),
    path("", include("myapp.urls")),
    path('pix/', include('pix.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)