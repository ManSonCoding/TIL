#
# 09 26 코딩테스트 - 완전탐색문제
#
def solution(answers):
    
    math_hate1 = [1,2,3,4,5]
    math_hate2 = [2,1,2,3,2,4,2,5]
    math_hate3 = [3,3,1,1,2,2,4,4,5,5]
    rank = []
    hate1_count = 0
    hate2_count = 0
    hate3_count = 0
    answer = []

    for i in range(0,len(answers)):
        if(answers[i] == math_hate1[(i + 5) % 5]):
            hate1_count += 1
        
        if(answers[i] == math_hate2[(i + 8) % 8]):
            hate2_count += 1 
            
        if(answers[i] == math_hate3[(i + 10) % 10]):
            hate3_count += 1
            
    # 1 혼자 제일 큰 경우
    if((hate1_count > hate2_count) & (hate1_count > hate3_count) ):
        answer.append(1)
    # 2 혼자 제일 큰 경우
    elif((hate2_count > hate1_count) & (hate2_count > hate3_count) ):
        answer.append(2)

    # 3 혼자 제일 큰 경우
    elif((hate3_count > hate1_count) & (hate3_count > hate2_count) ):
        answer.append(3)

    # 1,2 제일 큰 경우
    elif((hate1_count == hate2_count) & (hate1_count > hate3_count) ):
        answer.append(1)
        answer.append(2)


    # 1,3 제일 큰 경우
    elif((hate1_count == hate3_count) & (hate1_count > hate2_count) ):
        answer.append(1)
        answer.append(3)
    
    # 1,2,3 제일 큰경우
    elif((hate1_count == hate2_count) & (hate2_count == hate3_count) ):
        answer.append(1)
        answer.append(2)
        answer.append(3)

    # 2,3 제일 큰 경우
    elif((hate2_count > hate1_count) & (hate2_count == hate3_count)):
        answer.append(2)
        answer.append(3)   
        
        
    return answer
