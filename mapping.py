import pandas as pd

ml_ratings = pd.read_csv('datasets/ml-1m/ratings.dat', sep='::', header=None,
                         names=['user', 'movie', 'rating', 'timestamp'], engine='python')

ml_users = pd.read_csv('datasets/ml-1m/users.dat', sep='::', header=None,
                       names=['user', 'gender', 'age', 'occupation', 'zipcode'], engine='python')

ml_movies = pd.read_csv('datasets/ml-1m/movies.dat', sep='::', header=None,
                        names=['movie', 'title', 'genre'], engine='python', encoding='latin-1')

db_movies = pd.read_csv('datasets/dbpedia/movies', sep='::', header=None,
                        names=['movie', 'title', 'year'], engine='python', encoding='utf-8')


# 부제 처리 (두번째 괄호 삭제)


# 관사 처리
test1 = 'Les ' + ml_movies['title'][72].replace(', Les', '')


# 년도 처리 title + (년도 film), title + (film), title ==> title + (년도)
db_movies['title'][61517]