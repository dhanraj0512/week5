import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

# --- 1. Initial Data Inspection ---
print("Original DataFrame info:")
df.info()

print("\nMissing values per column:")
print(df.isnull().sum())

# --- 2. Visualize Missing Data ---
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()

# --- 3. Handle Missing Values ---
# For numerical columns like 'age', filling with the median is a good strategy
# as it's robust to outliers.
age_median = df['age'].median()
df['age'].fillna(age_median, inplace=True)
print(f"\nFilled 'age' NaNs with median value: {age_median}")

# For categorical columns, filling with the mode (most frequent value) is common.
embark_town_mode = df['embark_town'].mode()[0]
embarked_mode = df['embarked'].mode()[0]
df['embark_town'].fillna(embark_town_mode, inplace=True)
df['embarked'].fillna(embarked_mode, inplace=True)
print(f"Filled 'embark_town' NaNs with mode value: {embark_town_mode}")

# The 'deck' column has too many missing values to be useful. It's best to drop it.
df.drop('deck', axis=1, inplace=True)
print("Dropped the 'deck' column.")

# --- 4. Verification ---
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned DataFrame info:")
df.info()