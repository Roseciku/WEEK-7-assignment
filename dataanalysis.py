

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#TASK 1
#Loading dataset
file_path = 'Student Depression Dataset.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())

# Check the data types and for any missing values
print(df.info())

# Drop rows with any missing values
df.dropna(inplace=True)

#TASK 2
# Compute basic statistics
basic_stats = df.describe()
print(basic_stats)

#Grouping on a categorical column
gender_group = df.groupby('Gender')['Depression'].mean()
print(gender_group)

#TASK 3
#Line Chart 
age_grouped = df.groupby('Age')['Depression'].mean().reset_index() #used beacuse we have a large dataset
plt.figure(figsize=(10,5))
plt.plot(age_grouped['Age'], age_grouped['Depression'], marker='o')
plt.title('Age vs.Depression')
plt.xlabel('Age')
plt.ylabel('Depression')
plt.grid(True)
plt.show()

#Bar Chart
plt.figure(figsize=(10,6))
df.groupby('Gender')['Depression'].mean().plot(kind='bar', color='green')
plt.title('Average Depression Score by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Depression Score')
plt.show()

#Histogram
plt.figure(figsize=(10, 5))
plt.hist(df['Academic Pressure'], bins=5, edgecolor='black')
plt.title('Distribution of Academic Pressure Scores')
plt.xlabel('Academic Pressure Scores')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

#Scatter plot
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Age', y='Depression', data=df, alpha=0.5)
plt.title('Age vs. Depression')
plt.xlabel('Age')
plt.ylabel('Depression')
plt.grid(True)
plt.show()