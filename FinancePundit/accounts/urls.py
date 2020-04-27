from django.urls import path
from django.views.generic import TemplateView

from .views import signin, signup, logout, root, user, UserDetail

urlpatterns = [
    path(r'', root, name='root'),
    path(r'user/', user, name='user'),
    path(r'auth/signin/', signin, name='signin'),
    path(r'auth/signup/', signup, name='signup'),
    path(r'auth/logout/', logout, name='logout'),
    path(r'auth/<uuid:id>', UserDetail.as_view(), name='user-detail'),
]
