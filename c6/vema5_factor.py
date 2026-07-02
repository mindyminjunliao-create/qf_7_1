from jqfactor import get_factor_values
from jqfactor import analyze_factor
import datetime
portfolio = ['600519.XSHG', '600926.XSHG', '600015.XSHG', '601166.XSHG', '600061.XSHG', '601169.XSHG', '601288.XSHG', '600674.XSHG', '601919.XSHG']

today = datetime.date.today()
end_date = '%s-%s-%s'%(today.year, today.month, today.day)
start_date = today - datetime.timedelta(days = 500)
print(start_date, end_date)

factor_vema5 = get_factor_values(securities = portfolio, factors = ['VEMA5'], start_date = start_date, end_date = end_date)['VEMA5']

far = analyze_factor(factor=factor_vema5, start_date=start_date, end_date = end_date, weight_method='mktcap', universe = portfolio, quantiles=5, periods=(1,5,10))
far.mean_return_std_by_quantile

far.create_full_tear_sheet(demeaned=False, group_adjust=False, by_group=False, turnover_periods=None, avgretplot=(5, 15), std_bar=False)
