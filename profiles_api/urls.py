from .views import HelloApiView
from django.urls import path
'''
This is only for APIViews
'''
urlpatterns = [
    path('hello-view/', HelloApiView.as_view(), name='test-hello-view'),
]
