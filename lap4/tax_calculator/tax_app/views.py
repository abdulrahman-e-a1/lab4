from django.shortcuts import render

tax_rate = 0.15  

def default_view(request):
    return render(request, 'tax_app/default.html')

def calculate_tax_view(request, number):
    total_price = number + (number * tax_rate)
    context = {'total_price': total_price}
    return render(request, 'tax_app/calculate_tax.html', context)

def tax_rate_view(request):
    context = {'tax_rate': tax_rate}
    return render(request, 'tax_app/tax_rate.html', context)