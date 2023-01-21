import * as echarts from 'echarts';

// Create number formatter.
const formatter = new Intl.NumberFormat('en-US', {
  style: 'currency',
  currency: 'USD',

  // These options are needed to round to whole numbers
  minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
  maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
});

// Populate a chart displaying portfolioValue and totalInvested
waitForElement('#chart-container').then(() => {
  // initialize the echarts instance
  const portfolioValue = JSON.parse(document.getElementById('portfolio_values').textContent);
  const totalInvested = JSON.parse(document.getElementById('investment_totals').textContent);
  const tradeDates = JSON.parse(document.getElementById('trade_dates').textContent);
  
  // Draw the chart
  // Echarts docs: https://echarts.apache.org/en/option.html#title
  let chartContainer = document.getElementById('chart-container');
  chartContainer.style.minHeight = "400px";
  const myChart = echarts.init(chartContainer);
  myChart.setOption({
    title: {
      text: 'Investment Performance'
    },
    tooltip: {
      trigger: 'axis',
      valueFormatter: (value) => formatter.format(value)
    },
    legend: {
      data: ['Portfolio Value', 'Total Invested']
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    toolbox: {
      feature: {
        saveAsImage: {},
        dataZoom: {}
      }
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: tradeDates
    },
    yAxis: {
      type: 'value',
      name: '$USD',
      nameLocation: 'center',
      nameTextStyle: {
        fontWeight: 'bold',
        fontSize: 14
      }
    },
    series: [
      {
        name: 'Portfolio Value',
        type: 'line',
        data: portfolioValue
      },
      {
        name: 'Total Invested',
        type: 'line',
        data: totalInvested
      }
    ]
  });
});

function waitForElement(selector) {
  return new Promise(resolve => {
      if (document.querySelector(selector)) {
          return resolve(document.querySelector(selector));
      }
      
      const observer = new MutationObserver(mutations => {
          if (document.querySelector(selector)) {
              resolve(document.querySelector(selector));
              observer.disconnect();
          }
      });
      
      observer.observe(document.body, {
          childList: true,
          subtree: true
      });
  });
}