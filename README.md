# Beam-Search

Travelling Salesman problem solved through Beam search

The Traveling Salesman Problem is usually defined by the question: &quot;If there is a list of
cities and distances between each pair of cities, what is the shortest route that visits each city and
returns to the original city?&quot;
Example: In the graph below, if the Traveling salesman starts at &#39;A&#39;, he needs to visit &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;,
&#39;F&#39; and comes back to &#39;A&#39; while making sure the total distance he has travelled is at a minimum.
![image](https://github.com/muhammad-12345/Beam-Search/assets/111753966/43a841b5-ca73-42df-9b5c-b2a77e965710)

The shortest path that originates and ends at A is A → B → C → D → E → F → A
The cost of the path is: 16 + 21 + 12 + 15 + 16 + 34 = 114.

![image](https://github.com/muhammad-12345/Beam-Search/assets/111753966/35829e14-3019-4b8a-9d7b-6bb6b8cd6abe)


Project description:
A person in the USA has decided to travel from New York to various cities across the USA and come
back to his home in New York in 1 trip. He wants to avoid visiting the same city twice (except New
York which is his starting and ending city).
With rising fuel prices every day, he wants to cover the least distance possible.
Using the Beam search algorithm, we will finding the shortest possible path for the person
starting from New York City, visiting every city afterward only once and comes back home to New
York City.
