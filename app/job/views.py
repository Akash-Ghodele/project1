from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from serializers import JobTitleSerializer, JobDescriptionSerializer
from app.core.models import JobTitle


class JobTitleViewSet(viewsets.ModelViewSet):
    serializer_class = JobDescriptionSerializer
    queryset = JobTitle.objects.all()

    def get_serializer_class(self):

        if self.action == "list":
            return JobTitleSerializer

        return self.serializer_class

    def get_queryset(self):

        return self.queryset.filter(user=self.request.user).order_by("-id")


class CreateUserView(CreateAPIView):
    pass
