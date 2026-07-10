# Write your MySQL query statement below
select e.name from Employee e join employee e1 on e1.managerId=e.id group by e1.managerId having count(*)>=5
