from django.shortcuts import render

from .forms import SMSForm


def index(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
    else:
        form = SMSForm(
            initial={
                'recipient_numbers': '010-8494-1303, 010-1234-1234, 0212341234'
            }
        )
    content = {
        'form': form,
    }
    return render(request, 'common/index.html', content)
