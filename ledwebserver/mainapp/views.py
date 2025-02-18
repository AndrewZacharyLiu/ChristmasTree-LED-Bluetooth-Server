from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.shortcuts import render
from mainapp.bluetoothcommand import *

def submit_color(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)  # Parse the JSON request body
        color = data.get("color")

        # Process the pattern value as needed
        print(f"Color selected: {color}")
        message = f"COLOR:{color.lstrip('#')}"
        bluetooth_connection.send(message)

    # Wait for a response (adjust timeout as needed)
        result_string = bluetooth_connection.receive()
        # Send a JSON response back to the client
        return JsonResponse({"message": result_string})

    return JsonResponse({"error": "Invalid request"}, status=400)
 
def submit_gradient(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)  # Parse the JSON request body
        color1 = data.get("color1")
        color2 = data.get("color2")

        # Process the pattern value as needed
        print(f"Gradient selected: {color1} , {color2}")
        message = f"GRAD:{color1.lstrip('#')}{color2.lstrip('#')}"
        bluetooth_connection.send(message)

    # Wait for a response (adjust timeout as needed)
        result_string = bluetooth_connection.receive()
        # Send a JSON response back to the client
        return JsonResponse({"message": result_string})

    return JsonResponse({"error": "Invalid request"}, status=400)

def submit_pattern(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)  # Parse the JSON request body
        pattern = data.get("pattern")

        # Process the pattern value as needed
        print(f"Pattern selected: {pattern}")
        message = f"PATTERN:{pattern}"
        bluetooth_connection.send(message)

    # Wait for a response (adjust timeout as needed)
        result_string = bluetooth_connection.receive()
        # Send a JSON response back to the client
        return JsonResponse({"message": result_string})

    return JsonResponse({"error": "Invalid request"}, status=400)


def mainapp(request):
  return render(request, 'index.html')

def color(request):
  return render(request, 'color.html')

def gradient(request):
  return render(request, 'gradient.html')

def pattern(request):
  return render(request, 'pattern.html')
