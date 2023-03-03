import pandas as pd
import csv

df = pd.read_excel('C:/Users/melissa.goodhew/Marketing Spire Lux Combined Format All Sources.xlsx')
print(df.head())

for col in df.columns:
    print(col, ':', len(df[col].unique()), 'labels')
    
grouped_df = df.groupby(['name'])['speed'].mean().sort_values(ascending=False).head(20)
print(grouped_df)
