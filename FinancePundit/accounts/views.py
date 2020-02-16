from django.shortcuts import redirect, render
from requests import HTTPError
from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine.generics import RetrieveUpdateDestroyAPIView

from .models.User import User
from .serializers import UserSerializer
from .services.firebase import FireBase


def signin(request):
    firebase = FireBase()
    user = firebase.sign_in(request.POST['email'], request.POST['password'])
    if user:
        request.session['userId'] = str(User.objects.get(firebaseId=user['localId']).id)
        return redirect("/dashboard/")
    else:
        return redirect("/error/", {'error': 'Invalid username/password'})


def signup(request):
    firebase = FireBase()
    try:
        user = firebase.sign_up(request.POST['email'], request.POST['password'])
        if user:
            request.session['userId'] = str(User.objects.create_user(**user).id)
            return render(request, "user.html")
    except HTTPError as error:
        return redirect("/error/", {'error': error})


def root(request):
    if request.session.get('userId', None) is not None:
        return render(request, "user.html")
    else:
        return redirect("/")


class UserDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer
    queryset = User.objects

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        request.data.update(kwargs)
        return Response(data=UserSerializer(User.objects.update(**request.data)).data,
                        status=status.HTTP_200_OK)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(self, request, *args, **kwargs)
