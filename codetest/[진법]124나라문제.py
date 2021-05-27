# python 3

def solution(n):
    answer = []
    # 3진법으로 변환
    while n > 3:
        divd = n //3
        mod = n % 3
        # 0 숫자 변환
        if mod == 0:
            divd -= 1
            mod = 3
        n = divd
        answer.append(str(mod))
    answer.append(str(n))
    
    answer = ''.join(answer)
    # 3숫자 변환
    answer = answer.replace('3','4')
    
    # 리스트 결과 거꾸로 출력
    return answer[::-1]


