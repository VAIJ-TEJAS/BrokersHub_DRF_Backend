"""brokershub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from user import views as user_views
from requirement import views as requirement_views
from advertisement import views as advertisement_views
from deal import views as deal_views

router = DefaultRouter()
router.register('signup', user_views.Signup, basename='signup')
router.register('requirements', requirement_views.RequirementViewSet, basename='requirements')
router.register('advertisements', advertisement_views.AdvertisementViewSet, basename='advertisements')
router.register('deals', deal_views.DealViewSet, basename='deals')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path('auth/', user_views.Signin.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
