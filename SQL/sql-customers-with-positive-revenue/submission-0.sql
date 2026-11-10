-- Write your query below
select customers.customer_id
from customers
where customers.revenue > 0
and customers.year = 2020