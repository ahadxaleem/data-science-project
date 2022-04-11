import json
import math
import csv
def task7():
    # Opening JSON file
    f = open(r'task6.json')
    data=json.load(f)
    # print(len(data))
    words=[]
    for i in data:
        if len(data[i])<10:
            continue
        elif len(data[i]) == 1638:
            continue
        else:
            words.append(i)
    words.sort()
    # print(len(words))
    fake_news=[]
    real_news=[]
    # Opening JSON file
    f = open(r'C:\Users\bbb\Desktop\proj1\course\data\a1\reviews\HealthStory.json')
    data1=json.load(f)
    for j in data1:
        if j['rating']<3:
            fake_news.append(j['news_id'])
        else:
            real_news.append(j['news_id'])
    # print(fake_news)
    pr={}
    pf={}
    Or={}
    of={}
    lof={}
    for k in words:
        real_count=0
        fake_count=0
        for x in data[k]:
            if x in real_news:
                real_count+=1
            elif x in fake_news:
                fake_count+=1
        tempr=real_count/len(real_news)
        tempf=fake_count/len(fake_news)
        if tempr in [1.0,0.0] or tempf in [1.0,0.0]:
            continue
        else:
            pr[k]=tempr
            pf[k]=tempf
            Or[k]=pr[k]/(1-pr[k])
            of[k]=pf[k]/(1-pf[k])
            lof[k]=round(math.log10(of[k]/Or[k]),5)
            # lof[k]=of[k]/Or[k]
    # field names 
    fields = ['word', 'log_odds_ratio']
    # writing to csv file 
    with open('task7a.csv', 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        #writing all the rows
        for y in lof:
            row=[]
            row.append(y)
            row.append(lof[y])
            # writing the data rows 
            csvwriter.writerow(row)
    # print(Or)
    return
