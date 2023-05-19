import pandas as pd
import seaborn as sns

data = pd.read_csv("output/input.csv.gz")

# just a placeholder to test out a bit of cleaning
clean_data = data[~data.isnull().any(axis=1)]
clean_data.to_csv('output/clean_data.csv', index=False)

fig_1 = sns.distplot(data.age, kde=True).get_figure()
fig_1.savefig("output/seaborn_hist.png")

fig_2 = data.age.plot.hist().get_figure()
fig_2.savefig("output/pandas_hist.png")
