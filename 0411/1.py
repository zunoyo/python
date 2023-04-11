#0411
#리스트 ,튜플, 딕셔너리, 집합

#리스트 []  ['김','이','박','최']
#튜플 ()    ('김','이','박','최')  
#딕셔너리 -> 사전     {key:value,k1:vq,k2:v2....} {'홍길동':'서울','김길동':'부천'}   
address = {'홍길동':'서울','김길동':'부천','james':'미국'}
print(address['홍길동'])

#숫자,int,float,string 다 가능함
list = [10,20,30,40,50]
print(type(list))
print(list[0]," ",list[1],list[len(list)-1])

#빈 리스트 생성 ->  하나씩 원소를 추가
list1=[]
#list2 = list()
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("python")
list1.append("java")
list1.append("c++")
print(list1)
print(list1[0])


print("---------for 1---------")
for i in range(len(list1)):
    print(list1[i])

print("---------for 2---------")
for i in list1:
    print(i)

print(list1)
print("count : ",list1.count("python"))
print("index : ",list1.index("python"))
#"hahaha".index("a")

#list 수정
list1[0]="ai"
list1[2]="iot"
print(list1)

#슬라이싱

list2=list1[0:3:1] #0~2
print(list2)
list2=list1[1:5:1] #1~5
print(list2)
list2=list1[1:len(list1):2] #1~6    2칸씩 이니까 --  1,3,5
print(list2)
list2=list1[2:6:3] #2~5   3칸씩 이니까 -- 2,5
print(list2)
list2=list1[::-1] #시험에 나옴 -1 사용한거  - 역순으로 출력
print(list2)

print("-------list1--------")
print(list1)


#list1 , list3
#list1의 일부를 list3에 대입
list2 = list1[2:6:3] #iot java

list3=[1,2,3,4,5,6,7]
list3[1:2]=list2 #list 2,3 에 list2를 넣는다
print(list3)

list3[1]=list2
print(list3)





#튜플은 수정 불가 , 리스트는 수정 가능
#수정불가 -> append,insert,값 변경 불가능
