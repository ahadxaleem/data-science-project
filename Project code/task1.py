import os
import json
def task1():
    onlyfiles = next(os.walk(r"C:\Users\bbb\Desktop\proj1\course\data\a1\content\HealthStory"))[2] #dir is your directory path as string
    x=len(onlyfiles)
    # Opening JSON file
    f = open(r'C:\Users\bbb\Desktop\proj1\course\data\a1\reviews\HealthStory.json')
    data=json.load(f)
    y=len(data)
    
    return
