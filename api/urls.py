from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('companies', views.CompanyView, basename='Company')
# router.register('members', views.MemberView)
router.register('members', views.MemberView, basename='Member')

urlpatterns = [
    path('', include(router.urls))
]
