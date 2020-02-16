from django.urls import path
from django.views.generic import TemplateView

from .views import signin, signup, UserDetail, root

urlpatterns = [
    path(r'signin/', signin, name='signin'),
    path(r'signup/', signup, name='signup'),
    path('', root, name='root'),
    path(r'<uuid:id>', UserDetail.as_view(), name='user-detail'),
]
