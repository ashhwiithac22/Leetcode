# Write your MySQL query statement below
select p.product_id, coalesce(pr.new_price, 10) as price
from (select distinct product_id from Products ) p
left join Products pr
on p.product_id = pr.product_id
and pr.change_date = (
  select max(change_date)
  from Products
  where product_id = p.product_id
  and change_date <= '2019-08-16'
);
