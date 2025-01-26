from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    items = {
        'Cyperpunk 2077'                    : 'Купить',
        'Crysis'                            : 'Купить',
        'Crysis 2'                          : 'Купить',
        'Crysis 3'                          : 'Купить',
        'The Eler Scrolls V: Skyrim'        : 'Купить',
        'The Elder Scrolls IV: Oblivion'    : 'Купить',
        'Atomic Heart'                      : 'Купить',
    }
    return render(request, 'third_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')
