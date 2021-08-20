from django.shortcuts import render
from .models import Faq
# Create your views here.


def faq(request):
    """ a view to return the faqs page """
    faq = Faq.objects.all()

    context = {
        'faq': faq
    }

    return render(request, 'faq/faq.html', context)
