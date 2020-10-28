import psycopg2 as pg2

import random

#새로운 사람을 만드는 클래스
class new_person :

    def __init__(self, celcious = None, money = None , watercycle = None, id = None):
        if celcious == None :
            self.celcious = "온도정보 없어요!"
        if money == None :
            self.celcious = "돈이 없어요!"
            return
        self.celcious = celcious
        self.money = money
        self.watercycle = watercycle
        self.id = id

    def setInfo(self):
        print("당신의 집 온도는 몇 도 입니까?(정수형)")
        self.celcious = int(input())

        print("당신은 얼마를 가지고 있습니까? ex> 21000원일 경우 21 입력")
        self.money = int(input())

        self.watercycle = int(input("당신이 식물을 기른다면, 얼마나 자주 관리하겠습니까?\n 1.자주 \n 2.보통 \n 3.드물게 \n 4. 거의 안함 \n"))
        if self.watercycle == 1:
            self.watercycle = 53002
        elif self.watercycle == 2:
            self.watercycle = 53003
        elif self.watercycle == 3:
            self.watercycle = 53004
        elif self.watercycle == 4:
            self.watercycle = 53001

        self.id = 0


def make_new_person():
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


        ###새로운 유저 추가
        print("아이디를 입력해주세요")
        id = int(input())



        if id < 200:
            cur.execute("select uid from user2 where uid = %d " % id)
            rows = cur.fetchall()
            chk = rows[0][0]
            print(chk)

            if chk == id:
                # 있을 경
                cur.execute("select temp, price,watercycle from user2 where uid = %d" % id)
                rows = cur.fetchall()
                a = new_person()
                a.id = chk
                a.celcious = int(rows[0][0])
                a.money = int(rows[0][1])
                a.watercycle = int(rows[0][2])

            if  chk != id:
                #없을 경우
                print("id가 없습니다 새로 가입합ㄴ디ㅏ.")
                a = new_person()
                a.setInfo()
                print(a.celcious, a.money, a.watercycle)
                cur.execute("SELECT count(*) from user2")
                b = cur.fetchone()

             #   a.id = int(b[0] + 1)
                cur.execute("INSERT INTO user2 VALUES(%d, %d, %d, %d)" % (a.id, a.celcious, a.money, a.watercycle))
                print("debug 1")
        else:
            a = new_person()
            a.setInfo()
            print(a.celcious, a.money, a.watercycle)
            cur.execute("SELECT count(*) from user2")
            b = cur.fetchone()
            a.id = int(b[0] + 1)
            print("당신의 아이디는 %d" %a.id)

            cur.execute("INSERT INTO user2 VALUES(%d, %d, %d, %d)" % (a.id, a.celcious, a.money, a.watercycle))



        cur.execute("SELECT name FROM information WHERE waterCycle =  %d and temp >%d and price<%d " % (a.watercycle, a.celcious, a.money))
        rows = cur.fetchall()
        print("==================")
        print("ID: %d님께 추천드릴 식물은" % a.id)
        plt = rows[random.randrange(0, len(rows))]
        print(plt[0])
        plt = plt[0].replace(",","",1)

        print("%s 입니다!" % (plt))
        print("==================")

        cur.execute("INSERT INTO RECOMMENDATION VALUES('%s', %d, %d)" %( plt, a.id, a.money))

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




def showfunc():
    print("== 기능을 선택해주세요 == ")
    print("1.나만의 식물 추천 받기")
    print("2.장바구니 확인")
    print("3.식물 검색")
    print("4.종료")



def checkcart():

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


        ###새로운 유저 추가
        print("아이디를 입력해주세요 ")
        allPrice = 0
        id = int(input())

        cur.execute("select name , price from recommendation where uid = '%d' " % id)


        rows = cur.fetchall()
        print(rows)
        for i in len(rows):
            allPrice = allPrice + int(rows[i,1])

        print("장바구니에 담긴 총 비용은 %d 입니다" %allPrice )

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



def searchPT():

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

        print("메뉴를 입력해 주세요")
        print("1. 이름으로 검색하기")
        print("2. 가격으로 검색하기")
        print("3. 온도로 검색하기 ")
        print("4.종료")
        search = int(input())
        if search == 1:
            print("이름을 입력해주세요")
            plantname = input()
            cur.execute("select * from information where name like '%%%s%%' " % plantname)

        elif search == 2:
            print("가격을 입력해주세요 ex> 예시 = 20 ")
            plantprice = int(input())

            cur.execute("select * from information where price < %d" % plantprice)

        elif search == 3:
            print("온도를 입력해주세요 ex> 예시 = 20 ")

            planttemp = int(input())

            if planttemp < 0:
                planttemp =  57001
            elif  0 <= planttemp and planttemp < 5 :
                planttemp = 57002
            elif 5 <= planttemp and planttemp <7 :
                planttemp = 57003
            elif 7 <= planttemp and planttemp <10:
                planttemp = 57004
            elif 10 <= planttemp:
                planttemp = 57005


            cur.execute("select * from information where temp <= %d" % planttemp)



        else:
            print("잘못된 번호입니다. 다시 입력하세요.")





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




######################################################################################################################
#                                                                                                                   #
#                                                       프로그램 실행부                                                 #
#                                                                                                                   #
######################################################################################################################
# 새로운 사람을 만듬.
print("=== welcome to plant world ===")


while True:
    showfunc()

    func = int(input())
    if func == 1:

        make_new_person()
    elif func == 2:
        checkcart()
    elif func == 3:
        searchPT()

    elif func == 4:
        print("종료합니다")
        break
    else:
        continue

