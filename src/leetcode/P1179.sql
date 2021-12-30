SELECT id,
SUM(CASE WHEN month='Jan' THEN revenue ELSE NULL END) Jan_revenue,
SUM(CASE WHEN month='Feb' THEN revenue ELSE NULL END) Feb_revenue,
SUM(CASE WHEN month='Mar' THEN revenue ELSE NULL END) Mar_revenue,
SUM(CASE WHEN month='Apr' THEN revenue ELSE NULL END) Apr_revenue,
SUM(CASE WHEN month='May' THEN revenue ELSE NULL END) May_revenue,
SUM(CASE WHEN month='Jun' THEN revenue ELSE NULL END) Jun_revenue,
SUM(CASE WHEN month='Jul' THEN revenue ELSE NULL END) Jul_revenue,
SUM(CASE WHEN month='Aug' THEN revenue ELSE NULL END) Aug_revenue,
SUM(CASE WHEN month='Sep' THEN revenue ELSE NULL END) Sep_revenue,
SUM(CASE WHEN month='Oct' THEN revenue ELSE NULL END) Oct_revenue,
SUM(CASE WHEN month='Nov' THEN revenue ELSE NULL END) Nov_revenue,
SUM(CASE WHEN month='Dec' THEN revenue ELSE NULL END) Dec_revenue
FROM department
GROUP BY 1