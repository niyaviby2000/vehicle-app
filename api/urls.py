from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.routers import DefaultRouter

from api import views

router=DefaultRouter()

router.register("customers",views.CustomerViewSetView,basename="customers")

router.register("work",views.CustomerViewSetView,basename="work")

urlpatterns=[

    path('token/',ObtainAuthToken.as_view()),

    path('customers/<int:pk>/work/',views.WorkCreationView.as_view()),

    path('work/<int:pk>/',views.WorkDetailView.as_view()),


]+router.urls