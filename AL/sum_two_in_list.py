def solution(numbers):
    answer = []
    realanswer = []
    i_index = 0
    
    for i in numbers:
        j_index = 0
        
        for j in numbers:
            
            if i_index == j_index:
                pass
            
            else:
                if i+j not in answer:
                    ans = i+j
                    answer.append(ans)
                
                else:
                    pass
            
            j_index += 1    
        
        i_index += 1
                
    answer.sort()
    return answer
