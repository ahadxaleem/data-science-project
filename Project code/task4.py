import json
import csv
import matplotlib.pyplot as plt
def task4():
    # Opening JSON file
    f = open(r'C:\Users\bbb\Desktop\proj1\course\data\a1\reviews\HealthStory.json')
    data=json.load(f)
    # field names 
    fields = [ 'news_source', 'num_articles', 'avg_rating']
    # writing to csv file 
    with open('task4a.csv', 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
        # writing the fields 
        csvwriter.writerow(fields) 
        source={}
        #writing all the rows
        for i in data:
            if i['news_source']=="":
                continue
            else:
                if i['news_source'] in source:
                    source[i['news_source']].append(i['rating'])
                else:
                    source[i['news_source']]=[i['rating']]
        sorted_source={}
        # Dictionary’s value sorted in keys. 
        for i in sorted (source) :
            sorted_source[i]=source[i]
        graph={}
        for x in sorted_source:
            row=[]
            row.append(x)
            row.append(len(sorted_source[x]))
            row.append(sum(sorted_source[x])/len(sorted_source[x]))
            # writing the data rows 
            csvwriter.writerow(row)
            if len(sorted_source[x])>=5:
                graph[x]=sum(sorted_source[x])/len(sorted_source[x])
        sortedgraph=dict(sorted(graph.items(), key = lambda kv: kv[1]))
        plt.xticks(rotation='vertical')
        # Plotting barchart
        plt.bar(sortedgraph.keys(), sortedgraph.values())
        
        # Saving the figure.
        plt.savefig("task4b.png")

    return
