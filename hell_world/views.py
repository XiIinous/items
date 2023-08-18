from django.shortcuts import render

# Create your views here.
def hell_world(request):
    return render(request, 'hell_world.html', {})