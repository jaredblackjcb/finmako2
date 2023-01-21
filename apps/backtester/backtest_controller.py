import backtrader as bt
from .twelvedata_requests import request_daily_time_series




class BacktestController():
    def __init__(self, ticker, start_date, end_date, strategy, monthly_cash):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.strategy = strategy
        self.monthly_cash = monthly_cash

    # Run the strategy
    def run(self, plot=False):
        # Create a cerebro entity
        cerebro = bt.Cerebro(stdstats=False)

        # Get data from Twelve Data
        stock_df = request_daily_time_series(start_date=self.start_date, end_date=self.end_date, symbol=self.ticker)

        # Create a backtrader PandasData feed and add it to the cerebro instance
        data = bt.feeds.PandasData(dataname=stock_df)
        cerebro.adddata(data)

        # Add a strategy and set monthly_cash
        cerebro.addstrategy(self.strategy, self.monthly_cash)

        # Broker Information
        broker_args = dict(coc=True)
        cerebro.broker = bt.brokers.BackBroker(**broker_args)

        # Run cerebro
        result = cerebro.run()
        amount_invested = f"{result[0].amount_invested:,.2f}"
        shares_purchased = f"{result[0].shares_purchased:,.2f}"
        order_logs = result[0].order_logs
        order_logs_df = result[0].order_logs_df
        end_close_price = result[0].end_close_price
        end_portfolio_value = f"{result[0].end_portfolio_value:,.2f}"
        trade_start_date = result[0].trade_start_date
        end_date = result[0].end_date
        years_in_market = f"{result[0].years_in_market:,.2f}"
        total_percent_return = f"{result[0].total_percent_return:,.2f}"
        total_dollar_return = f"{result[0].total_dollar_return:,.2f}"
        annualized_return = f"{result[0].annualized_return:,.2f}"
        trade_dates = result[0].trade_dates
        investment_totals = result[0].investment_totals
        portfolio_values = result[0].portfolio_values
        if plot:
            cerebro.plot()

        return {'stock_df':stock_df
                    ,'amount_invested':amount_invested
                    ,'shares_purchased':shares_purchased
                    ,'order_logs':order_logs
                    ,'order_logs_df':order_logs_df
                    ,'end_close_price':end_close_price
                    ,'end_portfolio_value':end_portfolio_value
                    ,'trade_start_date':trade_start_date
                    ,'end_date':end_date
                    ,'years_in_market':years_in_market
                    ,'total_percent_return':total_percent_return
                    ,'total_dollar_return':total_dollar_return
                    ,'annualized_return':annualized_return
                    ,'trade_dates':trade_dates
                    ,'investment_totals':investment_totals
                    ,'portfolio_values':portfolio_values}