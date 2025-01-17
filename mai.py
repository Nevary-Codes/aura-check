import pandas as pd

data = pd.read_csv("Scripts/sample.csv", delimiter="\t")
dropped_questions = []
for i in data.columns:
    if i.startswith("Q") and (i.endswith("I") or i.endswith("E")):
        dropped_questions.append(i)

data = data.drop(dropped_questions, axis=1)

data.to_excel("abc.xlsx")