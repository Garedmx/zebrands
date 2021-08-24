
from django.http import HttpResponse, JsonResponse
from motor.models import Product
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt


def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        for product in products:
            num = product.consulted
            num = num + 1
            product.consulted = num
            product.save()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        num = product.consulted
        num = num + 1
        product.consulted = num
        product.save()
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)
