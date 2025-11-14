# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:53:15 2024

@author: phani
"""

import pandas as pd
import seaborn as sns
file_path = "C:/Users/phani/Desktop/AIT 580/Crime_Incidents_in_2024.csv"
crime_data = pd.read_csv(file_path)

missing_summary = crime_data.isnull().sum()
print("Missing values in each column:\n", missing_summary)


threshold = 0.9 * len(crime_data)
columns_to_drop = missing_summary[missing_summary > threshold].index
crime_data = crime_data.drop(columns=columns_to_drop)
print(f"Dropped columns with >90% missing values: {list(columns_to_drop)}")


crime_data['DISTRICT'] = crime_data['DISTRICT'].fillna(crime_data['DISTRICT'].median())
crime_data['WARD'] = crime_data['WARD'].fillna(crime_data['WARD'].median())

categorical_columns = ['ANC', 'NEIGHBORHOOD_CLUSTER', 'VOTING_PRECINCT']
for col in categorical_columns:
    if col in crime_data:
        crime_data[col] = crime_data[col].fillna(crime_data[col].mode()[0])


crime_data = crime_data.dropna(subset=['START_DATE', 'END_DATE'])

print("\nAfter handling missing values:")
print(crime_data.isnull().sum())

date_columns = ["REPORT_DAT", "START_DATE", "END_DATE"]
for col in date_columns:
    crime_data[col] = pd.to_datetime(crime_data[col], errors='coerce')
    
crime_data['RESPONSE_TIME_SECONDS'] = (crime_data['END_DATE'] - crime_data['START_DATE']).dt.total_seconds() / 60

cleaned_data = crime_data.dropna(subset=['RESPONSE_TIME_SECONDS', 'DISTRICT', 'WARD'])

overall_avg_response_time = cleaned_data['RESPONSE_TIME_SECONDS'].mean()

avg_response_by_district = cleaned_data.groupby('DISTRICT')['RESPONSE_TIME_SECONDS'].mean()

avg_response_by_ward = cleaned_data.groupby('WARD')['RESPONSE_TIME_SECONDS'].mean()

print(f"Overall Average Response Time: {overall_avg_response_time:.2f} seconds\n")
print("Average Response Time by District:")
print(avg_response_by_district)
print("\nAverage Response Time by Ward:")
print(avg_response_by_ward)


import matplotlib.pyplot as plt

avg_response_by_district.plot(kind='bar', color='dodgerblue', figsize=(10, 5))
plt.title('Average Response Time by District')
plt.xlabel('District')
plt.ylabel('Response Time (seconds)')
plt.show()

avg_response_by_ward.plot(kind='bar', color='lightseagreen', figsize=(10, 5))
plt.title('Average Response Time by Ward')
plt.xlabel('Ward')
plt.ylabel('Response Time (seconds)')
plt.show()




offense_counts = crime_data['OFFENSE'].value_counts()
offense_counts.plot(kind='bar', color='brown', figsize=(10, 6))
plt.title('Distribution of Offense Types')
plt.xlabel('Offense Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

ward_counts = crime_data['WARD'].value_counts().sort_index()
ward_counts.plot(kind='bar', color='tomato', figsize=(8, 5))
plt.title('Crime Count by Ward')
plt.xlabel('Ward')
plt.ylabel('Crime Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

crime_data['REPORT_DAT'] = pd.to_datetime(crime_data['REPORT_DAT'])
crime_data['Month'] = crime_data['REPORT_DAT'].dt.to_period('M')
monthly_crime_counts = crime_data['Month'].value_counts().sort_index()

monthly_crime_counts.plot(kind='line', figsize=(12, 6), color='darkorange')
plt.title('Monthly Crime Trends')
plt.xlabel('Month')
plt.ylabel('Crime Count')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(crime_data['RESPONSE_TIME_SECONDS'], kde=True, color='maroon', bins=30)
plt.title('Distribution of Response Times')
plt.xlabel('Response Time (Minutes)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

ward_offense_counts = crime_data.groupby(['WARD', 'OFFENSE']).size().unstack(fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(ward_offense_counts, annot=True, fmt='d', cmap='coolwarm', cbar=True)
plt.title('Heatmap of Offenses Across Wards')
plt.xlabel('Offense Type')
plt.ylabel('Ward')
plt.tight_layout()
plt.show()

ward_method_counts = crime_data.groupby(['WARD', 'METHOD']).size().reset_index(name='Count')
plt.figure(figsize=(12, 6))
sns.barplot(data=ward_method_counts, x='WARD', y='Count', hue='METHOD', palette='Set1')
plt.title('Crime Methods Across Wards')
plt.xlabel('Ward')
plt.ylabel('Count')
plt.legend(title='Method')
plt.tight_layout()
plt.show()

offense_time_counts = crime_data.groupby([crime_data['REPORT_DAT'].dt.to_period('M'), 'OFFENSE']).size().unstack(fill_value=0)

offense_time_counts.plot(kind='area', stacked=True, figsize=(12, 6), colormap='plasma')
plt.title('Crime Offense Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Crime Count')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 8))
sns.scatterplot(data=crime_data, x='LONGITUDE', y='LATITUDE', hue='OFFENSE', palette='Set1', alpha=0.7)
plt.title('Crime Locations by Offense Type')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Offense')
plt.tight_layout()
plt.show()

