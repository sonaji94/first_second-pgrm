from django.shortcuts import render

def hello_world(request):
    context = {'message': 'Hello World'}
    return render(request, 'hello_app/hello.html', context)
