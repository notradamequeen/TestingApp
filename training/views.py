from django.http import HttpResponse
from django.template import loader

from .models import Airline

# Here is my first view.
def index(request):
	airline_list = Airline.objects.all()
	template = loader.get_template('training/index.html')
	context = {
	    'airline_list': airline_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, airline_id):
    response = "here is the result of airline %s."
    return HttpResponse(response % airline_id)