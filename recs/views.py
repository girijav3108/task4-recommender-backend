from django.http import JsonResponse

def recommend(request):
    data = {
        "recommendations": [
            "Laptop",
            "Mobile",
            "Headphones",
            "Smart Watch"
        ]
    }
    return JsonResponse(data)
