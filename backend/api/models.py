from django.db import models


class Note(models.Model):
    """
    Note model stores simple notes with title and content.
    created_at and updated_at are managed automatically.
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.pk})"
