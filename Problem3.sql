/*
1. We need to find classes that have atleast 5 students, so group by class.
2. Filter out classes that have atleast 5 students.
*/

select class
from courses
group by class
having count(class) >= 5