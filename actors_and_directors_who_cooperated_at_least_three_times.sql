/* Write your PL/SQL query statement below */

/*

You are given ActorDirector tabel with columns actor_id, director_id, timestamp.
Find pairs that had at least 3 collaborations.
Return in any order.

I can simply group by the pair and count. Then filter that into at least 3 collabs.

```
select collab_counts.actor_id as actor_id, collab_counts.director_id as director_id
from (
    select count(1) collab_count, actor_director.actor_id, actor_director.director_id
    from ActorDirector actor_director
    group by actor_director.actor_id, actor_director.director_id
) collab_counts

where collab_counts.collab_count >= 3
```

There is a option to count in having filter that is faster.

*/


select actor_director.actor_id, actor_director.director_id
from ActorDirector actor_director
group by actor_director.actor_id, actor_director.director_id
having count(1) >= 3;