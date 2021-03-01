# class Player:
#     def __init__(self, name, country, age, no_of_matches, runs, wickets):
#         self.name=name
#         self.country=country
#         self.age= age
#         self.no_of_matches=no_of_matches
#         self.runs = runs
#         self.wickets=wickets
# class Team:
#     def getMinRuns(self,players):
#         return min(players, key=lambda x: x.runs)
#     def getMaxWickets(self,players):
#         return max(players, key=lambda x:x.wickets)
    
# n=int(input())
# player_objects=[]
# for _ in range(n):
#     name,country,age, matches, runs, wickets=input(),input(), int(input()),int(input()),int(input()), int(input())
#     player_objects.append(Player(name,country,age, matches,runs, wickets))

# team = Team()
# max_p=team.getMaxWickets(player_objects)
# min_runs=team.getMinRuns(player_objects)
# print(max_p.name)
# print(max_p.runs)
# print(max_p.country)
# print(min_runs.name)
# print(min_runs.wickets)
# print(min_runs.country)
# import re
# s=input()
# print(len(re.sub(r'[a-zA-Z0-9 ]','',s)))
# s=input()
# print(' '.join(s.split()[::-1]))

# from itertools import accumulate, combinations
# n=int(input())
# ratings=sorted([int(input()) for _ in range(n)])
# acc=list(accumulate(ratings, lambda x,y:abs(x-y)))
# pairs=list(combinations(ratings,2))
# # for ele,ac in zip(pairs,acc):
#     # if 
# d1=list(map(int,input().split()))
# d2=list(map(int,input().split()))
# print(min([abs(i-j) for i,j in zip(d1,d2)])

# l,r=map(int,input().split())
# print(sum(str(bin(i))[2:].count('1')%2==0 for i in range(l,r+1)))
# from math import sqrt
# def checkprime(x):
#     if x > 2 and x % 2 == 0:
#         return False
#     elif x < 2:
#         return False
#     else:
#         for i in range(2, int(sqrt(x)) + 1):
#             if x % i == 0:
#                 return False
#         return True
#     return False

# import re
# from string import ascii_lowercase
# data={j:i for i,j in enumerate(ascii_lowercase,1)}
# s=input().lower()
# if sum([sum(map(lambda x:data[x],st)) for st in re.split(r'[^a-z]',s)]):
#     print("Prime String")
# else:
#     print("Not prime")
# exec("try:\n\t if you[0]!='ME':\n\t\t print('hello', you) \nexcept: pass")
# import random
# data_set=''.join([random.choices('ATGC')[0] for _ in range(127)])
# print(data_set.count('A'), data_set.count('AT'), data_set.count('G'), data_set.count('GC'))
# n=int(input())
# for i in range(1,101):
#     print(f'{n} x {i} = {n*i}')
# import cgi
# form = cgi.FieldStorage()  
# print(form.keys())
# # if not (form.has_key("name") and form.has_key("age")):  
#     # print("<H1>Name & Age not Entered</H1>")
#     # print("Fill the Name & Age accurately.") 

# print("<p>name:", form["name"].value) 
# print("<p>Age:", form["age"].value)

from string import ascii_lowercase
data={j:i for i,j in enumerate(ascii_lowercase,1)}
s="anaconda"
print(sum(map(lambda x:data[x], s)))