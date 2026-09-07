from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import requests
from dotenv import load_dotenv
load_dotenv()
import os 
API_KEY = os.getenv("TFNSW_API_KEY")
# Create your views here.

# home page 
def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

def get_metro_position(request):
    url = "https://api.transport.nsw.gov.au/v2/gtfs/vehiclepos/metro"

    try:
        response = requests.get(url, headers={"Authorization": f"apikey {API_KEY}"}, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors

        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)
        data = MessageToDict(feed, preserving_proto_field_name=True)
        with open('metro_positions.json', 'w') as f:
            f.write(json.dumps(data, indent=4))  # Save the data to a JSON file
        return HttpResponse("Metro positions saved.")  # Return the data as JSON response
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)})
    # return HttpResponse("hello world")