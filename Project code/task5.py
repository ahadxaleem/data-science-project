import json
import matplotlib.pyplot as plt
def task5():
    # Opening JSON file
    f = open(r'C:\Users\bbb\Desktop\proj1\course\data\a1\reviews\HealthStory.json')
    data=json.load(f)
    rating_group={}
    for i in data:
        if i['rating'] in rating_group:
            rating_group[i['rating']].append(i['news_id'])
        else:
            rating_group[i['rating']]=[i['news_id']]
    f2=open(r'C:\Users\bbb\Desktop\proj1\course\data\a1\engagements\HealthStory.json')
    data2=json.load(f2)
    no_of_tweets=[0]*6
    for j in rating_group:
        for x in rating_group[j]:
            no_of_tweets[j]+=len((data2[x])['tweets'])
            no_of_tweets[j]+=len((data2[x])['retweets'])
    average=[0]*6
    for k in rating_group:
        average[k]=no_of_tweets[k]/len(rating_group[k])
    # print(average)
    rating=[0,1,2,3,4,5]
    plt.xlabel("Rating")
    plt.ylabel("Average Tweets")
    # Plotting barchart
    plt.bar(rating,average)
    
    # Saving the figure.
    plt.savefig("task5.png")
    return
