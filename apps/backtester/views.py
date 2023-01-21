from django.shortcuts import render
from django.contrib import messages

from .forms import BacktesterForm
from .backtest_controller import BacktestController
from .strategies import DollarCostAverage

# Create your views here.
def backtester(request):
    form = BacktesterForm(request.POST)
    context_dict = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            # Implement backtrader logic here using form input
            ticker = form.cleaned_data['ticker']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            monthly_investment = form.cleaned_data['monthly_investment']
            backtest_controller = BacktestController(ticker=ticker, start_date=start_date, end_date=end_date, strategy=DollarCostAverage, monthly_cash=monthly_investment)
            try:
                backtest_data = backtest_controller.run()
                print(backtest_data)
                context_dict.update({'backtest_data':backtest_data})
            except:
                messages.error(request, "An error occurred. Please ensure that you have entered a valid ticker symbol and date range.")

        else:
            for key, value in form.errors.items():
                messages.error(request, value)
    return render(request, 'backtester/backtester.html', context=context_dict)