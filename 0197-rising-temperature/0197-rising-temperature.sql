# Write your MySQL query statement below
select today.id
from Weather today
join weather yesterday
    on today.recordDate = Date_ADD(yesterday.recordDate , interval 1 Day)
where today.temperature > yesterday.temperature