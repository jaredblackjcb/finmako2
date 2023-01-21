from django.shortcuts import render
from django import views
from django.views import View
from . import forms
import math
from . import calculators

# Create your views here.
def pmi_calculator(request):
    form = forms.PmiCalculator(request.POST)
    context_dict = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            purchase_price = form.cleaned_data['purchase_price']
            down_payment_percent = form.cleaned_data['down_payment'] / 100
            annual_interest_rate = form.cleaned_data['interest_rate'] / 100
            loan_term = form.cleaned_data['loan_term']
            monthly_pmi_payment = form.cleaned_data['monthly_pmi_payment']
            opportunity_cost_roi = form.cleaned_data['opportunity_cost_roi'] / 100
            pmi_calculator = calculators.PmiCalculator(purchase_price, down_payment_percent, annual_interest_rate, loan_term, monthly_pmi_payment, opportunity_cost_roi)
            pmi_data = pmi_calculator.get_optimal_paydown_period()
            paydown_month = len(pmi_data)
            context_dict.update({'pmi_data': pmi_data, 'paydown_month': paydown_month})
    return render(request, 'calculator/pmi_calculator.html', context=context_dict)

def annuity_calculator(request):
    annuity_calculator_form = forms.AnnuityCalculator(request.POST)
    future_value = 0
    context_dict = {'future_value': future_value, 'annuity_form': annuity_calculator_form}
    if request.method == 'POST':
        if annuity_calculator_form.is_valid():
            payment = annuity_calculator_form.cleaned_data['payment']
            interest_rate = annuity_calculator_form.cleaned_data['interest_rate'] / 100
            periods = annuity_calculator_form.cleaned_data['periods']
            future_value = payment * (((math.pow(1 + interest_rate, float(periods))) - 1) / interest_rate)
            context_dict['future_value'] = f'{future_value:,.2f}'
    return render(request, 'calculator/annuity_calculator.html', context=context_dict)


