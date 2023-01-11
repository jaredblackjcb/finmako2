from django import forms
from . import models

class AnnuityCalculator(forms.Form):
    payment = forms.FloatField(label="Payment", help_text="Amount of money received per period")
    interest_rate = forms.FloatField(label="Interest Rate", help_text="Interest Rate per period")
    periods = forms.IntegerField(label="Periods", help_text='Number of periods')

class PmiCalculator(forms.Form):
    purchase_price = forms.FloatField(label="Purchase Price", help_text="Purchase price of your home")
    down_payment = forms.FloatField(label="Down Payment %")
    interest_rate = forms.FloatField(label="Interest Rate %", help_text="Mortage rate on your loan")
    loan_term = forms.IntegerField(label="Loan Term (Years)")
    monthly_pmi_payment = forms.FloatField(label="Monthly PMI Payment", help_text="Monthly cost of private mortgage insurance")
    opportunity_cost_roi = forms.FloatField(label="Market Return %", help_text="Estimated investment returns you could get in the market")