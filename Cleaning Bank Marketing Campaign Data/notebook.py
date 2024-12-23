# ## Solution:

# %%
import pandas as pd
import numpy as np

data = pd.read_csv("bank_marketing.csv")
data
#data.info()

# %% [markdown]
# #### `client.csv`

# %%
data = pd.read_csv("bank_marketing.csv")

# job
data["job"] = data["job"].str.replace(".", "_")

# education
data["education"] = data["education"].str.replace(".", "_")
data.loc[data["education"] == "unknown", "education"] = np.NaN

# credit_default 
#set(list(data["credit_default"]))
data["credit_default"] = data["credit_default"].map({"no": False,
                                                     "unknown": np.NaN,
                                                     "yes": True})

# mortgage
#set(list(data["mortgage"]))
data["mortgage"] = data["mortgage"].map({"no": False,
                                         "unknown": np.NaN,
                                         "yes": True})


client = data[["client_id", "age", "job", "marital",
               "education", "credit_default", "mortgage"]]

client.to_csv("clients.csv", index = False)

# %% [markdown]
# #### `campaign.csv`

# %%
data = pd.read_csv("bank_marketing.csv")

# previous_outcome
#set(list(data["previous_outcome"]))
data["previous_outcome"] = data["previous_outcome"].map({"failure": False,
                                                         "nonexistent": np.NaN,
                                                         "success": True})

# campaign_outcome
#set(list(data["campaign_outcome"]))
data["campaign_outcome"] = data["campaign_outcome"].map({"no": False,
                                                         "yes": True})

# last_contact_date
#set(list(data["month"]))
def MM(month):
    corresponding = {'apr': "04", 'aug': "08",'dec': "12", 'jul': "07",
                     'jun': "06", 'mar': "03", 'may': "05", 'nov': "11",
                     'oct': "08", 'sep': "09"}
    return corresponding[month]
data["last_contact_date"] =  "2022-" + data["month"].apply(MM) + "-" + data["day"].astype(str)


campaign = data[["client_id", "number_contacts", "contact_duration",
                 "previous_campaign_contacts", "previous_outcome",
                 "campaign_outcome", "last_contact_date"]]

campaign.to_csv("campaign.csv", index = False)

# %% [markdown]
# #### `economics.csv`

# %%
economics = data[["client_id", "cons_price_idx",
                  "euribor_three_months",]]

economics.to_csv("economics.csv", index = False)

# %% [markdown]
# ## Results:

# %%
pd.read_csv("clients.csv")

# %%
pd.read_csv("campaign.csv")

# %%
pd.read_csv("economics.csv")


