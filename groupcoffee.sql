select coffee_name,count(*) as orders, round(sum(money), 2) as money
from coffee 
group by coffee_name 
order by money desc;
