from django.urls import path
from . import views

urlpatterns = [
    path("api/destination/", views.DestinationListCreateAPI.as_view(), name="api_destination_list_create"),
    path("api/destination/<int:pk>/", views.DestinationRetrieveAPI.as_view(), name="api_destination_detail"),
    path("api/destination/<int:pk>/update/", views.DestinationUpdateAPI.as_view(), name="api_destination_update"),
    path("api/destination/<int:pk>/delete/", views.DestinationDeleteAPI.as_view(), name="api_destination_delete"),

    # frontend pages
    path("", views.front_list_view, name="destination_list"),
    path("create/", views.front_create_view, name="destination_create"),
    path("edit/<int:id>/", views.front_edit_view, name="destination_edit"),
    path("delete/<int:id>/", views.front_delete_view, name="destination_delete"),
]
