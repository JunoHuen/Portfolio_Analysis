#%%
import pandas as pd
import tushare as ts

# raw_data1 = pd.read_csv("Data\\Investment-Portfolio-Analysis-Data.csv", index_col='Date', parse_dates=True)

# print(pd.DataFrame(raw_data1))

fundHolding_df = pd.DataFrame(ts.fund_holdings(2019, 2))
fundHolding_df = fundHolding_df.sort_values(by='count', ascending=0)
# print(fundHolding_df)

# film_preDay_df = pd.DataFrame(ts.day_boxoffice())

#%%
