import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

from .forms import SMSForm

CUR_PATH = os.path.abspath(__file__)
SMS_TEST_PATH = os.path.dirname(CUR_PATH)
APP_PATH = os.path.dirname(SMS_TEST_PATH)
ROOT_PATH = os.path.dirname(APP_PATH)
CONF_PATH = os.path.join(ROOT_PATH, '.conf')
config = json.loads(open(os.path.join(CONF_PATH, 'settings_local.json')).read())


def index(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
        print(request)
        if form.is_valid():
            numbers = form.cleaned_data['recipient_numbers']
            content = form.cleaned_data['content']
            api_key = config["sms"]["api_key"]
            api_secret = config["sms"]["api_secret"]
            params = dict()
            params['type'] = 'sms'
            params['to'] = numbers
            params['from'] = config["sms"]["sender_number"]
            params['text'] = content
            cool = Message(api_key, api_secret)
            print(cool)
            try:
                response = cool.send(params)
                return HttpResponse("Success")

            except CoolsmsException as e:
                print("Error Code : %s" % e.code)



    else:
        form = SMSForm(
            initial={
                'recipient_numbers': '010-8494-1303'
            }
        )
    content = {
        'form': form,
    }

    return render(request, 'common/index.html', content)
