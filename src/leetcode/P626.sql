SELECT s1.id,s2.student
FROM Seat s1, Seat s2
WHERE if(mod(s1.id,2)=0
,s1.id-1=s2.id
,s1.id+1=s2.id OR (s1.id=s2.id AND s1.id = (SELECT max(id) FROM Seat))
)
ORDER BY s1.id