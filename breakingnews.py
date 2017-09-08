import mechanize
import time
from bs4 import BeautifulSoup


br = mechanize.Browser()

br.addheaders = [("User-agent","Chrome")]
br.set_handle_robots(False)


id = "enter the id of the last shared news"
while True: 
    
    source = br.open("http://www.trthaber.com/m/?news=&news_id="+str(id)).read()
    soup = BeautifulSoup(source)
    writingHead= soup.h2 

    
    if  writingHead == None:
        print "NONEWS"
    
    elif writingHead != None:
        print "BREAKINGNEWS"
        
        contentHTML = soup.find_all("p")
        content = ""
       
        for i in contentHTML:
            content = content + i.text
        
        news = writingHead.text.upper()+"\n\n\n\n"+content
        print news
        
        
        
        id = id+1
    
    time.sleep(30)
