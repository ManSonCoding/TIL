def solution(new_id):
    answer = ''

    table = str.maketrans("~!@#$%^&*()=+[{]}:?,<>/",\
                          "                       ")

    # 1단계, 대문자를 소문자로 모두 변환한다.
    check_id = new_id.lower()

    # 2단계, 사용할 수 있는 문자열을 변환한다. , 빈칸 제거
    check_id = check_id.translate(table)
    check_id = check_id.replace(" ","")

    # 3단계, 연속으로 사용되는 점을 하나로 대체한다.
    double = False
    while(double == False):

        if '..' in check_id:
            check_id = check_id.replace("..", ".")

        else:
            double = True



    # 4단계, 처음과 마지막으로 점을 사용하였는지 확인하고 제거한다.
    check_id = check_id.strip('.')

    # 5단계, 빈문자열인지 확인한다.

    if check_id == '':
        check_id = 'a'
    # 6단계, 아이디의 길이를 확인하여 15자를 제외한 나머지를 제거한다.
    if len(check_id) >= 16:
        check_id = check_id[0:15]

    check_id = check_id.strip('.')

    # 7단계, 아이디의 길이가 3자 이상인지 확인한다.
    if len(check_id) <= 3:
        while len(check_id) < 3:
            check_id += check_id[-1]

    answer = check_id
    return answer
