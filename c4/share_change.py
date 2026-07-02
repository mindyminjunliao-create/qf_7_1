q = query(finance.STK_SHAREHOLDERS_SHARE_CHANGE.code,\
        finance.STK_SHAREHOLDERS_SHARE_CHANGE.pub_date,\
        finance.STK_SHAREHOLDERS_SHARE_CHANGE.shareholder_name,\
        finance.STK_SHAREHOLDERS_SHARE_CHANGE.type,\
        finance.STK_SHAREHOLDERS_SHARE_CHANGE.change_number,\
        finance.STK_SHAREHOLDERS_SHARE_CHANGE.change_ratio, \
        finance.STK_SHAREHOLDERS_SHARE_CHANGE.after_chage_ratio)\
        .filter(finance.STK_SHAREHOLDERS_SHARE_CHANGE.code == '002458.XSHE', finance.STK_SHAREHOLDERS_SHARE_CHANGE.pub_date > '2019-09-01')

shrchg = finance.run_query(q)
shrchg
