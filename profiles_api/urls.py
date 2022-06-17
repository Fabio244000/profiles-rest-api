from .views import HelloApiView, HelloViewSets, UserProfileViewSet, UserLoginApiView, UserProfileFeedItemViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello-view-set', HelloViewSets, basename='test-view-set')
router.register('user-profile', UserProfileViewSet)
router.register('feed', UserProfileFeedItemViewSet, basename='feed-item')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view(), name='test-hello-view'),
    path('login/', UserLoginApiView.as_view(), name='user-login-view'),  # urls maps for APIViews
    path('', include(router.urls)),  # urls map for ViewSets using routers
]
"""If the Vietset have a query for the table, Not pass basename arguemnt to register an url"""