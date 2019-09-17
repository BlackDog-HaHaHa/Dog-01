import requests
import re


for page in range(1,5):
    url='http://www.ygdy8.net/html/gndy/dyzz/list_23_'+str(page)+'.html'
    print(url)
    html=requests.get(url)
    html.encoding="gb2312"
    #print(html.text)
    data=re.findall('<a href="(.*?)" class="ulink">',html.text)
    #print(data)
    for m in data:
        xqurl = 'http://www.ygdy8.net'+m
        #print(xqurl)

        html2=requests.get(xqurl)
        html2.encoding='gb2312'
        #print(html2.text)
        try:
            dyLink = re.findall('<a href="(.*?)">ftp://.*?</a></td>',html2.text)[0]
            print(dyLink)
        except:
            print("no")

        with open('list.txt','a') as f:
            f.write(dyLink+'\n')