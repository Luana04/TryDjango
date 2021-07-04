from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 456, 789, 'abc']
    }
    return render(request, "home.html", my_context)

