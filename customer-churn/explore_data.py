import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('./data/Churn_Modelling.csv')
except FileNotFoundError:
    df = pd.read_csv('./customer-churn/data/Churn_Modelling.csv')

print(df.head())
print(80*'-')
print(df.describe())
print(80*'-')
print(dir(pd.DataFrame))

