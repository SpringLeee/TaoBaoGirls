import urllib.request
from pyquery import PyQuery as pq
import os

def HttpClient(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html=pq(response.read().decode("gbk"))
    return html


def  wfileinfo():
    finfo=open(str("Data/"+UserinfoDetailList.eq(0).find("span").html())+"/个人资料.txt","w",encoding='utf-8')
    finfo.write("                                                         "+ "\n")
    finfo.write("                                                         "+ "\n")
    finfo.write("    -----------------------------------------------------"+ "\n")
    finfo.write("                                                         "+ "\n")
    finfo.write("    昵 称 :    "+UserinfoDetailList.eq(0).find("span").html()+"   \n");
    finfo.write("    生 日 :    "+UserinfoDetailList.eq(1).find("span").html() + "\n")
    finfo.write("    城 市 :    "+UserinfoDetailList.eq(2).find("span").html() + "\n")
    finfo.write("    职 业 :    "+UserinfoDetailList.eq(3).find("span").html() + "\n")
    finfo.write("    学校/专业: "+UserinfoDetailList.eq(5).find("span").html() + "\n")
    finfo.write("    身 高 :    "+UserinfoDetailList.eq(7).find("p").html() + "\n")
    finfo.write("    体 重 :    "+UserinfoDetailList.eq(8).find("p").html() + "\n")
    finfo.write("                                                         "+ "\n")
    finfo.write("    -----------------------------------------------------"+ "\n")
    finfo.close()

os.mkdir("Data")

for p in range(1,10):
    
    url = 'https://mm.taobao.com/json/request_top_list.htm?page='+str(p)
    html=HttpClient(url)
    list=html('.lady-name')
    for x in list.items():

     userlink=x.attr("href")
     index=userlink.find("id=")
     uid = userlink[index+3:]

     userinfourl="https://mm.taobao.com/self/info/model_info_show.htm?user_id="+str(uid)
     userinfohtml=HttpClient(userinfourl)
     UserinfoDetailList=userinfohtml(".mm-p-base-info").find("li")
     Userdomin=userinfohtml(".mm-p-domain-info").find("ul").find("li").find("span").html()

    
     if Userdomin!=None:
        nickname=UserinfoDetailList.eq(0).find("span").html()
        os.mkdir("Data/"+nickname)
        wfileinfo()
        userimghtml=HttpClient("https:"+Userdomin)
        UserImgInfoList=userimghtml(".mm-aixiu-content").find("img")
        a=0
        for y in UserImgInfoList.items():
         try: 
           a+=1
           print("                                                ")
           print("   正在抓取  "+nickname+"  的第"+str(a)+"张图片.......")
           uimg ="http:" + y.attr("src")
           nickurl="Data/"+str(nickname) +"/"+ str(a)+".jpg"
           urllib.request.urlretrieve(uimg,nickurl)
         except: 
             e="error" 