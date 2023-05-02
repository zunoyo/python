#0502 함수
#input 을 주면 output을 주는 것

'''
input - 숫자  -num1
output = 숫자 -output+num
이런 기능을 하는 function - multi
'''
#함수정의
def multi(num1) :
    output_num = num1 * 3
    return output_num

#정의한 함수 호출 
print(multi(3))


#hello,  input - 사람이름 두개 입력,  output  - 안녕 1번사람, 안녕 2번사람  함수 내에서 출력

def hello (n1="나나",n2="너너") :   #이렇게 기본값 지정 가능 호출 시 파라메터 입력 없으면 기본 값 출력 - n1 = "나나"
    print("안녕, ",n1)
    print("안녕, ",n2)


hello("김준호","홍길동")




#두개의 숫자를 입력받아 두개의 합을 함수 내에서 출력

def sum(a1,a2) :
    y = a1+a2
    print("두 수의 합", y)
   
sum(3,4)

def sum2(a1,a2) :
    return a1+a2

print(sum2(100,200))
