import json
import math
import csv
import matplotlib.pyplot as plt
  
# Function returns N largest elements
def Nmaxelements(list1, N):
    final_list = {}
  
    for i in range(0, N): 
        max1 = 0
        index1=''
        for j in list1:     
            if list1[j] > max1:
                max1 = list1[j]
                index1=j  
        final_list[index1]=max1
        list1.pop(index1)
    return final_list

# Function returns N smallest elements
def Nminelements(list1, N):
    final_list = {}
  
    for i in range(0, N): 
        max1 = 0
        index1=''
        for j in list1:     
            if list1[j] < max1:
                max1 = list1[j]
                index1=j  
        final_list[index1]=max1
        list1.pop(index1)
    return final_list

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
    plt.xlabel("log_odds_ratio")
    plt.ylabel("Count")
    # Plotting histogram
    plt.hist(lof.values(),bins=30)
    
    # Saving the figure.
    plt.savefig("task7b.png")
    figure, axis = plt.subplots(1,2)
    # plt.xticks(rotation='vertical')
    # figure.tight_layout()
    max=Nmaxelements(lof,15)
    for tick in axis[0].get_xticklabels():
        tick.set_rotation(90)
    axis[0].bar(max.keys(),max.values())
    axis[0].set_title("highest odds ratios")
    min=Nminelements(lof,15)
    for tick in axis[1].get_xticklabels():
        tick.set_rotation(90)
    axis[1].bar(min.keys(),min.values())
    axis[1].set_title("lowest odds ratios")
    # Saving the figure.
    plt.savefig("task7c.png",bbox_inches ="tight")
    # print(Or)
    return
