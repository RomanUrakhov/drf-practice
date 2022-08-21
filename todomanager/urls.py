from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserModelCustomViewSet, JWTGeneratePairView, JWTRefreshView
from todo.views import ProjectViewSet, TodoViewSet

router = DefaultRouter()
router.register('user', UserModelCustomViewSet)
router.register('todo', TodoViewSet)
router.register('project', ProjectViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token/', JWTGeneratePairView.as_view()),
    path('token/refresh/', JWTRefreshView.as_view()),
]
