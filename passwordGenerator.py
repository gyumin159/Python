# 유저가 설정한 특정 조건에 맞는 비밀번호를 생성해주는 프로그램.
# 조건은 길이(length), 특수문자의 활용여부, 대소문자, 숫자 포함여부 4가지 고려
# 길이는 처음에 입력받으므로 해결(필수)
# 우선 길이만큼의 크기를 가지는 리스트를 만들고
# 길이를 제외한 나머지 조건들에 맞는 랜덤한 값은 순서대로 넣은 후
# 리스트를 순환하며 False인 애들은 랜덤으로 값을 정해주고 shuffle을 이용해 섞은 후 join()을 이용해 붙힌걸 리턴하자.

import random

def generate(length, spa=True, num=True, bs=True) -> str:
    if length < 4 :
        return 'PassWord too short!'
    password = [False] * length
    conditions = [spa, num]
    if bs:
        conditions += [True, True]
    else:
        conditions += [False, False]

    spa_cha = list(range(32, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))
    nums = list(range(48, 58))
    big = list(range(65, 91)) # 32를 더해주면 소문자
    temp = [spa_cha, nums, big, [x+32 for x in big]]

    i = 0
    # 선택된 조건에 맞는 값 무조건 선택후 password에 순서대로 넣음
    while i < 4:
        if conditions[i]:
            random_num = random.randint(0,len(temp[i]) - 1)
            selected = chr(temp[i][random_num])
            password[i] = selected
        i += 1
    # password를 순회하면 False인 값은 랜덤으로 지정해서 넣음
    for i, p in enumerate(password):
        if p == False:
            password[i] = chr(random.randint(32, 126))
    random.shuffle(password)
    
    return ''.join(password)
        



print(generate(25))
