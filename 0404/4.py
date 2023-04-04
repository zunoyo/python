# countinue, break
# 반복문 안쪽에서 실행
# 주로 if문 안쪽에서 사용됨



#input  으로 입력 받는다
#무한반복
#exit라는 값을 받으면 입력받는 것을 종료
#apple을 입력받으면, '넌 이 단어를 입력했다' 출력하지 않기


#위 문제의 답 
'''

while True :
    str=input("단어를 넣으세요   ")
    if str=="exit":
        print("넌 exit를 입력했다 . 종료한다.")
        break
    else:
        if str=="apple":
            print("apple을 입력 받았음")
            print("countinue 실행함")
            continue
        print("넌 이 단어를 입력했다 : ", str)
    
    print( str,"저는 아직 while 안에 있어요")

print("while문이 정상적으로 종료됨")

'''

#내주신 문제임 **

#input  으로 입력 받는다
#무한반복
#exit라는 값을 받으면 입력받는 것을 종료
#apple을 입력받으면, 'apple을 입력했다' 하고 다시 입력받기 
#그 외의 단어를 입력받으면 해당 단어를 3번 찍어줄것
#countinue,break를 활용해서 해보기


while True:
    str = input("입력하세요")
    if str=="exit":
        print("프로그램 종료")
        break
    else :
        if(str=="apple"):
            print("apple을 입력했다")
            continue
        else:
            print(str,str,str)

print("while문 정상 종료")
#이 코드 맞음 ? 
        


