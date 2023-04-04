#제어문
'''
value = True 

print(type(value))
print(int(value)) #ture 는 1 false는 0으로 반환

print(bool(0),bool(1),bool(1.1222),bool(-12)) # false true true true
print(bool("dddddddd"),bool("-1"),bool("")) #  true true false

if 조건 :
        실행문 1
else:
    실행문2
'''

'''
hour=13
if hour<12 :
    print("12시가 지나지 않았으니 오전입니다.")
elif hour<18 :  
    print("12시가 지나고 18시가 지나지 않았으니 오후입니다.")
else :
    print("18시가 지났으니 저녁입니다.")    
    '''

'''
score=input("점수는?")
score2=int(score)

if score2 < 200 :
    print("50만원 획득")
elif score2 < 400 :
    print("100만원 획득")        
else : 
    print("1000만원 획득")
    '''


#점심식사
answer = input("서브웨이 먹을래?  먹고싶으면 yes를 쓰시오")
if answer=='yes' :
    print("8호관 1층")
else :
    again_answer = input("학식?")    
    if again_answer =='yes' :
        print("8호관 3층")
    else :
        print("먹지마세요")
      