"""
1. We need to compute number of subjects each teacher teaches so group by teacher_id.
2. Count the distinct number of subjects.
"""

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    return df.rename(columns={'subject_id': 'cnt'})