from collections import Counter


name = input("Enter your name: ")

def recommend_movies(user, movies, neighbors=5):
  

  
  user_similarities = {}
  for other_user in movies:
    if other_user == user:
      continue
    rated_movies_in_common = len(set(movies[user]) & set(movies[other_user]))
    total_rated_movies = len(movies[user]) + len(movies[other_user])
    user_similarities[other_user] = rated_movies_in_common / total_rated_movies

  
  nearest_neighbors = sorted(user_similarities, key=user_similarities.get, reverse=True)[:neighbors]

 
  recommendations = Counter()
  for neighbor in nearest_neighbors:
    for movie in movies[neighbor]:
      if movie not in movies[user]:
        recommendations[movie] += user_similarities[neighbor]

 
  return [movie for movie, _ in recommendations.most_common() if movie not in movies[user]]


movies = {
  "Alice": ["The Matrix", "Fight Club", "Inception"],
  "Bob": ["The Matrix", "The Terminator", "Pulp Fiction"],
  "Charlie": ["Casablanca", "Citizen Kane", "The Godfather"],
  
}

recommendations = recommend_movies(name, movies)
print(f"Movie recommendations: {recommendations}")
