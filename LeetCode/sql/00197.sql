select a.Id as 'Id'
from Weather as a
    join Weather as b on datediff(a.RecordDate, b.RecordDate) = 1
where a.Temperature > b.Temperature