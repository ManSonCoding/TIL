#########################################
# 2020. 09.24 프로그래머스 level 1 hash 문제 #
#########################################



def solution(participant, completion):

    
    # 정렬된 리스트를 만든다    
    sort_part = sorted(list(participant))
    sort_com = sorted(list(completion))

    #셋된 리스트를 만든다
    set_part = list(set(sort_part))
    set_com = list(set(sort_com)) 


    # 동명이인이 없거나 , 동명이인이 아닌 사람이 완주했을 경우
    if len(set_part) - 1 == len(set_com):
        for i in range(0, len(sort_com)):
            # i 번째 인덱스를 비교한다.
            if sort_part[i] != sort_com[i]:
                return sort_part[i]
                
        #참가자의 마지막 완주자가 실패했을 경우    
        return sort_part[-1]

    #동명이인이 완주 실패할 경우    
    else:

        #동명이인이 완주 실패한 경우 세트 리스트안의 요소는 같게 됨
        if len(set_part) == len(set_com):
            for i in range(0, len(sort_com)):


            # i 번째 인덱스를 비교한다.
                if sort_part[i] != sort_com[i]:
                    return sort_part[i]
                    
            #참가자의 마지막 완주자가 실패했을 경우            
            return sort_part[-1]
