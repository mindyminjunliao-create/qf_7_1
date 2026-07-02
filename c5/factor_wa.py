q = query(valuation.code, valuation.pe_ratio, valuation.pcf_ratio, valuation.turnover_ratio)\
        .filter(valuation.pe_ratio < 20, valuation.pe_ratio > 0, valuation.pcf_ratio > 0, valuation.pcf_ratio < 20, valuation.turnover_ratio > 4).order_by(valuation.turnover_ratio.desc())

portfolio = get_fundamentals(q, date = '2020-04-03')
portfolio.head(30)

