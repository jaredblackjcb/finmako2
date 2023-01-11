from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import datetime
import pandas as pd

# Strategy for 401k
class DollarCostAverage(bt.Strategy):
    params = dict(
        monthly_cash=None,
        month_days=[1, 15],
    )
    
    def __init__(self, *args, **kwargs):
        self.order = None
        self.amount_invested = 0
        self.shares_purchased = 0
        self.p.monthly_cash = args[0]
        self.trade_dates = []
        self.investment_totals = []
        self.portfolio_values = []
        self.order_logs = []
        self.order_logs_df = pd.DataFrame(columns=['datetime', 'action', 'purchase_price', 'shares_purchased', 'amount_invested', 'portfolio_value'])
        self.end_close_price = 0
        self.end_portfolio_value = 0
        self.trade_start_date = None
        self.end_date = None
        self.years_in_market = 0
        self.total_percent_return = 0
        self.total_dollar_return = 0
        self.annualized_return = 0
        


    def log(self, txt, datetime=None):
        datetime = datetime or self.datas[0].datetime.date()
        self.order_logs.append(f"{datetime.isoformat()} - {txt}")
        print(f"{datetime.isoformat()} - {txt}")

    def start(self):
        print(f"Monthly Cash: ${self.p.monthly_cash:,.2f}")
        self.broker.set_fundmode(fundmode=True, fundstartval=100.0)
        self.broker.setcash(0.01)
        self.cash_start = self.broker.get_cash()
        self.fund_start_value = 100.0
        # Timer to trigger actions on closest trading day to dates in month_days
        self.add_timer(
            when= bt.timer.SESSION_START,
            monthdays=[i for i in self.p.month_days],
            monthcarry=True,
        )

    # Takes place of next_start method, notify_timer contains logic to be triggered when the timer goes off
    def notify_timer(self, timer, when, *args):
        # Deposit money into the brokerage account
        cash_deposit = (self.p.monthly_cash / len(self.p.month_days)) * 10**6
        self.broker.add_cash(cash_deposit)
        target_purchase = self.broker.get_value() + cash_deposit
        self.order_target_value(target=target_purchase)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        
        if order.status in [order.Completed]:
            trade_date = self.datas[0].datetime.date()
            self.trade_dates.append(trade_date)
            if order.isbuy():
                shares_purchased = float(order.executed.size)/10**6
                amount_invested = order.executed.value/10**6
                # Add number of shares and the total cost to the running totals
                self.log(
                    f"BUY EXECUTED, Price per Share ${order.executed.price:,.2f}, Shares Purchased {shares_purchased:,.2f}, Total Cost ${amount_invested:,.2f}, Commission ${order.executed.comm:.2f}"
                )
                self.shares_purchased += float(order.executed.size)/10**6
                self.amount_invested += order.executed.value/10**6
                portfolio_value = self.datas[0].close * self.shares_purchased + self.broker.get_cash() / 10**6
                print(f"PORTFOLIO VALUE: ${portfolio_value:,.2f}, TOTAL SHARES: {self.shares_purchased:,.2f}, CLOSE PRICE: {self.datas[0].close[0]}")
                df = pd.DataFrame({'datetime':[trade_date] , 'action':['BUY EXECUTED'], 'purchase_price':[f"${order.executed.price:,.2f}"], 'shares_purchased':[f"{shares_purchased:,.2f}"], 'amount_invested':[f"${self.amount_invested:,.2f}"], 'portfolio_value':[f"${portfolio_value:,.2f}"]})
                self.order_logs_df = pd.concat([self.order_logs_df, df], axis=0)
                self.investment_totals.append(self.amount_invested)
                self.portfolio_values.append(portfolio_value)
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
            print(order.status, [order.Canceled, order.Margin, order.Rejected])

        self.order = None

    def stop(self):
        self.fund_roi = (self.broker.get_fundvalue() - self.fund_start_value) - 1
        self.end_close_price = self.datas[0].close.array[-1]
        self.end_portfolio_value = self.end_close_price * self.shares_purchased + self.broker.get_cash() / 10**6 # last closing price * units held + ending cash
        self.trade_start_date = self.trade_dates[0]
        self.end_date = self.datas[0].datetime.date()
        self.years_in_market = (self.end_date - self.trade_start_date).days/365
        self.total_percent_return = (self.end_portfolio_value / self.amount_invested - 1) * 100
        self.total_dollar_return = self.end_portfolio_value - self.amount_invested
        self.annualized_return = 100 * ((1 + self.total_percent_return/100)**(365/(self.end_date - self.trade_start_date).days) - 1)
        print('-'*50)
        print('DOLLAR COST AVERAGE')
        print(f"Years in Market: {self.years_in_market:.1f} years")
        print(f"Shares Purchased: {self.shares_purchased:,.2f}")
        print(f"Final Closing Price: ${self.end_close_price:,.2f}")
        print(f"Portfolio Value: ${self.end_portfolio_value:,.2f}")
        print(f"Total Invested: ${self.amount_invested:,.2f}")
        print(f"Total Return: ${self.total_dollar_return:,.2f}")
        print(f"Total % Return: {self.total_percent_return:.2f}%")
        # print(f"Fund ROI: {self.fund_roi:.2f}%")
        print(f"Annualized Return: {self.annualized_return:.2f}%")
        print('-'*50)

        #TODO: Return dataframe with logs and dictionary with metrics




