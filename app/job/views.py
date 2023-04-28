from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .serializers import JobTitleSerializer, JobDescriptionSerializer
from app.core.models import JobTitle
from app.job import serializers
from rest_framework import serializers


from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet


class JobTitleViewSet(viewsets.ModelViewSet):
    """
    /api/jobtitle (plural)
    /api/jobtitle/481241 (singular)
    """

    serializer_class = JobDescriptionSerializer
    queryset = JobTitle.objects.all()

    def get_serializer_class(self):
        """Returns the serializer class to be used for the request"""

        if self.action == "list":
            return JobTitleSerializer

        return self.serializer_class

    def get_queryset(self):
        """
        We want to filter out jobtitles for authenticated users
        """

        return self.queryset

    def perform_create(self, serializer_obj):
        """Create a new job title
        # TODO - refer
        https://www.django-rest-framework.org/api-guide/generic-views/#methods
        Args:
            serializer: validated serializer
        Returns:
        """

        serializer_obj.save(user=self.request.user)


class CreateUserView(CreateAPIView):
    pass