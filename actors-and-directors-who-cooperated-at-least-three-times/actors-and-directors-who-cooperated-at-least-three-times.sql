# Write your MySQL query statement below
SELECT
    actor_id, director_id
FROM
    (SELECT 
        actor_id, director_id, COUNT(timestamp) AS num
    FROM 
        ActorDirector
    GROUP BY
        actor_id, director_id)AS freq
WHERE
    freq.num>=3;
