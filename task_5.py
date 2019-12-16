import csv
import json
import requests
import urllib
url="https://randomuser.me/api/"
with open('csv/random_user.csv','w') as f:
    response=requests.get(url)
    r=response.text
    writer=csv.writer(f,delimiter=',',quotechar='|')
    json_parse=json.loads(r)
    j=json_parse["results"][0].keys()
    writer.writerow([j[1],j[11],j[8],j[10]])
    location=json_parse["results"][0]["location"].keys()
    #only for testing
    x=0
    print "location index:"
    while x<6:
        l=location[x]
        print l
        x+=1
    k=0
    print "\nresult index:"
    while k<12:
        print (j[k])
        k+=1
    #only for testing
    i=0
    for i in range(0,10):
        response=requests.get(url)
        r=response.text
        json_parse=json.loads(r)
        
        name=json_parse["results"][0]["name"].values()
        n=name[0]+" "+name[1]
        n=n.encode('ascii', 'ignore')

        email=json_parse["results"][0].values()
        e=email[11]
        e=e.encode('ascii', 'ignore')

        location=json_parse["results"][0]["location"].values()
        l=location[0]
        l=l.encode('ascii', 'ignore')

        login=json_parse["results"][0]["login"].values()
        u=login[0]
        u=u.encode('ascii', 'ignore')

        writer=csv.writer(f,delimiter=',',quotechar='|')
        writer.writerow([n,e,l,u])

        pic=json_parse["results"][0]["picture"].values()
        p=pic[1]
        urllib.urlretrieve(p, 'pics/'+u+'.jpg')
        i+=1
    f.close()

    """k=0
    while k<10:
        print j[i]
        i+=1

        j=json_parse.encode(encoding='UTF-8', errors='ignore')
    for i in j:
       print j[i].encode("ascii","ignore")
        """