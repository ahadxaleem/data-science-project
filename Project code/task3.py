import os
import json
import datetime
import csv
import matplotlib.pyplot as plt
def task3():
    # assign directory
    directory = r'C:\Users\bbb\Desktop\proj1\course\data\a1\content\HealthStory'
    # field names 
    fields = [ 'news_id', 'year', 'month', 'day']
    # iterate over files in
    # that directory

    with open('task3a.csv', 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        graph={}
        #writing all the rows
        for filename in os.scandir(directory):
            if filename.is_file():
                # Opening JSON file
                f = open(filename.path)
                data=json.load(f)
                # Initializing a timestamp value
                Timestamp = data['publish_date']
                
                # Calling the fromtimestamp() function
                # over the above specified Timestamp
                if Timestamp==None:
                    continue
                else:
                    row=[]
                    date_From_Timestamp = datetime.date.fromtimestamp(Timestamp)
                    row.append(filename.name)
                    row.append(date_From_Timestamp.year)
                    row.append(date_From_Timestamp.month)
                    row.append(date_From_Timestamp.day)
                    # writing the data rows 
                    csvwriter.writerow(row)
                    if date_From_Timestamp.year in graph:
                        graph[date_From_Timestamp.year]+=1
                    else:
                        graph[date_From_Timestamp.year]=1
                    # print(date_From_Timestamp)
                    # print(filename)
        # Plotting barchart
        plt.bar(graph.keys(), graph.values())
        
        # Saving the figure.
        plt.savefig("task3b.png")
    return
