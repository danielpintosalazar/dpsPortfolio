import json
import openpay
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View

# Configurate the attributes in Openpay package
openpay.api_key = settings.OPENPAY_API_KEY
openpay.merchant_id = settings.OPENPAY_MERCHANT_ID
openpay.production = settings.OPENPAY_PRODUCTION # By default this works in sandbox mode
openpay.verify_ssl_certs = settings.OPENPAY_VERIFY_SSL_CERTS
openpay.country = settings.OPENPAY_COUNTRY  # 'mx' is default value, to use for Colombia set country='co'


def find_customer_by_email(email_customer):
    """ This function searches for the client by the supplied email and if it exists, it returns all its information, otherwise it returns a None value. 

    Args:
        email_customer (string): email sended on the request

    Returns:
        customer_object_openpay: all data of a customer
        None: a empty value
    """
    
    query = json.loads(json.dumps(openpay.Customer.all())) # Convert a query object to a string and then to a dictionary
    for customer in query['data']: # Go through each of the customers
        if customer['email'] == email_customer: # Compare the current customer with the customer you are looking for
            return openpay.Customer.retrieve(str(customer['id'])) # Return the id customer
        else:
            return None # Return None when the costumer don't exists


def create_charge(request, customer):
    """ Create a charge using openpay, and save the information in a variable transaction. Also return the link to pay this charge.

    Args:
        request (Http request): a petition http POST
        customer (customer openpay object): a customer object by openpay

    Returns:
        url_transaction: url to finish the transaction
    """

    try:
        transaction = openpay.Charge.create(
                    method=request.POST.get('method'),
                    amount=int(request.POST.get('amount')),
                    currency=request.POST.get('currency'),
                    iva=1900,
                    description='Donation to Daniel Pinto Salazar',
                    customer=customer['id'],
                    confirm = False,
                    send_email = True,
                    redirect_url='http://127.0.0.1:8000/pay-gateway/donate/'
                )
        transaction = json.loads(json.dumps(transaction))
        url_transaction = transaction["payment_method"]["url"]
        return str(url_transaction)
    except:
        return None


def generate_transaction(request, customer):
    """ If the customer already exists, it assigns the specified charge. Otherwise, it creates the customer first and then the transaction is generated.

    Args:
        request (Http request): a petition http POST
        customer (customer openpay object): a customer object by openpay

    Returns:
        function: returns the function with the payment link, or otherwise generates returns None
    """

    try:
        if customer:
            return create_charge(request, customer)
        else:
            customer= openpay.Customer.create(
                name=request.POST.get('name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email')
            )
            return create_charge(request, customer)
    except:
        return None