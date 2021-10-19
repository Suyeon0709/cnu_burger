# 1. 햄버거 단품 메뉴 선택하는 메서드
def choice_burger():
    print('000000000000000000000000000000000000000000000')
    print('00 BURGER MENU')
    print('00 1. 불고기 버거 : 3000원')
    print('00 2. 치킨 버거 : 3500원')
    print('00 3. 치즈 버거 : 3500원')
    print('000000000000000000000000000000000000000000000')
    print('00 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num = int(input('>>번호:'))
        if choice_num >= 1 and choice_num <= 3:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')
    return choice_num

# 2. 사이드 단품메뉴 선택하는 메서드
def choice_side():
    print('0000000000000000000000000000000000000000000')
    print('00 SIDE MENU')
    print('00 1. 감자튀김 : 1500원')
    print('00 2. 치킨너겟 : 2000원')
    print('00 원하시는 메뉴의 번호를 입력해주세요')
    print('0000000000000000000000000000000000000000000')
    while True:
        choice_num2 = int(input('>>번호:'))
        if choice_num2 >= 1 and choice_num2 <= 2:
            break
        else:
            print('# MSG: 1~2의 번호만 입력해주세요:)')
    return choice_num2


# 3. 으료 단품 메뉴 선택하는 메서드
def choice_drink():
    print('00000000000000000000000000000000000000000000')
    print('00 DRINK MENU')
    print('00 1. 코카콜라 : 1000원')
    print('00 2. 커피 : 1000원')
    print('00 3. 주스 : 1500원')
    print('원하시는 메뉴의 번호를 입력해주세요')
    print('00000000000000000000000000000000000000000000')

    while True:
        choice_num3 = int(input('>> 번호:'))
        if choice_num3 >= 1 and choice_num3 <= 3:
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요:)')
    return choice_num3
