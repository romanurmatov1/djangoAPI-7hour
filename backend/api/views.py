from django.http import JsonResponse

def api_home(request, *args, **kywargs):
    return JsonResponse({"message":"Hello my project!"})