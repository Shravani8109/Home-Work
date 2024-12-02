list=[]
list.append('shravani')
print(list)

name=["shravani","raj","shivani",1,2,3,1+8j]
print(name)
print(type(name))
print(name[1:])

movies = ["Action1", "Action2", "Action3","comedy1"]
# movies.index("Action2")
print(movies[0:3])
print(movies[-1])
print(movies[-2])
movies.append("shravani")
print(movies)

movies.pop(-1)
print(movies)

movies.insert(4,"shravani")
print(movies)

# real_movie_nmame=["kgf","RRR","Devil"]
# real_movie_nmame.extend(movies)
# print(real_movie_nmame)

# real_movie_nmame + movies
# print(real_movie_nmame)
# print("*"*5)
# print([1,2,3]*5)

list=[1,2,3,4,5,6,7,8,9,10]
print(list[0:4] * 2)

msg = "your appointment is tomorrow \n"
print(msg * 3)

list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[:]
print(list2)
list1.append("shravani")
print(list1)
print(list2)

movies = ["Action1", "Action2", "Action3","comedy1"]
movies.index("Action2")
print(movies)