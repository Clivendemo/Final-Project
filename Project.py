import pandas as pd

# Load the data
df = pd.read_csv('country_wise.csv')

# View structure
print(df.columns)
print(df.head())

# Check missing values
print(df.isnull().sum())

# Convert 'date' to datetime

df['date'] = pd.to_datetime(df['date'])

# Filter for countries
countries = ['Kenya', 'USA', 'India']
df_countries = df[df['location'].isin(countries)]

# Drop rows with missing total_cases or total_deaths
df_countries = df_countries.dropna(subset=['total_cases', 'total_deaths'])

# Optionally fill missing values
df_countries = df_countries.fillna(0)

import matplotlib.pyplot as plt

# Plot total cases over time
for country in countries:
    country_data = df_countries[df_countries['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.show()

for country in countries:
    country_data = df_countries[df_countries['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.show()

