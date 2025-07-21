from django.http import HttpResponse

# Create your views here.
def print_hello(request):
    return HttpResponse("Hello, Ayoob")

print_hello