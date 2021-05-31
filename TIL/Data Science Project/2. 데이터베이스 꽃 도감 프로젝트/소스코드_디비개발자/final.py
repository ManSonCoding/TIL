#모듈 모음.

import requests
import pandas as pd
import json
import xmltodict
import random
import numpy as np


MAXPLANTNUM = 200

# API접속하여 데이터를 가져오는 함수###################################################

def go_to_api(self, url,set ,pID):
    URL = url    #URL 여기에 바꾸시면 됩니다.
    response = requests.get(URL)
    response.status_code

    if set == True:
        params = {"apiKey": "202005291NH6HWCTHLGRTH7IOERMYA", "numOfRows": "240"}
        res = requests.get(URL, params=params)
        response_text = res.text
        response_dict = json.dumps(xmltodict.parse(response_text), indent=4)
        st_python = json.loads(response_dict)

        flowers = pd.DataFrame(st_python['response']['body']['items']['item'])
        flowers = flowers[['%s' % self]]
        # 파라미터 추가방식 {" ":" "," ":" "}
    else:
        params = {{"apiKey": "202005291NH6HWCTHLGRTH7IOERMYA", "cntntsNo": "%d" % pID }}
        res = requests.get(URL, params=params)
        response_text = res.text
        response_dict = json.dumps(xmltodict.parse(response_text), indent=4)
        st_python = json.loads(response_dict)

        flowers = pd.DataFrame(st_python['response']['body']['items']['item'])
        flowers = flowers[['items']['%s' % self]]


    return flowers

##################################################################################
# API 접속하여 테이블을 만드는 함수


## 컨텐츠 번호를 가져옴
cntntsNo = 'cntntsNo'
url = 'http://api.nongsaro.go.kr/service/garden/gardenList'
url2 = ''
num = go_to_api(cntntsNo,url,True,1)

## 컨텐츠 이름을 가져옴
cntntsSj = 'cntntsSj'
name = go_to_api(cntntsSj,url,True,1)


## 식물 가격을 가져옴
plantPrice = 'http://api.nongsaro.go.kr/service/garden/gardenDtl'
pcBigInfo = 'pcBigInfo'



price = {}

#for i in range(MAXPLANTNUM):

indexNum = {}
indexName = {}
shape = {}
flowerColor ={}
waterCycle = {}
priceType = {}
winterLwet ={}
# 인덱스 테스트



print(type(indexNum))
## 식물 형태를 가져옴

###################API 연결#####################################################
for i in range(MAXPLANTNUM) :
    indexNum[i] = int(num.iloc[i, 0])

    indexName[i] = name.iloc[i, 0]
    indexName[i] = indexName[i].replace("'", "", 2)


    URL = 'http://api.nongsaro.go.kr/service/garden/gardenDtl'    #URL 여기에 바꾸시면 됩니다.
    response = requests.get(URL)
    params = {"apiKey": "202005291NH6HWCTHLGRTH7IOERMYA","cntntsNo":"%d" % indexNum[i] } #파라미터 추가방식 {" ":" "," ":" "}
    res = requests.get(URL, params=params)
    response_text = res.text
    response_dict = json.dumps(xmltodict.parse(response_text), indent=4)
    st_python = json.loads(response_dict)
    flowers = pd.DataFrame(st_python['response']['body'])

    shape[i] = flowers['item']['grwhstleCodeNm']
    flowerColor[i] = flowers['item']['flclrCodeNm']

    waterCycle[i] = flowers['item']['watercycleWinterCode']

    if waterCycle[i] == None:
        waterCycle[i] = '053004'

    winterLwet[i] = flowers['item']['winterLwetTpCode']
    random.seed(i)
    priceType[i] = random.randrange(1,10)


# print(shape[i])


#보정



#####################################################################################################################
##여기까지가 수정선 입니다.                                                                                               #
#####################################################################################################################


# postgres 실행
print("check ")
import psycopg2 as pg2



try: # port 기본값 = 5432
    conn = pg2.connect("host = localhost dbname=postgres user=postgres password=1234")
    # autocommit 없으면, InternalError: CREATE DATABASE cannot run inside a transaction block
    conn.autocommit = True
    cur = conn.cursor()

    # database 만들기
    cur.execute('create database testdb') # superuser 만 create database 명령어 가능..
    cur.execute('SELECT version()')
    ver = cur.fetchone()


except Exception as e:
    e = 'postgresql database connection error!'
    #print(e)

else:
    print(ver)

finally:
    if conn:
        conn.close()


try: # 다른 db 로 바꿀려면 재접속 해야함...
    conn = pg2.connect("host = localhost dbname=testdb user=postgres password=9075")
    cur = conn.cursor()

    cur.execute("DROP TABLE INFORMATION")
    cur.execute("DROP TABLE user2")
    cur.execute("DROP TABLE recommendation")



    # table 만들기
    cur.execute("CREATE TABLE information (Id INTEGER PRIMARY KEY, Name VARCHAR(30), Shape VARCHAR(30), flcl VARCHAR(50),temp INT,Price INT, waterCycle INT)")
    cur.execute("CREATE TABLE recommendation (Name VARCHAR(30), UID VARCHAR(30), Price INT)")
    cur.execute("CREATE TABLE user2 (UID INT PRIMARY KEY, temp INT, Price INT, waterCycle INT)")



    examplePrice = 2000  ##price 코드 파싱 변수 넣으면 됨.
    # data insert

    for i in range(MAXPLANTNUM):
        random.seed(i+1)
        cur.execute("INSERT INTO information VALUES(%d,'%s','%s','%s', %d, %d, %d)" % (int(indexNum[i]), indexName[i], shape[i], flowerColor[i], int(winterLwet[i]), priceType[i], int(waterCycle[i]) ))

        ind = random.randrange(MAXPLANTNUM)
        cur.execute("INSERT INTO recommendation VALUES('%s',%d,  %d)" % (indexName[ind],random.randrange(MAXPLANTNUM), priceType[ind]))




        if i % 4 == 0:
            cur.execute("INSERT INTO user2 VALUES(%d, %d, %d, 53001)" %( i+1 , random.randrange(30) ,random.randrange(40)))
        elif i % 4 ==1:
            cur.execute("INSERT INTO user2 VALUES(%d, %d, %d, 53002)" %( i+1 , random.randrange(30) ,random.randrange(40)))
        elif i % 4 ==2:
            cur.execute("INSERT INTO user2 VALUES(%d, %d, %d, 53003)" %( i+1 , random.randrange(30) ,random.randrange(40)))
        else:
            cur.execute("INSERT INTO user2 VALUES(%d, %d, %d, 53004)" %( i+1 , random.randrange(30) ,random.randrange(40)))




    cur.execute("SELECT * FROM RECOMMENDATION")
    rows = cur.fetchall()
    conn.commit()


except Exception as e:
    print(e)
    if conn:
        conn.rollback()

else:
    print(rows)

finally:
    if conn:
        conn.close()





###########################################################################
#       ==  PLANT WORLD ==
#
###################################################################
