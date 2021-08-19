## 행렬 전치

def matrixMult(A):
    row=len(A)
    col=len(A[0])    
    
    B = [[0 for row in range(row)]for col in range(col)]
    
    for i in range(row):
        for j in range(col):
            B[j][i]=A[i][j]
    return B
 
           
A = [[2, -3],[-1, 4]]
matrixMult(A)

def solution(scores):
    student = []
    
    # 행렬 바꾸기
    scores = matrixMult(scores)
            
    for row in range(len(scores)):
        for col in range(len(scores)):
            # 자기 자신 평가 점수
            if row == col:
                myScore = scores[row][col]
                temp = []
                for i in scores[row]:
                    temp.append(i)

                temp.pop(temp.index(myScore))
        # 유일한 최고점, 유일한 최저점 판단.
        if myScore > max(temp):
            average = sum(temp) / float(len(temp))

        elif myScore < min(temp):
            average = sum(temp) / float(len(temp))

        else:
            print(scores[row])
            average = sum(scores[row]) / float(len(scores[row]))
        
        # 평균 구하기
        student.append(average)
        
    for i in range(len(student)):
        if student[i] >= 90:
            student[i] = 'A'
        elif student[i] >= 80:
            student[i] = 'B'
        elif student[i] >= 70:
            student[i] = 'C'
        elif student[i] >= 50:
            student[i] = 'D'
        else:
            student[i] = 'F'
    
            
    # 점수 변환
    answer = "".join(student)
    return answer
