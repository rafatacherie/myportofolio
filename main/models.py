import uuid
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True, default="")
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-start_year"]

    def __str__(self):
        return self.institution

    @property
    def is_ongoing(self):
        return self.end_year is None

    @property
    def period_label(self):
        if self.is_ongoing:
            return f"{self.start_year} - Present"
        return f"{self.start_year} - {self.end_year}"

class Skill(models.Model):
    SKILL_TYPE_CHOICES = [
        ('technical', 'Technical Skills'),
        ('soft', 'Soft Skills'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)        
    percentage = models.IntegerField()             
    icon_class = models.CharField(max_length=50)
    skill_type = models.CharField(max_length=15, choices=SKILL_TYPE_CHOICES) 

    def __str__(self):
        return f"{self.name} ({self.get_skill_type_display()})"