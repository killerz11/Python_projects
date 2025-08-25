import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [66,77,99]
}
student_df = pd.DataFrame(student_dict)
print(student_df)

#loop through rows of df
for (index, row) in student_df.iterrows():
    print(row)
