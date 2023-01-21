from backtest_controller import BacktestController
from strategies import DollarCostAverage

if __name__ == '__main__':
    backtest_controller = BacktestController(ticker='spxl', start_date='2020-01-01', end_date='2022-10-31', strategy=DollarCostAverage, monthly_cash=500.0)
    results = backtest_controller.run(plot=True)
    print(results['order_logs_df'])