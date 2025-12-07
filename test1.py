import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
print("Original DataFrame info:")
df.info()

print("\nMissing values per column:")
print(df.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()


age_median = df['age'].median()
df['age'].fillna(age_median, inplace=True)
print(f"\nFilled 'age' NaNs with median value: {age_median}")

embark_town_mode = df['embark_town'].mode()[0]
embarked_mode = df['embarked'].mode()[0]
df['embark_town'].fillna(embark_town_mode, inplace=True)
df['embarked'].fillna(embarked_mode, inplace=True)
print(f"Filled 'embark_town' NaNs with mode value: {embark_town_mode}")

df.drop('deck', axis=1, inplace=True)
print("Dropped the 'deck' column.")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned DataFrame info:")
df.info()