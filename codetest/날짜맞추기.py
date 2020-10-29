def solution(a, b):
    
    dayList = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    
    # 5월 24일은 화요일이다.
    # 1,3,5,7,8,10,12 월은 31일까지 있다 4,6,9,11월은 30일까지 있다. 2월은 28일까지 있다.
    # 년도를 4로 나눠서 나머지가 0이면 2월은 29일까지 존재한다.#단 2016년만 게산
    thirtyOne = [1,3,5,7,8,10,12]
    thirty = [4,6,9,11]
    feb = [2]
    
    
    # 5월 24 화요일을 기점으로 계산해야 한다.
    #ex) a =  3 b = 14     5월 24일 - 3월 14일 = 31 29 31 30 24 - 31 29 14 = 17 30 24 = 71 7로 나누먄 
    
    daysum = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366 ]
    
    standard = daysum[4] + 24
    question = daysum[a - 1] + b
    
    if question > standard:
        diff = question - standard 
        day = diff % 7
        answer = dayList[(2 + day) % 7 ]
        return answer
    
    elif question < standard:
        diff = standard - question
        day = diff % 7
        answer = dayList[(2 - day) % 7 ]
        return answer        
    
    else:
        return "TUE"
