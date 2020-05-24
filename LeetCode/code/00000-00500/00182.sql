select Email
from (select Email, count(Email) as cnt
     from Person
     group by Email) as statistic
 where cnt > 1

 select Email
 from Person
 group by Email
 having count(Email) > 1

 select distinct a.Email as 'Email'
 from Person as a
 join Person as b
 on a.Email = b.Email and a.Id != b.Id