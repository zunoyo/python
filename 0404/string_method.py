'''string 메소드'''


str="파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 "

print('{}+{}={}'.format(2,3,5))


a,b=5,10.000
print('{}+{}={}'.format(a,b,a+b))
print('{0}+{1}={2}'.format(a,b,a+b)) #숫자들이 변수들의 위치
print('{2}+{0}={1}'.format(a,b,a+b))  
print('{0:d}+{1:f}={2:f}'.format(a,b,a+b))  
print('{0:d}+{1:f}={2:f},{3:s}'.format(a,b,a+b,"oioioioi"))  


'''
print(str.split())
'''

'''
print(str.find("파이썬"))
print(str.find("파"))
print(str.find("썬"))
print(str.find("썬"))
print(str.index("썬"))
print(str.find("자바")) #str.find는 값이 없으면 -1 출력
print(str.index("자바")) #str.index는 값이 없으면 오류 출력
'''


'''
newstr=str.replace("파이썬","자바")
print("str: " ,str)
print("newstr: " ,newstr)

print('str.count("파이썬"): ',str.count("파이썬"))

print('^'.join(str))
'''
