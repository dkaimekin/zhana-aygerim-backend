from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"orders", views.IndexViewSet)
router.register(r"images", views.ImageViewSet)

urlpatterns = [path("api/", include(router.urls))]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
