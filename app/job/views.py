from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .serializers import JobTitleSerializer, JobDescriptionSerializer
from core.models import JobTitle
from job import serializers
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

        if self.action == "list":
            return JobTitleSerializer

        # localhost:8000/app/job/jobtitle prural
        # localhost:8000/app/job/jobtitle/id=1 singular

        return self.serializer_class

    def get_queryset(self):
        return self.queryset


        return self.queryset.filter(user=self.req.useuestr).order_by("-id")

    def perform_create(self, serializer_obj):
        """Create a job title
        """

        serializer_obj.save(user=self.request.user)



class CreateUserView(CreateAPIView):
    pass
