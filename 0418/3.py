#zip
# list , tuple 이 여러개 -> 하나의 튜플의 조합으로 된 리스트로. 
l1 = ['1조','2조','3조']
YA = ['홍','김','이']
YB = ['최','한','공']

z = zip(l1,YA,YB)
print(type(z))
print(z)
print(list(z))
print(tuple(zip(l1,YA,YB)))


l10 = ['한식','양식','중식','분식']
l11 = ['전주식당','닥터로빈','전가복','토마토']
l12 = ['제육','파스타','탕짜면','김밥']

print(list(zip(l10,l11,l12)))


#for i in range(4):    양이 많아지면 이렇게 쓰기 어렵기때문에 zip 사용
#   print(l10[i],l11[i],l12[i])

l100 = zip('abcd',l10,l11,l12)
for i  in l100:
    print(i[0],i[1],i[2],i[3])

'''
l10 = ['한식','양식']#'중식','분식']
l11 = ['전주식당','닥터로빈','전가복','토마토']
l12 = ['제육','파스타','탕짜면']# ,'김밥']
print(list(zip(l11,l10,l12)))   #이렇게 값들이 갯수가 다르면 알아서 짧은 값에 맞춰서 출력
'''


l10 = ['한식','양식','중식','분식']
l11 = ['전주식당','닥터로빈','전가복','토마토']
l12 = ['제육','파스타','탕짜면','김밥']

#dictionary

print(list(zip(l10,l11)))
print(dict(zip(l10,l11)))
# print(dict(zip(l10,l11,l12))) #오류 남 dictionary는 key:vlaue로써 값이 2개뿐이기 때문 현재 이건 값이 3개임 
print(dict(zip(l10,zip(l11,l12)))) #이렇게 뒤 2개의 값을 zip로 묶어주면 가능함 


#       0           1        2        3 
l11 = ['전주식당','닥터로빈','전가복','토마토']

print(list(enumerate(l11))) # enumerate - 앞에 숫자를 붙여줌 0부터 
print(dict(enumerate(l11)))  



ll1 = ['파이썬','자바','알고리즘','데이터베이스','iot']
ll2 = ['101','102','103','104','105']
#dictionary로 만든다 
#for ,while 
#quit이 들어올때까지 계속 받는다 
#input() -> 강의명 입력
#강의실을 알려줌 


print(dict(zip(ll1,ll2)))

to=dict(zip(ll1,ll2)) #{'파이썬':101,'자바':102.....}

while True:
    c = input("강의명을 쓰시오")
    if c =='quit' :
        print('quit 입력이니 종료.')
        break
    else:
        if c in to.keys():
             print(to[c])
        else:
            continue
         
