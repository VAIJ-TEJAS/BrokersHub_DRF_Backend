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

import os
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.http import FileResponse
from otp.views import GenerateOTP, ResetPassword, VerifyOTP
from rest_framework.views import APIView
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response

from user import views as user_views
from requirement import views as requirement_views
from advertisement import views as advertisement_views
from deal import views as deal_views


class FileView(APIView):
    def get(self, request):
        file_path = "A1B5AA01AC351DC6FE0DC0DD5E134293.txt"
        file_path = os.path.join(settings.MEDIA_ROOT, file_path)

        if os.path.exists(file_path):
            file = open(file_path, "rb")
            response = FileResponse(file)
            return response
        else:
            return Response({"error": "File not found"}, status=404)


router = DefaultRouter()
router.register("signup", user_views.Signup, basename="signup")
router.register(
    "requirements", 
    requirement_views.RequirementViewSet, 
    basename="requirements"
)
router.register(
    "my-requirements",
    requirement_views.MyRequirementViewSet,
    basename="my-requirements",
)
router.register(
    "advertisements",
    advertisement_views.AdvertisementViewSet,
    basename="advertisements",
)
router.register(
    "my-advertisements",
    advertisement_views.MyAdvertisementViewSet,
    basename="my-advertisements",
)
router.register("deals", deal_views.DealViewSet, basename="deals")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("auth/", user_views.Signin.as_view()),
    path('generate-otp/', GenerateOTP.as_view(), name='generate-otp'),
    path('verify-otp/', VerifyOTP.as_view(), name='verify-otp'),
    path('reset-password/', ResetPassword.as_view(), name='reset-password'),
    path(
        ".well-known/pki-validation/A1B5AA01AC351DC6FE0DC0DD5E134293.txt/",
        FileView.as_view(),
        name="file-view",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
