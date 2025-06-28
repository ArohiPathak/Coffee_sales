select cash_type as payment_method, count(*) as number
from coffee group by cash_type;