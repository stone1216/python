import requests
from bs4 import  BeautifulSoup
import time
import json
from selenium import webdriver

url="http://www.nowcoder.com/profile/558780/codeBookDetail?submissionId=6406291"
url1="http://www.baidu.com"
driver=webdriver.Chrome()

driver.get(url)
driver.find_element_by_id("emailIpt").send_keys("1013116273@qq.com")
driver.find_element_by_id("passwordIpt").send_keys("090932yanglei")
driver.find_element_by_id("loginBtn").click()
time.sleep(1)
html=driver.page_source


Result=[]

def getResult():
    question=driver.find_element_by_class_name("subject-question").text
    answerstate=driver.find_element_by_class_name("font-green").text
    if(answerstate=="状态：答案正确"):
        html=driver.page_source
        bsObj=BeautifulSoup(html,'lxml')
        ans=bsObj.find('div',{'class','result-subject-item'})
        s=ans.contents[3].text
        pos1=s.find('class')
        pos2=s.find('/**')
        if (pos1>0&pos2>0):
            pos=min(pos1,pos2)
        else:
            pos=max(pos1,pos2)

        answer=s[pos:]
        info=[question,answer]
        Result.append(info)

i=1
while True:
    try:
        getResult()
        print('第%s页' %i)
        driver.find_element_by_link_text("下一题").click()
    except Exception as Ex:
        print(Ex)
        with open('result.txt', 'w+', encoding='utf-8') as fp:
            json.dump(Result, fp, ensure_ascii=False)
        print("停止搜索")
        break


