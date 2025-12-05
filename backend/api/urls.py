from django.urls import path
from .views import health, notes_collection, note_detail

urlpatterns = [
    path("health/", health, name="Health"),
    path("notes/", notes_collection, name="notes-collection"),
    path("notes/<int:pk>/", note_detail, name="note-detail"),
]
