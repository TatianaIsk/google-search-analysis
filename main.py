import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()

#%%
trends.build_payload(kw_list=["Machine Learning"])
data = trends.interest_by_region()
data = data.sort_values(by="Machine Learning", ascending=False)
data = data.head(10)
print(data)
#%%
data.reset_index().plot(x="geoName", y="Machine Learning",
                        figsize=(20, 15), kind="bar")
plt.style.use("fivethirteight")
plt.show()
#%%
data = TrendReq(hl="en-US", tz=360)
data.build_payload(kw_list=["Machine Learning"])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(20, 15))
data["Machine Learning"].plot()
plt.style.use("fivethirteight")
plt.title("Total Google Searches for Machine Learning", fontweight='bolt')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()
#%%
