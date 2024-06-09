from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from renderers import render_to_pdf

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            'invoice_id': 123, 
            'customer_name': 'Jhon Cooper',
            'amount': 1399.99,
            'today': "today",
        }
        html = template.render(context)
        return HttpResponse(html)