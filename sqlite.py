import urllib.request
import urllib.parse
import json
url = 'https://streamable.com/v3o8'
urls = ['https://streamable.com/v3o8','http://streamable.com/bn1z','http://streamable.com/37le']  
def duration(url):
    with urllib.request.urlopen(url) as response:
       html = response.read() #Get Page Source
    s = html.decode("utf-8") #Make it not Bytes
    s = s.split('\n') #Split it by New Line
    boot = ''#Find the bootstrap variable in the source page
    for a in s:
        if 'bootstrap' in a:
            boot = a  
            
    loc = boot.find('JSON')#Find the "JSON Parser starting point"
    JSON_Parser = boot[loc:] #Rebuild Array
    x = JSON_Parser[12:] #Ignores white spaces

    #For this to work you need to remove the " and replace the whole json of backslashes
    x = x.replace('\\','')
    x = x[:len(x)-3]
    d = json.loads(x)
    print(d['video']['duration'])

for a in urls:
    duration(a)
