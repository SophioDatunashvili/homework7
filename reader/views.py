from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ReaderForm


# Create your views here.
def reader_create_view(request):
    form = ReaderForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'reader/form.html', context)


def my_view(request):
    if request.method == 'POST':
        # Process the form data

        # Redirect to the destination HTML file
        return HttpResponseRedirect('/templates/book_list.html')
