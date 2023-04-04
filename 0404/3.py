#반복문


'''
for i in 1,3,4,5,6,8 :
    print(i)

print("range1")
for i in range(0,11,2) :
    print(i)

print("range2")
for i in range(11) :
    print(i)

'''

'''
#1부터 10까지 합을 구하시오
sum=0
for i in range(11) :
    sum = sum + i
    print(i,"번째 sum은 ",sum)
else: #for-else에서 else문은 정상종료시에만 출력됨
    print("for문의 조건이 더이상 만족하지 않습니다.")
    print("i가 range(11)에서 벗어남.")
    print("for문이 break나 countinue로 종료된게 아니라 정상 종료시에만 실행")

print("sum: ",sum)
'''

#while 조건 :
       #수행문


'''
i=10
while i>5 :
    print(i," 은 5보다 크다.")
    i=i-1

# n=1 부터 5까지 찍어보는 프로그래밍
# 1 2 3 4 5 
i=1
while i<=5 :
    print(i,end = '   **   ')
    i=i+1
else :
    print("while이 잘 끝났습니다. 현재 i의 값은 ",i,"입니다")

    '''


#놀이기구 탑승
#4명 탑승 가능, 5명은 안돼요
#키 150이상만 탑승 가능
#입력을 키를 받음
#탑승인원 체크, 키 체크
#while문을 끝내는 조건은? 사람을 4명 채웠는가?


'''
while 5명이 아닐것 :
    
    키를 물어본다.
    150이 넘는가?
    -yes:
    -no:
else:
    4명 다 탔음. 놀이기구 출발

    '''


people =0
max_people=4
while people<4:
    height=input("키는?")
    int_height=int(height)
    if int_height>=150:
        print("한명탑승")
        print("현재인원:",people+1)

        people=people+1
    else:
        print("탑승 불가능")    
else:
    print("모두 탑승 완료. 출발합니다.")





    



 
