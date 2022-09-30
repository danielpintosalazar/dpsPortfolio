from django.shortcuts import render, redirect
from django.views.generic import View
from applications.openpay_integration.utils import *


class CreateChargeView(View):

    def post(self, request, *args, **kwargs):
        customer = find_customer_by_email(request.POST.get('email'))
        return redirect(generate_transaction(request, customer))
    
    def get(self, request, *args, **kwargs):
        return render(request, 'donate.html')