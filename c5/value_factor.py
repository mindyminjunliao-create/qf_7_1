from jqfactor import get_factor_values
import pandas as pd
indices = get_all_securities(types=['index'])
indices.head(10)

from jqfactor import analyze_factor
factor_mc=get_factor_values(securities=get_index_stocks('000300.XSHG'), factors=['market_cap'], end_date='2020-04-10',count=1)['market_cap']
factor_mc.T.head()

factor_cfp = get_factor_values(securities = get_index_stocks('000300.XSHG'), factors = ['cash_flow_to_price_ratio'], end_date = '2020-04-10', count = 1)['cash_flow_to_price_ratio']
factor_cfp.T.head(5)

factor_npr = get_factor_values(securities = get_index_stocks('000300.XSHG'), factors = ['net_profit_ratio'], end_date = '2020-04-10', count=1)['net_profit_ratio']
factor_npr.T.head()

factor_npgr = get_factor_values(securities = get_index_stocks('000300.XSHG'), factors=['net_profit_growth_rate'], end_date = '2020-04-10', count=1)['net_profit_growth_rate']
factor_npgr.T.head()

factors = pd.DataFrame(index = factor_mc.T.index)
factors['mc'] = factor_mc.T['2020-04-10 00:00:00']
factors['cfp'] = factor_cfp.T['2020-04-10 00:00:00']
factors['npr'] = factor_npr.T['2020-04-10 00:00:00']
factors['npgr'] = factor_npgr.T['2020-04-10 00:00:00']
factors.head()

factors = factors.dropna()
factors.isnull().sum()

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
scaler = StandardScaler()
factors_scl = scaler.fit_transform(factors)
pca = PCA(n_components = 1)
pca.fit(factors_scl)
pca.components_

factors['pca'] = pca.transform(factors_scl)
factors.sort_values(by='pca', ascending = False).head(9)
