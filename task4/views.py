from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'fourth_task/menu.html', {'pagename': 'Главная страница'})


def shop(request):
    items = {'games': ['Cyperpunk 2077', 'Crysis', 'Crysis 2', 'Crysis 3', 'The Eler Scrolls V: Skyrim',
                       'The Elder Scrolls IV: Oblivion', 'Atomic Heart']}
    return render(request, 'fourth_task/shop.html', {'pagename': 'Магазин', 'games': items['games']})


def cart(request):
    return render(request, 'fourth_task/cart.html', {'pagename': 'Корзина'})
