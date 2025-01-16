import pandas as pd
import numpy as np

# Define column names based on the provided structure
columns = [
    "Q1A", "Q1I", "Q1E", "Q2A", "Q2I", "Q2E", "Q3A", "Q3I", "Q3E", "Q4A", "Q4I", "Q4E",
    "Q5A", "Q5I", "Q5E", "Q6A", "Q6I", "Q6E", "Q7A", "Q7I", "Q7E", "Q8A", "Q8I", "Q8E",
    "Q9A", "Q9I", "Q9E", "Q10A", "Q10I", "Q10E", "Q11A", "Q11I", "Q11E", "Q12A", "Q12I", "Q12E",
    "Q13A", "Q13I", "Q13E", "Q14A", "Q14I", "Q14E", "Q15A", "Q15I", "Q15E", "Q16A", "Q16I", "Q16E",
    "Q17A", "Q17I", "Q17E", "Q18A", "Q18I", "Q18E", "Q19A", "Q19I", "Q19E", "Q20A", "Q20I", "Q20E",
    "Q21A", "Q21I", "Q21E", "Q22A", "Q22I", "Q22E", "Q23A", "Q23I", "Q23E", "Q24A", "Q24I", "Q24E",
    "Q25A", "Q25I", "Q25E", "Q26A", "Q26I", "Q26E", "Q27A", "Q27I", "Q27E", "Q28A", "Q28I", "Q28E",
    "Q29A", "Q29I", "Q29E", "Q30A", "Q30I", "Q30E", "Q31A", "Q31I", "Q31E", "Q32A", "Q32I", "Q32E",
    "Q33A", "Q33I", "Q33E", "Q34A", "Q34I", "Q34E", "Q35A", "Q35I", "Q35E", "Q36A", "Q36I", "Q36E",
    "Q37A", "Q37I", "Q37E", "Q38A", "Q38I", "Q38E", "Q39A", "Q39I", "Q39E", "Q40A", "Q40I", "Q40E",
    "Q41A", "Q41I", "Q41E", "Q42A", "Q42I", "Q42E", "country", "source", "introelapse", "testelapse",
    "surveyelapse", "TIPI1", "TIPI2", "TIPI3", "TIPI4", "TIPI5", "TIPI6", "TIPI7", "TIPI8", "TIPI9",
    "TIPI10", "VCL1", "VCL2", "VCL3", "VCL4", "VCL5", "VCL6", "VCL7", "VCL8", "VCL9", "VCL10",
    "VCL11", "VCL12", "VCL13", "VCL14", "VCL15", "VCL16", "education", "urban", "gender", "engnat",
    "age", "screensize", "uniquenetworklocation", "hand", "religion", "orientation", "race", "voted",
    "married", "familysize", "major"
]

# Generate random data based on the sample provided
num_rows = 100
data = []

for _ in range(num_rows):
    row = np.random.randint(1, 50, size=len(columns) - 16).tolist()  # Random values for numerical fields
    row += [
        "IN",  # country
        np.random.randint(1, 5),  # source
        np.random.randint(1, 50),  # introelapse
        np.random.randint(100, 10000),  # testelapse
        np.random.randint(100, 10000),  # surveyelapse
        np.random.randint(1, 7), np.random.randint(1, 7), np.random.randint(1, 7), np.random.randint(1, 7),
        np.random.randint(1, 7), np.random.randint(1, 7), np.random.randint(1, 7), np.random.randint(1, 7),
        np.random.randint(1, 7), np.random.randint(1, 7),  # TIPI scores
        np.random.randint(0, 2), np.random.randint(0, 2), np.random.randint(0, 2), np.random.randint(0, 2),
        np.random.randint(0, 2), np.random.randint(0, 2), np.random.randint(0, 2), np.random.randint(0, 2),
        np.random.randint(0, 2), np.random.randint(0, 2), np.random.randint(0, 2), np.random.randint(0, 2),
        np.random.randint(0, 2), np.random.randint(0, 2), np.random.randint(0, 2), np.random.randint(0, 2),  # VCL responses
        np.random.randint(1, 5),  # education
        np.random.randint(1, 5),  # urban
        np.random.randint(1, 3),  # gender
        np.random.randint(1, 3),  # engnat
        np.random.randint(18, 70),  # age
        np.random.randint(1, 20),  # screensize
        np.random.randint(1, 5),  # uniquenetworklocation
        np.random.randint(1, 3),  # hand
        np.random.randint(1, 12),  # religion
        np.random.randint(1, 5),  # orientation
        np.random.randint(1, 10),  # race
        np.random.randint(0, 2),  # voted
        np.random.randint(0, 2),  # married
        np.random.randint(1, 10),  # familysize
        np.random.randint(1, 5)  # major
    ]
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
file_path = "random_dataset.csv"
df.to_csv(file_path, index=False)

file_path