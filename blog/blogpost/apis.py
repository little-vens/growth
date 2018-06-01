from .models import Blogpost
from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions

class BlogpostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blogpost
        fields = ('title', 'author', 'body', 'slug', 'id')

class BlogpostSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
    serializer_class = BlogpostSerializer
    search_fields = 'title'
    queryset = Blogpost.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Blogpost.objects.all()

        search_param = self.request.query_params.get('title', None)
        if search_param is not None:
            queryset = Blogpost.objects.filter(title__contains=search_param)

        serializer = BlogpostSerializer(queryset, many=True)
        return Response(serializer.data)