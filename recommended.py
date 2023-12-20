import pandas as pd
data = {
    'User': ['User1', 'User1', 'User2', 'User2', 'User3', 'User3', 'User4', 'User4', 'User5', 'User5'],
    'Movie': ['Movie1', 'Movie2', 'Movie1', 'Movie3', 'Movie2', 'Movie4', 'Movie3', 'Movie4', 'Movie5', 'Movie2'],
    'Rating': [5,4,3,4,5,5,3,1,5,3]
}
df = pd.DataFrame(data)
def recommend_movies(user):
  user_ratings = df[df['User'] == user]
  similar_users = df[(df['Movie'].isin(user_ratings['Movie']))& (df['User'] != user)&(df['Rating'] >=3)]
  movie_ratings = similar_users.groupby('Movie')['Rating'].mean()
  recommended_movies = movie_ratings.sort_values(ascending=False)
  return recommended_movies.index.to_list()
while True:
  user = input('Enter your username: ')
  if user.lower() == 'exit':
    print('Goodbye!')
    break
  elif user in df['User'].unique():
    recommended_movies = recommend_movies(user)
    print(f'Recommended movies for {user}: {recommended_movies}')
  else:
    print(f"User '{user}' not found in the dataset. please try again.")
