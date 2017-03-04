from django.http import HttpResponse
from django.shortcuts import render

from .forms import SMSForm


def index(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():
            numbers = form.cleaned_data['recipient_numbers']
            return HttpResponse(numbers)
    else:
        form = SMSForm(
            initial={
                'recipient_numbers': '010-8494-1303, 0212341234, 0123231'
            }
        )
    content = {
        'form': form,
    }
    return render(request, 'common/index.html', content)
