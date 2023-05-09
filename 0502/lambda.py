#lambda fucntino
#function 을 만드는데 이름짓기가 귀찮다 , 실행문이 하나밖에 없다

# 형식:  lambda parameter_name : parameter로 실행문 

print((lambda x : x+1)(100)) #이렇게 사용 가능 

print((lambda x,y: x+y)(100,200))


#map , filter 
#lsit가 존재할 때 

#map(함수, input 리스트 )
#map(addone, list)

list1=[1,2,4,5,6,7,8,9,10]
print(list(map(lambda x : x+1,list1)))

list1=[1,2,4,5,6,7]
list2=[1,2,4,5,6,7]
#result = [2,4,6,8,10,12,14]
print(list(map(lambda x,y: x+y,list1,list2)))




