from rest_framework import serializers
from app.core.models import JobTitle, Portal, JobDescription


class JobTitleSerializer(serializers.ModelSerializer):
    """
    Serializer class for JobTitle list view
    """

    class Meta:
        model = JobTitle
        fields = ["id", "title"]
        read_only_fields = ["id"]


class JobDescriptionSerializer(JobTitleSerializer):
    """
    TODO
    - https://www.django-rest-framework.org/api-guide/serializers/#overriding-serialization-and-deserialization-behavior

    """

    class Meta(JobTitleSerializer.Meta):
        fields = JobTitleSerializer.Meta.fields + [
            "job_description", "portal"
        ]

