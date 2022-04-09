import os
import json
def task1():
    onlyfiles = next(os.walk(r"C:\Users\bbb\Desktop\proj1\course\data\a1\content\HealthStory"))[2]
    x=len(onlyfiles)
    # Opening JSON file
    f = open(r'C:\Users\bbb\Desktop\proj1\course\data\a1\reviews\HealthStory.json')
    data=json.load(f)
    y=len(data)
    f2=open(r'C:\Users\bbb\Desktop\proj1\course\data\a1\engagements\HealthStory.json')
    data2=json.load(f2)
    tweets=list()
    for i in data2.values():
        tweets.extend(i['tweets'])
        # print(i)
    
    z=len(set(tweets))
    dictionary={ 
    "Total number of articles": x, 
    "Total number of reviews": y,  
    "Total number of tweets": z 
    }
    with open("task1.json", "w") as outfile:
        json.dump(dictionary, outfile) 
    return
