from django.shortcuts import render

# Create your views here.


def about(request):
    """a view to return the about page """
    return render(request, 'about/about.html')