from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Faq
from .forms import FaqForm
# Create your views here.


def faq(request):
    """ a view to return the faqs page """
    faq = Faq.objects.all()

    context = {
        'faq': faq
    }

    return render(request, 'faq/faq.html', context)


""" login decorater so only the admin that is logged in can add a faq """


@login_required
def add_faq(request):
    """ Add a faq to faq page"""

    if not request.user.is_superuser:
        messages.error(request, 'Only the guys at Jerseys for Tims can do this :)')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ has been successfully added to list of faqs!')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request, 'Failed to add FAQ. Please check the form is valid and again')
    else:
        form = FaqForm()

    template = 'faq/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


""" login decorater to allow only the admin that is logged in to edit faqs """


@login_required
def edit_faq(request, faq_id):
    """a view to edit the faq"""
    if not request.user.is_superuser:
        messages.error(request, 'Only our siopaFIA team can access this.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ successfully updated!')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request, 'Unable to update faq. Please check your form.')
    form = FaqForm(instance=faq)
    messages.warning(request, f'You are editing - {faq.question}')

    template = 'faq/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete a faq """
    if not request.user.is_superuser:
        messages.error(request, 'Only the guys at Jerseys for Tims can do this team are permitted to do this.')
        return redirect(reverse('home'))

    Faq = get_object_or_404(Faq, pk=faq_id)
    Faq.delete()
    messages.success(request, 'FAQ has been deleted')
    return redirect(reverse('faq'))