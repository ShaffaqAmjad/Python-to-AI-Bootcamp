
# Day 2 - Pandas Practice

import pandas as pd

print("Welcome to Pandas Practice!")

# Load the Titanic dataset
df = pd.read_csv("Day 2/titanic.csv")

# Explore the dataset
print("\nFirst five rows:")
print(df.head())

print("\nLast ten rows:")
print(df.tail(10))

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nDataset information:")
df.info()

print("\nStatistical description:")
print(df.describe())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Select columns
print("\nName, Sex and Age:")
print(df.loc[:, ["Name", "Sex", "Age"]].head())

# Female passengers
female_passengers = df.loc[
    df["Sex"] == "female",
    ["Name", "Age", "Survived"]
]
print("\nFemale passengers:")
print(female_passengers.head(10))

# Male passengers
male_passengers = df.loc[
    df["Sex"] == "male",
    ["Name", "Age", "Survived"]
]
print("\nMale passengers:")
print(male_passengers.head(10))

# Select specific rows and columns
print("\nSelected rows and columns:")
print(df.iloc[5:19, 0:6])

# Survival counts
print("\nSurvival counts:")
print(df["Survived"].value_counts())

# Survival percentages
print("\nSurvival percentages:")
print(df["Survived"].value_counts(normalize=True) * 100)
