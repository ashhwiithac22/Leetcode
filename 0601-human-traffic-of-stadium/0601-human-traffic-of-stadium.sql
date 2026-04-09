# Write your MySQL query statement below
select id, visit_date, people
from (
    select *, id - row_number() over(order by id) as grp
    from stadium 
    where people >= 100
) t
where grp in (
    select grp from (
        select id - row_number() over(order by id) as grp
        from stadium
        where people >= 100
    ) x
group by grp 
having count(*) >= 3 
)
order by visit_date;