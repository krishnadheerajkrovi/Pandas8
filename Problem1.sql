/*
1. Since we have to calculate time spent by each employee on each day, we have to group the data by emp_id and event_day.
2. For each day, the total time spent is out_time - in_time.
*/

select event_day as day, emp_id, sum(out_time - in_time) as total_time
from employees
group by event_day, emp_id