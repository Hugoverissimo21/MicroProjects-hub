# %% [markdown]
# ## Solution:

# %%
import numpy as np
import pandas as pd
import seaborn as sns

# %%
balance_sheet = pd.read_excel("Balance_Sheet.xlsx")
balance_sheet.sample(5)

# %%
income_sheet = pd.read_excel("Income_Statement.xlsx")
income_sheet.sample(5)

# %%
df_ratios = pd.DataFrame()

# debt-to-equity ratio
df_ratios["leverage_ratio"] = balance_sheet["Total Liab"]/balance_sheet["Total Stockholder Equity"]

# gross margin ratio
df_ratios["profitability_ratio"] = (income_sheet["Total Revenue"] - income_sheet["Cost Of Goods Sold"])/income_sheet["Total Revenue"]

df_ratios.head(5)

# %%
df_ratios1 = pd.concat([df_ratios, income_sheet["comp_type"]], axis=1)
df_ratios_comp_type = df_ratios1.groupby(by=["comp_type"]).mean()

# lowest_profitability
lowest_profitability = df_ratios_comp_type["profitability_ratio"].idxmin()

# highest_leverage
highest_leverage = df_ratios_comp_type["leverage_ratio"].idxmax()

print([lowest_profitability, highest_leverage])

# %%
# relationship between leverage and profitability in real_est
df_ratios_real_est = df_ratios1.loc[df_ratios1["comp_type"] == "real_est"]
df_ratios_real_est
sns.regplot(x = "leverage_ratio", y = "profitability_ratio", data = df_ratios_real_est)
relationship = "positive"

# %%



