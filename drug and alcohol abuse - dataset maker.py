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
substances = ["None", "Alcohol", "Drugs", "Alcohol and Drugs"]
grades = np.random.randint(0, 101, size=data_size)
family_income = np.random.randint(20000, 100001, size=data_size)
bool_columns = [np.random.choice([0, 1], size=data_size).astype(bool) for _ in range(9)]

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
    "Criminal_Record": bool_columns[5],
    "Family_Income": family_income,
    "School_Type": [fake.random_element(school_types) for _ in range(data_size)],
    "Parents_Substance_Abuse": bool_columns[6],
    "Father_Educated": bool_columns[7],
    "Mother_Educated": bool_columns[8]
}

df = pd.DataFrame(data)

# Introducing some null values
np.random.seed(0)
for col in df.columns:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

# Exporting to a CSV file
file_path = "drug and alcohol abuse - dataset.csv"
df.to_csv(file_path, index=True)
print(f"Dataset saved to {file_path}")
