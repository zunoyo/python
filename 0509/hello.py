
# 나만의 module 만들기 여기서 만들어서 module.py에서 사용하는 실습 
def hello() :
    print("hello")

if __name__ == "__main__" :
    print("__name__ :", __name__)
    print("오늘은  module 처음 배운 날")
    print("오늘 날씨는 더움 ")
    hello()

print("hello.py __name__ :", __name__)