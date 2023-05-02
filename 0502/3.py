#인자의 갯수가 여러개인 경우 

def hello(*names) :  #   * 로 인자의 갯수 여러개 가능 
    #안녕 찍기 
    for i in names:
        print("hello", i) #hello 홍길동 

hello("홍길동","김준호","나나") # 이렇게 여러개 인자 가능


print()


#몇개의 숫자를 받던지 합을 구하는 함수

def sum(*nums) :
    result = 0
    for i in nums:
        result = result + i
    return result     

print("합", sum(1,2,3,4,5,6,7,8,9,10) )


list = [1,2,3,4,5,6,7,8,9,10]
print("리스트의 합",sum(*list)) #리스트 활용 

print()
#dict{key1:vlaue1}
#딕셔너리는 ** 써준다

coffee = {"아아":2000,"라떼":3000,"아이스초코":4000}

def printmenu(**keyvalue):
    for i in keyvalue :  #이렇게만 쓰면 키 값 리턴 
        print(i,keyvalue[i])

printmenu(**coffee)
print()
printmenu(아아=2000, 라떼=3000,티=3000,핫도그=5000)   #직접 key와 value값을 써줘도 된다. 써준대로 출력 가능 

print()

#위 리스트와 딕셔너리를 섞어서 활용한 예제 --이해하기 중요할듯 
def func1(*num,**menu):
    #num들의 합
    result = 0
    for i in num:
        result = result + i
    print(result)

    #menu를 출력
    for num in  menu :  #이렇게만 쓰면 키 값 리턴 
        print(num,menu[num])

list = [1,2,3,4,5,6,7,8,9,10]
coffee = {"아아":2000,"라떼":3000,"아이스초코":4000}
func1(1,2,3,4,5,6,7,8, 아아=1000,티=3000,초코=4000)
print()
func1(*list,**coffee)
print()
func1(1,2,3,4,5,6,7,8, **coffee)
