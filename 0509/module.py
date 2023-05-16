import sys
print(sys.builtin_module_names)
sys.path

import numpy as np  #이런 모듈들은 설치를 해줘야함 sys는 기본 탑재 되어있음  , as로 별명 설정 가능 
#pip install numpy 설치 명령어 (터미널에 입력)

arrA = np.array([1,2,3,4,5]) #원래 nmpy.array인데 별명 설정으로 np.array로 쓴거임 
arrB = np.array([6,7,8,9,10])
print(type(np.array([1,2,3,4,5])))

print(arrA+arrB) #원소 전체가 합쳐지는게 아닌 같은 위치의 원소 값들끼리 더한다 
print(arrA-arrB)
print(arrA*arrB)
print(arrA/arrB)

np.array


#####################################################################################################

import math
from math import gcd #이렇게 쓰면 math.gcd 에서 'math.'을 안 써도 됨
print(math.fsum([1,2,3])) # 리스트의 값을 더해 float값으로 리턴하는 
print(math.gcd(80,56)) #최대 공약수를 구하는 

print(math.ceil(1.19))

import hello as h

print(h.hello())
print("__name__ in module.py   :",__name__)

import zuno 



# https://github.com/dongmisw/python_programming 교수님 git