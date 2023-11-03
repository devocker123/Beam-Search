import numpy as np

def create_data_model():
    """Stores the data for the problem."""
    data = {}


    # The estimated distance matrix is an array whose i, j entry is the distance from location i to location j in miles,
    # where the array indices correspond to the locations in the following order:
    data["distance_matrix"] = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972], #new york 1
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579], #Los angeles 2
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260], # chicago 3
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987], #minneapolis 4
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371], #Denver 5
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999], #Dallas 6
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701], #Seattle 7
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099], #Boston 8
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600], #san francisco 9
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162], #st.louis 10
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200], #Houston 11
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],#phoenix 12
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0], #salt lake 13
    ]

    # The distance matrix assumes that travelling between cities is symmetrical and bi-directional, meaning you can travel
    # from New York to Denver in 1631 miles and travel back from Denver to New York in 1631 miles

    # These distance values are estimates. As such, they do not accurately represent the distance between the cities.

    # These are the names of the cities with respect to the indices of the above matrix
    # Some examples are written below to give you an idea:
    # data["distance_matrix"][0][0] would represent distance from New York to New York which is 0 miles
    # data["distance_matrix"][0][3] would represent distance from New York to Minneapolis which is 1018 miles
    # data["distance_matrix"][2][4] would represent distance from Chicago to Denver which is 920 miles
    data["cities"] = { 0 : "New York",
                       1 : "Los Angeles",
                       2 : "Chicago",
                       3 : "Minneapolis",
                       4 : "Denver",
                       5 : "Dallas",
                       6 : "Seattle",
                       7 : "Boston",
                       8 : "San Francisco",
                       9 : "St. Louis",
                       10: "Houston",
                       11: "Phoenix",
                       12: "Salt Lake City" }
    return data


'''
Question: Using the Beam search algorithm, find the shortest possible path for the person starting from New York City, 
visiting every city afterward only once and comes back home to New York City. Assume a beam value of 2. For your heuristics, 
use the total estimated distance which has been travelled thus far by the node.
I.e. if a node has travelled from New York -> Boston -> Chicago so far. 
It’s heuristic value would be 213 + 851 = 1064 Heuristic Value. 
Your output should show the result in the following format 
(Where City1 would be replaced by New York, City2 would be replaced by Los Angeles etc):
Path: City1 -> City2 -> City3 -> .... -> City1.

Total Estimated Distance: 2098 miles
'''

# # # Beam search code goes here
def beam_search(data, beam_value = 2):
    cities = data['cities']
    distance_matrix = data['distance_matrix']
    start_city = 0
    goal_city = 0
    number_of_cities = len(cities)
    beam = [(start_city, [start_city], 0)]
#     count = 0
    while True:
        new_beam = []
        
        for item in beam:
            neighbors = [next_city for next_city in range(number_of_cities) if next_city not in item[1]]#path
            for next_city in neighbors:
                new_path = item[1] + [next_city]
                new_distance = item[2] + distance_matrix[item[0]][next_city]
                heuristics = new_distance
#                 print(item[1])
                new_beam.append((next_city, new_path, new_distance, heuristics))
            
            
        if not new_beam:
            break
                    
        new_beam.sort(key = lambda x: x[2])
        beam = new_beam[:beam_value]
        
#         print(beam[0][1])
#         print(beam[0][0])
        if len(beam[0][1]) == number_of_cities + 1 and beam[0][1][-1] == start_city:
#             print("abcd")
            break

            
    best_path = beam[0][1]
    best_path.append(start_city)
    total_distance = beam[0][2]
    total_distance = beam[0][2] + distance_matrix[best_path[-2]][start_city]
    
    city_names = [cities[city] for city in best_path]
    path_str = "Path: " + " -> ".join(city_names) + "."
    print("Beam value : ", + beam_value)
    print(path_str)
    print(total_distance)
#     return path_str, total_distance

# Example usage:
data = create_data_model()
beam_search(data, beam_value = 2)


# # Varying Beam Search code goes here
def varying_beam_search(data, beam_value):  # Set beam_value to 10
    cities = data['cities']
    distance_matrix = data['distance_matrix']
    start_city = 0
    goal_city = 0
    number_of_cities = len(cities)
    beam = [(start_city, [start_city], 0)]
    while True:
        new_beam = []
        
        for item in beam:
            neighbors = [next_city for next_city in range(number_of_cities) if next_city not in item[1]]
            for next_city in neighbors:
                new_path = item[1] + [next_city]
                new_distance = item[2] + distance_matrix[item[0]][next_city]
                heuristics = new_distance
                new_beam.append((next_city, new_path, new_distance, heuristics))
        if not new_beam:
            break
        new_beam.sort(key=lambda x: x[2])
        beam = new_beam[:beam_value]

        if len(beam[0][1]) == number_of_cities + 1 and beam[0][1][-1] == start_city:
            break

    beam2 = [] # new beam to add start city for complete path

    for item in beam:
        current_city = item[0] # updation of beam values
        current_path = item[1]
        current_distance = item[2]
        current_heuristic = item[3]
    
        #final distance
        distance_to_start = data["distance_matrix"][current_city][start_city]
    
        #update path
        updated_path = current_path + [start_city]
        updated_distance = current_distance + distance_to_start
    
        # Update the heuristic value
        updated_heuristic = updated_distance  # You can update the heuristic as needed
    
        beam2.append((current_city, updated_path, updated_distance, updated_heuristic))



#######
    beam2.sort(key=lambda x: x[2])
#     print(beam2)
    best_path = beam2[0][1]
#     best_path.append(start_city)
    print("best path : " ,best_path)
    total_distance = beam2[0][2] #+ distance_matrix[best_path[-2]][start_city]

    city_names = [cities[city] for city in best_path]
    path_str = "Path: " + " -> ".join(city_names) + "."
    print("Beam value:", beam_value)
    print(path_str)
    print("Total Distance:", total_distance)
    return path_str, total_distance

# Example usage:
data = create_data_model()
varying_beam_search(data, beam_value=10)  # Set beam_value to 10


# Graph Code goes here
import matplotlib.pyplot as plt

def calculate_total_distance(beam_value):
    path_str, total_distance = varying_beam_search(data, beam_value)
    return total_distance


beam_values = list(range(2, 1001))
total_distances = []


for beam_value in beam_values:
    total_distance = calculate_total_distance(beam_value)
    total_distances.append(total_distance)

# Create a line plot
plt.figure(figsize=(12, 6))
plt.plot(beam_values, total_distances, marker='o', linestyle='-')
plt.title('Total Distance vs. Beam Value')
plt.xlabel('Beam Value')
plt.ylabel('Total Distance (miles)')
plt.grid(True)

# Show the plot
plt.show()


'''
Obversations
1.   List item
From the above the graph for beam values between 2 - 1000 the graph shows multiple local minima. generally the distance decreases as
beam value increases. on lower beam values the search space is typically narrow hence only limited number of path are explored.
this leads to local minimas. but as beam value approaches to 1000, the computation cost is increased however search space also increases
and this helps explore variety of paths escaping local minimas and providing optimal solution.
2.   List item
'''

'''
   stochastic beam search vs local beam search
    
    stochastic beam search assigns a fitness score or certain function to each path. and then selects a particular path based 
    on its fitness score or particular function value which is considered the fittest. with this appraoch a certain randomness 
    is added to this selection process for a particular path. this helps in escaping the local minima solutions.
    
    example:
        in this particular problem of traveling salesman, while using local beam search if the start city is new york then 
        we can see in the Question 3 section that initially it takes path 0, 7, 2, 9, 10, 5, 4, 12, 11, 1, 8, 6, 3, 0 and 
        continues to consider going from 0 -> 7 -> 2 -> 9 -> 10 and does not consider any other possibility. this is the reason
        why we can see observe in the graph the local optima. stochastic beam search can provide more optimal solution and 
        avoid local optimas through random selection method based on which path is the fittest.
    
'''
