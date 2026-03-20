/*
1. We need to compute number of subjects each teacher teaches so group by teacher_id.
2. Count the distinct number of subjects.
*/

select teacher_id, count(distinct subject_id) as cnt
from teacher
group by teacher_id