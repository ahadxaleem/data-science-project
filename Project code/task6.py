import re
import os
import json
def removeStops(letter):
        N = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
        return False if letter in N else True
def task6():
    # assign directory
    directory = r'C:\Users\bbb\Desktop\proj1\course\data\a1\content\HealthStory'
    dictionary={}
    for filename in os.scandir(directory):
            if filename.is_file():
                # Opening JSON file
                f = open(filename.path)
                data=json.load(f)
                text = re.sub(r'[^a-zA-Z]',' ',data['text'])
                # filteredtxt=re.sub(r'[\t\n]',' ',text)
                text1=re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', text)
                lowertxt=text1.lower()
                list_of_words=lowertxt.split()
                filtered_list_of_words=list(filter(removeStops,list_of_words))
                filtered_list_of_words.sort()
                for i in filtered_list_of_words:
                    if i in dictionary:
                        if filename.name in dictionary[i]:
                            continue
                        else:
                            dictionary[i].append(filename.name)
                    else:
                        dictionary[i]=[filename.name]
                # print(dictionary)
                with open("task6.json", "w") as outfile:
                    json.dump(dictionary, outfile) 
    return
