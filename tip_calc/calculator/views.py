from django.shortcuts import render
from django.http import HttpResponse

def calculate_tip(request):
    if request.method == 'POST':
        subtotal = float(request.POST.get('subtotal'))
        tip_percentage = float(request.POST.get('tip_percentage'))
        tip_amount = subtotal * (tip_percentage / 100)
        total = subtotal + tip_amount
        return render(request, 'result.html', {'total': total})
    else:
        return render(request, 'index.html')
