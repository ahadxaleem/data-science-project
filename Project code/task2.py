import csv
import json
def task2():
    # field names 
    fields = ['news_id', 'news_title', 'review_title', 'rating', 'num_satisfactory']
    # Opening JSON file
    f = open(r'C:\Users\bbb\Desktop\proj1\course\data\a1\reviews\HealthStory.json')
    data=json.load(f)
    # writing to csv file 
    with open('task2.csv', 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        for i in data:
            row=[]
            row.append(i['news_id'])
            row.append(i['original_title'])
            row.append(i['title'])
            row.append(str(i['rating']))
            num_satisfactory=0
            for x in i['criteria']:
                if x['answer']=='Satisfactory':
                    num_satisfactory+=1
            row.append(str(num_satisfactory))
            # writing the data rows 
            csvwriter.writerow(row)
    
    return
