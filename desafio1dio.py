import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avengers.csv")

df.head()

df.shape

df.columns

df.dtypes

df.tail()

df.describe()

df.groupby("Gender")["Name/Alias"].nunique()

df.groupby("Year")["Name/Alias"].nunique()

df.groupby("Death1")["Name/Alias"].nunique()

df.groupby("Death2")["Name/Alias"].nunique()

df.groupby("Death3")["Name/Alias"].nunique()

df.groupby("Death4")["Name/Alias"].unique()

df.groupby("Return1")["Name/Alias"].nunique()

df.groupby("Return2")["Name/Alias"].nunique()

df.groupby("Return3")["Name/Alias"].unique()

df.groupby("Return4")["Name/Alias"].nunique()

df.groupby("Gender")["Name/Alias"].nunique().plot.bar()

df.groupby("Appearances")["Name/Alias"].unique()

df.groupby("Year")["Name/Alias"].nunique().plot.bar(title="número de primeiras aparições por ano")

somaAppearances = df.groupby("Gender")["Appearances"].sum().plot.bar(title="Número de aparições por gênero")
somaAppearances

origens_2013 = df.groupby(["Year"]).get_group(1900)["Name/Alias"].unique()
origens_2013

df["Appearances"].describe()

plt.boxplot(df["Appearances"])