from django.shortcuts import render

# Create your views here.
def payment_process(request):
    return render(request, 'payments/payment_process.html')

# from django.http import HttpResponse

# def payment_process(request):
#     # Logique de traitement de paiement
#     return HttpResponse("Traitement du paiement")
