from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer


class DestinationListCreateAPI(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationRetrieveAPI(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationDeleteAPI(generics.DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer



import requests
from django.shortcuts import render, redirect

API_BASE = "http://127.0.0.1:8000/api/destination/"

def front_list_view(request):
    api_url = "http://127.0.0.1:8000/api/destination/"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            destinations = response.json()
        else:
            destinations = []
    except:
        destinations = []

    return render(request, "destination_list.html", {"destinations": destinations})


import requests

def front_create_view(request):
    if request.method == "POST":
        api_url = "http://127.0.0.1:8000/api/destination/"

        data = {
            "Place": request.POST.get("Place"),
            "Weather": request.POST.get("Weather"),
            "District": request.POST.get("District"),
            "State": request.POST.get("State"),
            "Map": request.POST.get("Map"),
            "Description": request.POST.get("Description"),
        }

        files = {}
        if "Image" in request.FILES:
            files["Image"] = request.FILES["Image"]

        requests.post(api_url, data=data, files=files)

        return redirect("destination_list")

    return render(request, "destination_create.html")

def front_edit_view(request, id):
    detail_url = f"{API_BASE}{id}/"
    update_url = f"{API_BASE}{id}/update/"

    response = requests.get(detail_url)
    destination = response.json()

    if request.method == "POST":
        data = {
            "Place": request.POST.get("Place"),
            "Weather": request.POST.get("Weather"),
            "District": request.POST.get("District"),
            "State": request.POST.get("State"),
            "Map": request.POST.get("Map"),
            "Description": request.POST.get("Description"),
        }

        image = request.FILES.get("Image")
        files = {"Image": image} if image else None

        requests.put(update_url, data=data, files=files)

        return redirect("destination_list")

    return render(request, "destination_edit.html", {"destination": destination})

def front_delete_view(request, id):
    delete_url = f"{API_BASE}{id}/delete/"
    requests.delete(delete_url)
    return redirect("destination_list")



