select Customers.Name as 'Customers'
from Customers
where Customers.Id not in (select CustomerId
                            from Orders)

select a.Name as 'Customers'
from Customers as a
left join Orders as b
on a.Id = b.CustomerId
where b.CustomerId is null
