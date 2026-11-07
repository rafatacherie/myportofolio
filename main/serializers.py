from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Project


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
        ]
        # id dibuat otomatis (UUID default), tidak boleh ditentukan lewat input API
        read_only_fields = ["id"]

    # Validasi tambahan, menggantikan peran clean_title/clean_tech_stack/
    # clean_description pada ProjectForm (main/forms.py) untuk jalur API.
    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value).strip()

    def validate_tech_stack(self, value):
        return strip_tags(value).strip()

    # SerializerMethodField -> otomatis read-only, memanggil get_<nama_field>
    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())


class ExperienceSerializer(serializers.ModelSerializer):
    # started_at/ended_at di ExperienceForm memakai widget bulan-tahun (%Y-%m)
    started_at = serializers.DateField(input_formats=["%Y-%m", "%Y-%m-%d", "iso-8601"])
    ended_at = serializers.DateField(
        required=False,
        allow_null=True,
        input_formats=["%Y-%m", "%Y-%m-%d", "iso-8601"],
    )

    category_display = serializers.CharField(source="get_category_display", read_only=True)
    period_label = serializers.CharField(read_only=True)
    is_ongoing = serializers.BooleanField(read_only=True)

    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            "id", "title", "role", "description", "category", "category_display",
            "thumbnail", "started_at", "ended_at", "period_label", "is_ongoing",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    # Validasi tambahan, menggantikan peran clean_title/clean_role/clean_description
    # pada ExperienceForm (main/forms.py) untuk jalur API.
    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_role(self, value):
        return strip_tags(value).strip()
 
    def validate_description(self, value):
        return strip_tags(value).strip()
 
    def get_star_count(self, obj):
        return obj.starred_by.count()
 
    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()
 
    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())