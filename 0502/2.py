#지역변수, 전역변수

'''
num =100 #전역변수  global variable 

def addone() :
     num = 10 #
     print("addone(): ",num+1) #-> 11   
     print("addone() num: ",num) #-> 10
     num = num +20
     return num

result = addone() #함수 내에서 선언한 변수를 가져오기 리턴을 해주면 됨 
print(result)

print("*** num : ",num)  #전역변수  num = 100
'''




#) 내부 function에서 전역변수를 사용하면 좋겠고 수정도 하고 , function이 끝나도 그 값이 반영 되었으면 좋겠다

num =100 #전역변수  global variable 

def addone() :
     global num  #num은 전역변수를 사용한다  
     #num = 3 - 이렇게 쓰면 전역변수를 쓴다고 선언해도 이 3 값을 쓰게 됨 
     print("addone(): ",num+1) #-> 11   
     print("addone() num: ",num) #-> 10
     num = num +20
     return num

result = addone() #함수 내에서 선언한 변수를 가져오기 리턴을 해주면 됨 
print(result)

print("*** num : ",num)  #전역변수  num = 100


