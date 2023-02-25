from django.urls import path, include
from rest_framework import routers
from .views import *
from .routers import CustomReadOnlyRouter

router = routers.DefaultRouter()
router_dynamic = CustomReadOnlyRouter()

router.register(r'personal', PersonalMVS)
router.register(r'', DepartmentMVS)
router_dynamic.register(r'department', DynamicDepartmentMVS)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router_dynamic.urls)),
]

#? 2nd
# urlpatterns = router.urls
# urlpatterns += router_dinc.urls