from .views import HelloApiView, HelloViewSets, UserProfileViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-view-set', HelloViewSets, basename='test-view-set')
router.register('user-profile', UserProfileViewSet)

urlpatterns = [
    path('hello-view/', HelloApiView.as_view(), name='test-hello-view'),  # urls maps for APIViews
    path('', include(router.urls))  # urls map for ViewSets using routers
]
"""If the Vietset have a query for the table, Not pass basename arguemnt to register an url"""