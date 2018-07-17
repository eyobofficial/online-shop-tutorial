from django.shortcuts import render, get_object_or_404

from .models import Product, Catagory


def product_list(request, catagory_slug=None):
    # Update User Site Visit Count
    visit_count = request.session.get('visit_count', 0)
    visit_count += 1
    request.session['visit_count'] = visit_count

    product_list = Product.objects.available()
    catagory_list = Catagory.objects.all()
    catagory = None  # Default value if no slug is argument is passed
    if catagory_slug:
        catagory = get_object_or_404(Catagory, slug=catagory_slug)
        product_list = product_list.filter(catagory=catagory)
    template_name = 'shop/product/product_list.html'
    return render(request, template_name, {
        'catagory_list': catagory_list,
        'catagory': catagory,
        'product_list': product_list,
        'visit_count': visit_count,
    })


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug, available=True)
    catagory_list = Catagory.objects.all()
    template_name = 'shop/product/product_detail.html'
    return render(request, template_name, {
        'catagory_list': catagory_list,
        'product': product,
    })
