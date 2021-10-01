from django.shortcuts import render

def index(request):
    return render(request, "base.html")

def search(request):
    results = request.GET.get("results")
    return render(request, "search_results.html", {'results':results})