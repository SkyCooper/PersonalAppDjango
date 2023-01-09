from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("personal", PersonalMVS)
router.register("department", DepartmentMVS)

urlpatterns = router.urls
