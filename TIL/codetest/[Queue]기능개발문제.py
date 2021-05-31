# JUNCODE 
# 21/01/04
# 기능개발 문제

# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

def solution(progresses, speeds):
    
    temp = []
    temp2 = []
    answer = []
    temp3 = []
    k = 0
    i = 0
    
    #모든 작업이 끝날 때 까지 반복
    while(len(temp) != len(progresses)):
        
        # 100퍼센트 달성하면 배포
        if progresses[i] >= 100:
            temp.append(progresses[i])
            temp2.append(k)
            i += 1
            
            

            
        # 100퍼센트 달성하지 못했다면, speed에 있는 만큼 진척도 증가
        else:
            for j in range(len(speeds)):
                progresses[j] += speeds[j]
        
            k += 1
        
    print(temp2)    
    
    #중복 개수를 제거한 리스트 생성
    for j in temp2:
        if j not in temp3:
            temp3.append(j)
    
    #배포 가능 개수 계산하여 answer에 append
    for m in range(len(temp3)):
        answer.append(temp2.count(temp3[m]))
    
    
    
    return answer
