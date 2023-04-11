#0411
#리스트 ,튜플, 딕셔너리, 집합

#리스트 []  ['김','이','박','최']
#튜플 ()    ('김','이','박','최')  
#딕셔너리 -> 사전     {key:value,k1:vq,k2:v2....} {'홍길동':'서울','김길동':'부천'}   

address = {'홍길동':'서울','김길동':'부천','james':'미국'}
print(address['홍길동'])

#숫자,int,float,string 다 가능함
lst = [10,20,30,40,50]
print(type(lst))
print(lst[0]," ",lst[1],lst[len(lst)-1])

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
list2 = list1[2:6:3] #iot , java

list3=[1,2,3,4,5,6,7]
list3[1:2]=list2 #list 2,3 에 list2를 넣는다
print(list3)

list3[1]=list2
print(list3)





#튜플은 수정 불가 , 리스트는 수정 가능
#수정불가 -> append,insert,값 변경 불가능




#list insert
food=[]
food.append("짜장면")
food.append("샌드위치")
print(food)
food.insert(0,"파스타")
print(food)
food.insert(2,"파스타")
print(food)
food.insert(2,"제육")
print(food)


'''
food.remove("제육")
print(food)
food.remove("짜장면")
print(food)
food.remove("파스타")
print(food)
food.remove("파스타")
print(food)
food.remove("샌드위치")
print(food)
'''


print("food pop : ", food.pop())
print(food)
print("food pop : ", food.pop())
print(food)

#extend
print(food)
dessert=["커피","케잌","와플"]

food_list = food + dessert
print(food_list)

food.extend(dessert) #food + dessert 
print(food)

food.reverse() #역방향으로 출력 
print(food)

#food.clear() #리스트의 인덱스 싹다 지우기
#del food #del  메모리에서 food 를 지움(메모리에서 삭제) 출력하면 정의되지 않았다고 뜬다
#print(food)

'''
a="1"
print(type(a)) #str
print(int(a)+5) # -> 6  여기서만 잠깐 a가 1 이지 계속 int 형식이 아니고 str임
print(type(a))
'''

#정렬
#sort() 순서대로
#sorted()
l1=["banana","apple","orange","mango"]
print(l1)
print("sorted(l1): ",sorted(l1))
print("li        :", l1)
l1.sort()
print(l1)


#리스트 컴프리헨션
#0부터 10까지 있는 list를 만들자

#1)
l3=[0,1,2,3,4,5,6,7,8,9,10]
print(l3)

#2)
l3=[]
for i in range(11):
    l3.append(i)
print(l3)

#3) 리스트 컴프리헨션 (중요)
#리스트 변수명 = [i for i in range()]
l3 = [i for i in range(11)]
print(l3)



# 10)
#리스트 컴프리헨션으로 0~10까지의 숫자의 제곱을 원소로 가지는 리스트 작성
#i**2 제곱 표현
#[0,1,4,9,16.....100]

#반복문 사용
l4 = []
for i in range(11):
    l4.append(i**2)
print(l4)    

#리스트 컴프리헨션
l5 = [i**2 for i in range(11)]
print(l5) 



#11) 0~10까지의 숫자의 3배를 원소로 가지는 리스트 작성
l6 = [i*3 for i in range(11)]
print(l6) 




#12)"hello" 를 1개 가지는 리스트 작성
l7 = ['hello' for i in range(10)]
print(l7)

l8 = []
for i in range(10):
    l8.append("hello")
print(l8)    


#0~10까지의 숫자의 제곱을 리스트로 만들어라
#짝수의 제곱만 넣어라
# [0,4,16....100]

# for 
l9 = []
for i in range(11):
    if i%2==0:
        l9.append(i**2)
print(l9)    

#리스트 컨프리헨션
l10 = [ i**2 for i in range(11) if i%2==0 ]
print(l10)


#**중요**
# 얕은 복사 , 깊은 복사 
# 얕은 복사는 하나의 값이 변하면 그 주소를 사용하는 다른 변수도 변하지만 깊은 복사는 새로운 주소를 받아 영향을 받지 않는다

#shallow copy
print("food : ", food)
wishlist = food
print("wishlis : ",wishlist)

food.pop() #파스타 빠짐
print("after pop-- ")
print("food :",food)
print("wishlist : ",wishlist)

print(food is wishlist) #같으면 true 다르면 false


#deep copy
food2 = food[:] #food 를 물려받음 deep copy 하는 방법 1
food3 = list(food) #deep copy 하는 방법 2

print("deep copy")
print("food : ",food)
print("food2 : ",food2)
print(food is food2) #false  두 변수가 같은지 식별하는 함수 
food2.append("김밥")
print("food : ",food)
print("food2 : ",food2)
food.append("라볶이")
print("food : ",food)
print("wishlis : ",wishlist)
print("food2 : ",food2) #food , wishlist와 따로 논다 메모리가 다름 

print(food3)