import json
sentence="this is a super idea This idea will change the idea of learning"
words=sentence.split()
d={}
for one in words:
    key=one
    if key not in d:
        count=words.count(key)
        d[key]=count
print("counting frequencies in list \n",words)
print(json.dumps(d,indent=1))
