# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("adult.data.csv")
#x = df.columns
#print(x)

race_count = df['race'].value_counts()

average_age_men = df[df['sex']=='Male']['age'].mean().round(1)

bachelors = df[df['education'] == 'Bachelors']
percentage_of_bachelors = round(len(bachelors) / len(df) *100,1)

masters = df[df['education'] == 'Masters']
doctorate = df[df['education'] == 'Doctorate']

higher_education = pd.concat([bachelors, masters, doctorate])
lower_education = df[~df['education'].isin(['Bachelors', 'Masters','Doctorate'])]

higher_education_rich = higher_education[higher_education['salary'] == '>50K']
lower_education_rich = lower_education[lower_education['salary'] == '>50K']

min_work_hours = df['hours-per-week'].min()

min_workers = df[df['hours-per-week'] == min_work_hours]
num_min_workers = len(min_workers)

min_worker_riches = min_workers[min_workers['salary'] == '>50K']
min_worker_rich_percentage = round(len(min_worker_riches) / len(df) * 100, 3)


highest_earning_countries = df[df['salary'] == '>50K']['native-country']
wealth = (highest_earning_countries.value_counts() / df['native-country'].value_counts())*100

highest_earning_country = wealth.idxmax()
highest_earning_country_percentage = round(wealth.max())

people_from_india = df[df['native-country'] == 'India']
riches_of_india = people_from_india[people_from_india['salary'] == '>50K']

top_IN_occupations = riches_of_india['occupation'].value_counts().idxmax()
print(top_IN_occupations)
