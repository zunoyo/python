#dictionary

#key:value
#1001:"홍길동", 1002:"김길동" 
d1 = {1001:"홍길동", 1002:"김길동" ,1003:"박길동"}
print(d1[1001])
print(d1[1003])
# print(d1[0]) #이런 키 값은 존재하지 않기 때문에 에러 남 키 값을 넣어야함 

#d2 = {}
d2 = dict()
d2['강좌명'] = '파이썬' #문자열넣기
d2['개설요일'] = '화요일'
d2["년도"] = 2023 #숫자 넣기 
d2['수강생'] = ['김','이','박'] #리스트 값 넣기 
print("d2:",d2)
print(d2['수강생'])
print(len(d2)) #key:vlaue 를 하나로 취급 

#dictionary key:value 1:1월, 2:2월 ... 12:12월
#for문 돌려서 각각의 value 값을 찍어라

month = {1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',7:'7월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}

#방법 1) key값이 숫자인것을 활용
for i in range(1,13): #1,2,3,4,5....12
    print(month[i])


#dictionary method

print('month.keys:', month.keys())     #리스트 형태 값으로 반환
print('month.values:', month.values()) #리스트 형태 값으로 반환
print('month.items:', month.items())   #리스트 형태 값으로 반환

#방법 2)  month.key() 활용
for i in month.keys() : #[1,2,3.4,5...12] 리턴
    print('i:',i)
    print(month[i])

print()

#방법 3) month.values() 활용
for i in month.values():  #1월,2월...12월 리턴 
    print(i)


#방법 4) month.items() 활용
print(month.items())
print('item 활용')
for i in month.items():  #item - (1,'1월')  -왜 이거 안 되지 ?
   print(i[1])  #i[0]-key 값 , i[1] - value값 


#방법 5)  month.items() 활용
for k,v in month.items():  #k = key , v = value
    print(k)
    print(v)

# 방법 6) month.keys() month
# month = {1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',7:'7월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}
for i in month:  #key들이 리턴  #month.keys()
    print(i)
    print(month[i]) #value 값 리턴


print('month.pop(0):', month.pop(1)) #key에 있는 아이템 제거 ()안에 index값이 아닌  key값을  써야함
print(month)
print('month.popitem():', month.popitem()) #제일 마지막 item 을 제거 
print(month)
 
month.update({3:'march'}) #값 수정 
print(month)
month.update({15:'15월'}) #없던 값 추가도 가능 , 있던 값은 수정 
print(month)


#dictionary - tuple - list 변환
#tuple - 변경불가, 수정불가  (아메,핫초코,라떼)
#tuple -> list 유자차 추가  - > tuple로 다시 변경
#list -> tuple 수강신청 전 수강생 변경, -> tuple
#tuple , list => dictionary (1,2,3,4) , (홍,김,박,이)

seql = ['a','b','c','d'] #list
seqt = tuple(seql) #list를 tuple로 바꾼 과정
print(seqt)
print(type(seqt))

seql2 = list(seqt) #tuple을 다시 list로 변경 
print(seql2)
print(type(seql2))

seqd = dict(enumerate(seql))  
print(seqd)
print(type(seqd))



