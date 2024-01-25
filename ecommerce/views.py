from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This functionrender index page of ecommerce view'''

    return HttpResponse('welcome to 6410742693 Yongyut Pornpongsawadi view!')

def item_view(request, item_id) :
    context_data = {
        "item_id": item_id
    }

    return render(request, 'index.html',context = context_data)

def ecommerce_homepage_view(request):

    return render(request, 'homepage.html')

def ecommerce_categorypage_view(request):

    return render(request, 'categorypage.html')

def ecommerce_productpage_view(request):

    return render(request, 'productpage.html')

def ecommerce_checkoutpage_view(request):

    return render(request, 'checkoutpage.html')

def ecommerce_contactpage_view(request):

    return render(request, 'contactpage.html')