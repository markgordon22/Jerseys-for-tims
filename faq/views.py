from django.shortcuts import render

# Create your views here.
def faq(request):
    """a view to return the about page """
    return render(request, 'faq/faq.html')
