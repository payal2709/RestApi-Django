from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from college import views
from django.views.generic.base import RedirectView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'notice',views.NoticeViewSet)
router.register(r'student',views.StudentViewSet)

#if url contains home/ then navigate to Home
# if url is blank like only ip address is given and no page mentioned, then also navigate to home
urlpatterns = [
    path(r'api/',include(router.urls)),
    path('',RedirectView.as_view(url='api/')),
]
