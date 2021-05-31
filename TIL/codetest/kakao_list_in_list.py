board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

from pprint import pprint

# 열의 빈칸을 찾고 값을 리턴하는 인덱스
def solution(board, moves):
    doll = []
    answer = 0
    # moves를 이용해 index를 접근한다.
    for i in moves:
        i = i - 1
        for j in range(len(board)):

            if (board[j][i] == 0):
                pass

            else:

                re = board[j][i]
                board[j][i] = 0

                doll.append(re)
                # 스택에 같은 인형 2개가 쌓이면 제거한다.
                if len(doll) > 1:
                    if (doll[-1] == doll[-2]):
                        doll.pop()
                        doll.pop()
                        answer += 2
                break
    return answer






