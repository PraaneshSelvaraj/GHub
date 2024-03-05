from django.shortcuts import render

# Create your views here.
def home_view(request):
    print(request.method)
    return render(request=request, template_name="index.html")

def game_view(request, name):
    print(name)
    return render(request, "game.html")