#import pandas
import pandas as pd

#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

years = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93,90] 
movie_dict = {"years": years,"durations":durations}
print(movie_dict)

#create dataframe

durations=pd.DataFrame(movi_dict)
# print DataFrame
print(durations)

fig=plt.figure()
plt.plot(years,durations)
# Read csv as a dataFrame

#print the first rows
net_pd[0:5]

net_pd = pd.read_csv('datasets'/netflix.csv)
#show the plot
plt.show()
#add plot title
plt.title("A graph of durations against years")

#create subset for movie
net_movie_only=net_pd[['type']='movie']

#select columns

net_movie-col =net_movie_only[["title","country","genre","release_year","Duration"]]

#Create figure and increase size

fig = plt.figure(figsize-12,8)
# create a scatter plot
plt.scatter('duration','year')
