from django.http import HttpResponse

# Here is my first view.
def index(request):
	return HttpResponse("This is my first view")
