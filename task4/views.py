from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'fourth_task/menu.html', {'pagename': 'Главная страница'})


def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'Doom Eternal']
    return render(request, 'fourth_task/shop.html', {'pagename': 'Магазин', 'games': games})


def cart(request):
    return render(request, 'fourth_task/cart.html', {'pagename': 'Корзина'})
