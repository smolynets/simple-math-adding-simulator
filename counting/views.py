from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from counting.models import FinishPerDay
from counting.utils import get_max_number


@csrf_exempt
def index(request):
    FinishPerDay.prepare_sessions(request)
    # POST method
    if request.method == "POST":
        template_name, template_params = FinishPerDay.index_post_logic(request)
        if template_name != None:
            return render(request, template_name, template_params)
    # GET method
    max_number = get_max_number()
    template_name, template_params = FinishPerDay.index_get_logic(request, max_number)
    if template_name != None:
        return render(request, template_name, template_params)


def server_time_view(request):
    return HttpResponse(datetime.now().strftime("%H:%M:%S"))
