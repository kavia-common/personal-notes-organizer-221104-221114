from typing import Any

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from .models import Note
from .serializers import NoteSerializer


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def health(request):
    """
    PUBLIC_INTERFACE
    Health check endpoint.
    Returns:
      200 JSON { "message": "Server is up!" }
    """
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
@api_view(["GET", "POST"])
@renderer_classes([JSONRenderer])
def notes_collection(request):
    """
    Notes collection endpoint.
    - GET: List notes (ordered by -updated_at).
    - POST: Create a note. Body: {title, content}
    Returns appropriate status codes and error messages.
    """
    if request.method == "GET":
        queryset = Note.objects.all().order_by("-updated_at")
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# PUBLIC_INTERFACE
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@renderer_classes([JSONRenderer])
def note_detail(request, pk: int):
    """
    Single note endpoint.
    - GET: Retrieve note by id.
    - PUT/PATCH: Update fields (title, content).
    - DELETE: Remove note.
    Returns proper status codes.
    """
    note = get_object_or_404(Note, pk=pk)

    if request.method == "GET":
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    if request.method in ("PUT", "PATCH"):
        partial = request.method == "PATCH"
        serializer = NoteSerializer(note, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
