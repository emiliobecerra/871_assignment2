import pandas as pd
import matplotlib.pyplot as plt
import os

csv_path = "~/Desktop/ECON870/assignment2/Occupation.csv"
csv_path2 = "~/Desktop/ECON870/assignment2/elections.csv"

df = pd.read_csv(csv_path)
elections = pd.read_csv(csv_path2)



occupation_mapping = {
    1: 'Exec, Admin, Mgmt',
    2: 'Professional Specialty',
    3: 'Technician, Support',
    4: 'Sales',
    5: 'Admin Support',
    6: 'Private Household',
    7: 'Protective Service',
    8: 'Service',
    9: 'Farming, Forestry',
    10: 'Crafts, Repair',
    11: 'Machine Operators',
    12: 'Transportation',
    13: 'Manual Labor',
    14: 'Military'
}


df['Occupation'].fillna('Unknown', inplace=True)

df['Occupation'] = df['Occupation'].map(occupation_mapping)

occupation_counts = df['Occupation'].value_counts()

occupation_proportions = occupation_counts / occupation_counts.sum()


plt.figure(figsize=(10, 6))

plt.barh(occupation_proportions.index, occupation_proportions)
plt.xlabel('Proportion')
plt.ylabel('Occupation')
plt.title('Proportion of Occupations among Democrat Voters')
plt.tight_layout()  
# plt.show()




filtered_elections = elections[elections['VCF0004'].isin([2000, 2004])]

columns_to_keep = ["VCF0004", "VCF0101", "VCF0104", "VCF0106A", "VCF0704A"]

filtered_elections_subset = filtered_elections[columns_to_keep]

age_table_columns = ["VCF0004", "VCF0704A", "VCF0101"]
Age_Table = filtered_elections[age_table_columns]

gender_table_columns = ["VCF0004", "VCF0704A", "VCF0104"]
Gender_Table = filtered_elections[gender_table_columns]
print(Gender_Table)

race_table_columns = ["VCF0004", "VCF0704A", "VCF0106A"]
Race_Table = filtered_elections[race_table_columns]
# print(Race_Table)

party_mapping = {1: 'Democratic', 2: 'Republican'}

summary_data = {}

for year in [2000, 2004]:
    for party_code, party_name in party_mapping.items():
        filter_condition = (Gender_Table['VCF0004'] == year) & (Gender_Table['VCF0704A'] == party_code)
        
        gender_data = Gender_Table.loc[filter_condition, 'VCF0104']
        
        summary_statistics = {
            'Mean': gender_data.mean(),
            'Number of Observations': gender_data.count()
        }
        
        column_name = f'{year} {party_name}'
        
        summary_data[column_name] = summary_statistics

Gender_Summary = pd.DataFrame(summary_data)

print(Gender_Summary)

export_path = "~/Desktop/ECON870/assignment2/Gender_Summary.csv"

export_path = os.path.expanduser(export_path)

Gender_Summary.to_csv(export_path, index=False)

print(f"Gender_Summary exported to {export_path}")

summary_data = {}

for year in [2000, 2004]:
    for party_code, party_name in party_mapping.items():
        filter_condition = (Race_Table['VCF0004'] == year) & (Race_Table['VCF0704A'] == party_code)
        
        race_data = Race_Table.loc[filter_condition, 'VCF0106A']
        
        summary_statistics = {
            'Mean': race_data.mean(),
            'Number of Observations': race_data.count()
        }
        
        column_name = f'{year} {party_name}'
        
        summary_data[column_name] = summary_statistics

Race_Summary = pd.DataFrame(summary_data)

print(Race_Summary)

export_path = "~/Desktop/ECON870/assignment2/Race_Summary.csv"

export_path = os.path.expanduser(export_path)

Race_Summary.to_csv(export_path, index=False)

print(f"Race_Summary exported to {export_path}")

party_mapping = {1: 'Democratic', 2: 'Republican'}

summary_data = {}

for year in [2000, 2004]:
    for party_code, party_name in party_mapping.items():
        filter_condition = (Age_Table['VCF0004'] == year) & (Age_Table['VCF0704A'] == party_code)
        
        age_data = Age_Table.loc[filter_condition, 'VCF0101']
        
        summary_statistics = {
            'Mean': age_data.mean(),
            'Standard Deviation': age_data.std(),
            'Minimum': age_data.min(),
            'Median': age_data.median(),
            'Maximum': age_data.max(),
            'Number of Observations': age_data.count()
        }
        
        column_name = f'{year} {party_name}'
        
        summary_data[column_name] = summary_statistics

Age_Summary = pd.DataFrame(summary_data)

print(Age_Summary)

export_path = "~/Desktop/ECON870/assignment2/Age_Summary.csv"

export_path = os.path.expanduser(export_path)

Age_Summary.to_csv(export_path, index=False)

print(f"Age_Summary exported to {export_path}")



