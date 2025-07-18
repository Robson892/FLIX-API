from django.urls import path
from . import views

urlpatterns = [
    path("review/", views.ReviewCreateListView.as_view(), name="review-crete-list"),
    path(
        "review/<int:pk>/",
        views.ReviewRetrieveUpdateDestroyView.as_view(),
        name="review-detail-view",
    ),
]
