"""
1. Since we have to calculate time spent by each employee on each day, we have to group the data by emp_id and event_day.
2. For each day, the total time spent is out_time - in_time.
"""

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    df = employees.groupby(['event_day','emp_id']).sum('total_time').reset_index()
    return (df[['event_day','emp_id','total_time']].rename(columns={'event_day':'day'}))
