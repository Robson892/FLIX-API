from genres.models import Genre
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from rest_framework import generics
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermissions,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermissions,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
