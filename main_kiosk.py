###########################################################
## CNU 버거 키오스크 프로그램
## 일지 : 2021. 10. 12
## 작성자 : 김수연
## 내용 : Console 기반의 햄버거를 판매하는 키오스크 프로그램

# 조건
# 사용자는 최대로 버거 1개, 사이드 1개, 음료 1개 주문할 수 있습니다.

# 메뉴와 가격표
burger_name = {1: '불고기버거', 2: '치킨버거', 3: '치즈버거', 4: '새우버거'}
side_name = {1: '감자튀김', 2: '치킨너겟'}
drink_name = {1: '코카콜라', 2: '커피', 3: '주스' }

burger_price = {1: 3000, 2: 3500, 3: 3500, 4: 3500 }
side_price = {1: 1500, 2: 2000}
drink_price = {1: 1000, 2: 1200, 3: 1500}

# 고객 주문 기록 저장
menu_save = {}  # 고객 주문 메뉴 기록
price_save = {} # 고객 주문 금액 기록

######################
## 1 . 메인 메뉴 선택 ##
#####################
print('00000000000000000000000000000000000000000000000000000000000000000')
print('00== CNU 버거(ver.01)==00')
print('CNU 버거에 방문해주셔서 감사합니다.')
print('00000000000000000000000000000000000000000000000000000000000000000')
print('00 메뉴')
print('00 1.햄버거 세트')
print('00 2.햄버거 단품')
print('00 3.사이드 메뉴')
print('00 4.음료')
print('00000000000000000000000000000000000000000000000000000000000000000')

while True:
    print('00 원하시는 메뉴의 번호를 입력해주세요.')
    menu_num =int(input('>> 번호:')) # 사용자로부터 주문 MENU 입력
    if menu_num >= 1 and menu_num <= 4:
        break
    else:
        print('# MSG: 1~4의 번호만 입력해주세요 :)')
####################
## 2. 세부메뉴 선택 ##
####################

if menu_num == 1:      # 햄버거 세트
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
            menu_save['burger'] = burger_name[choice_num]
            price_save['burger'] = burger_price[choice_num]
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요 :)')

    print('0000000000000000000000000000000000000000000')
    print('00 SIDE MENU')
    print('00 1. 감자튀김 : 1500원')
    print('00 2. 치킨너겟 : 2000원')
    print('00 원하시는 메뉴의 번호를 입력해주세요')
    print('0000000000000000000000000000000000000000000')
    while True:
        choice_num2 = int(input('>>번호:'))
        if choice_num2 >= 1 and choice_num2 <= 2:
            menu_save['side'] = side_name[choice_num2]
            price_save['side'] = side_price[choice_num2]
            break
        else:
            print('# MSG: 1~2의 번호만 입력해주세요:)')

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
            menu_save['drink'] = drink_name[choice_num3]
            price_save['drink'] = drink_price[choice_num3]
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요:)')
elif menu_num == 2:    # 햄버거 단품
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
elif menu_num == 3:    # 사이드 메뉴
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('00 SIDE MENU')
    print('00 1. 감자튀김 : 1500원')
    print('00 2. 치킨너겟 : 2000원')
    print('00 원하시는 메뉴의 번호를 입력해주세요')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    while True:
        choice_num2 = int(input('>>번호:'))
        if choice_num2 >= 1 and choice_num2 <= 2:
            menu_save['side'] = side_name[choice_num2]
            price_save['side'] = side_price[choice_num2]
            break
        else:
            print('# MSG: 1~2의 번호만 입력해주세요:)')
elif menu_num == 4:    # 음료
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('00 DRINK MENU')
    print('00 1. 코카콜라 : 1000원')
    print('00 2. 커피 : 1000원')
    print('00 3. 주스 : 1500원')
    print('원하시는 메뉴의 번호를 입력해주세요')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

    while True:
        choice_num3 = int(input('>> 번호:'))
        if choice_num3 >= 1 and choice_num3 <= 3:
            menu_save['drink'] = drink_name[choice_num3]
            price_save['drink'] = drink_price[choice_num3]
            break
        else:
            print('# MSG: 1~3의 번호만 입력해주세요:)')

##############################
## 주문 메뉴와 금액 정산 및 출력 ##
##############################

# Total 주문 금액 계산
total_price = 0 # Total 주문 금액

print('메뉴 저장: ', menu_save)
print('가격 지정:', price_save)

for price in price_save.values():
    total_price += price

print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('00 고객님이 주문하신 메뉴는')
for i, menu in enumerate(menu_save.values()):
    print('□■ {}. {}'.format(i+1, menu))
print('■■ 으로 총 주문금액은 {}원 입니다.'.format(total_price))
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('00 이용해주셔서 감사합니다. 또 방문해주세요 :D')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
