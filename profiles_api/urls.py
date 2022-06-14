from .views import HelloApiView, HelloViewSets
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-view-set', HelloViewSets, basename='test-view-set')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view(), name='test-hello-view'),  # urls maps for APIViews
    path('', include(router.urls))  # urls map for ViewSets using routers
]
