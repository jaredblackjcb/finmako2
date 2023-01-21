import pandas as pd

class PmiCalculator():
    def __init__(self, purchase_price, down_payment_percent, annual_interest_rate, loan_term, monthly_pmi_payment, opportunity_cost_roi):
        self.purchase_price = purchase_price
        self.down_payment_percent = down_payment_percent
        self.annual_interest_rate = annual_interest_rate
        self.loan_term = loan_term
        self.monthly_pmi_payment = monthly_pmi_payment
        self.opportunity_cost_roi = opportunity_cost_roi
        self.total_mortgage = self.__calculate_mortgage(purchase_price, down_payment_percent)
        self.pmt_periods = self.__calculate_pmt_periods(loan_term)
        self.monthly_rate = self.__calculate_monthly_rate(annual_interest_rate)

    def __calculate_mortgage(self, purchase_price, down_payment_percent):
        return purchase_price - purchase_price * down_payment_percent

    def __calculate_monthly_rate(self, annual_interest_rate):
        return annual_interest_rate / 12

    def __calculate_pmt_periods(self, loan_term):
        return loan_term * 12

    def calculate_monthly_mortgage_payment(self):
        return self.total_mortgage / ((((1 + self.monthly_rate) ** self.pmt_periods) - 1) / (self.monthly_rate * (1 + self.monthly_rate) ** self.pmt_periods))

    def calculate_total_interest_paid(self):
        return self.calculate_monthly_mortgage_payment() * self.pmt_periods - self.total_mortgage
    
    def calculate_amortization_amount(principal, annual_interest_rate, period):
        x = (1 + annual_interest_rate) ** period
        return principal * (annual_interest_rate * x) / (x - 1)
    
    def get_effective_annual_interest_rate(self, amount_to_cancel_pmi):
        # Define the effective interest rate you are paying
        # Mortgage rate + additional cost of borrowing the amount it would take to cancel PMI
        effective_annual_interest_rate = self.monthly_pmi_payment / amount_to_cancel_pmi * 12 + self.annual_interest_rate
        return effective_annual_interest_rate

    def get_optimal_paydown_period(self):
        # Compare the effective interest rate to the opportunity_cost_roi
        total_principal_paid = 0
        loan_amount = self.total_mortgage
        monthly_mortgage_pmt = self.calculate_monthly_mortgage_payment()
        data = {'month':[], 'principal_paid':[], 'interest_paid':[], 'loan_amount':[], 'amount_to_cancel_pmi':[], 'effective_annual_borrowing_cost_pmi':[]}
        for i in range(self.pmt_periods):
            principal_paydown = monthly_mortgage_pmt - self.monthly_rate * loan_amount
            total_principal_paid += principal_paydown
            interest_paid = monthly_mortgage_pmt - principal_paydown
            amount_to_cancel_pmi = self.purchase_price * (0.2 - self.down_payment_percent) - total_principal_paid
            effective_annual_borrowing_cost_pmi = self.get_effective_annual_interest_rate(amount_to_cancel_pmi)
            loan_amount -= principal_paydown
            
            data['month'].append(f"{(i + 1):.0f}")
            data['principal_paid'].append(f"${principal_paydown:,.2f}")
            data['interest_paid'].append(f"${interest_paid:,.2f}")
            data['loan_amount'].append(f"${loan_amount:,.2f}")
            data['amount_to_cancel_pmi'].append(f"${amount_to_cancel_pmi:,.2f}")
            data['effective_annual_borrowing_cost_pmi'].append(f"{(effective_annual_borrowing_cost_pmi * 100):,.2f}%")

            # Find the period in which effective interest rate > the opportunity_cost_roi
            if effective_annual_borrowing_cost_pmi > self.opportunity_cost_roi:
                print(f"monthly_pmt: {self.calculate_monthly_mortgage_payment()}")
                return pd.DataFrame(data)