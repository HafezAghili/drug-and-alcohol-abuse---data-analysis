import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the size of the dataset
data_size = 100000

# Generate data
countries = ["USA", "Canada", "UK", "Germany", "France", "Spain", "Italy", "Japan", "Australia", "Brazil"]
school_types = ["Public", "Private"]
substances = ["No Use", "Alcohol", "Drugs", "Alcohol and Drugs"]
grades = np.random.randint(0, 101, size=data_size)
family_income = np.random.randint(20000, 100001, size=data_size)
bool_columns = [np.random.choice([0, 1], size=data_size).astype(bool) for _ in range(8)]
criminal_record_values = np.random.choice([True, False], size=data_size, p=[0.9, 0.1])

# Generate unique phone numbers
phone_numbers = set()
while len(phone_numbers) < data_size:
    phone_numbers.add(fake.phone_number())
phone_numbers = list(phone_numbers)

data = {
    "Country": [fake.random_element(countries) for _ in range(data_size)],
    "Phone_Number": phone_numbers,
    "Gender": [fake.random_element(["Male", "Female"]) for _ in range(data_size)],
    "Age": [fake.random_int(min=15, max=18) for _ in range(data_size)],
    "Has_Older_Sibling": bool_columns[0],
    "Has_Younger_Sibling": bool_columns[1],
    "Parents_Together": bool_columns[2],
    "Substance_Abuse": [fake.random_element(substances) for _ in range(data_size)],
    "Grades": grades,
    "Does_Sports": bool_columns[3],
    "In_Relationship": bool_columns[4],
    "Criminal_Record": criminal_record_values,
    "Family_Income": family_income,
    "School_Type": [fake.random_element(school_types) for _ in range(data_size)],
    "Parents_Substance_Abuse": bool_columns[5],
    "Father_Educated": bool_columns[6],
    "Mother_Educated": bool_columns[7]
}

df = pd.DataFrame(data)

# Introducing some null values
np.random.seed(0)
for col in df.columns:
    if np.random.rand() > 0.2:  # 80% chance to add nulls
        df.loc[df.sample(frac=np.random.uniform(0.001, 0.005)).index, col] = np.nan

# Exporting to a CSV file
file_path = "drug and alcohol abuse - dataset.csv"
df.to_csv(file_path, index=True)
print(f"Dataset saved to {file_path}")
