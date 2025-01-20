
# 자료형 - 튜플
# 리스트는 [], 튜플은 ()로 둘러싼다
# 리스트는 요소값의 생성, 삭제, 수정이 가능하지만
# 튜플은 요소값을 수정할 수 없다!

# 튜플 생성 방법
t1 = ()
t2 = (1,) 
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# 생성시 주의할 점
# 1) t2와 같이 1개의 요소만을 가지는 경우 끝에 쉼표 (,)를 꼭 붙여야 한다.
# 2) t4와 같이 소괄호를 생략해서 작성해도 가능하다.

# 리스트와의 큰 차이점은 요소값을 변화시킬 수 있는지의 여부
# 값이 바뀌는 걸 원하지 않는다면, 리스트가 아닌 튜플을 사용해야 함
# But, 실제로는 값이 바뀌는 형태의 변수가 훨씬 많기 때문에 실제로는 리스트를 더 많이 사용

# 1. 튜플의 요소값 삭제 / 수정
# 1-1) 튜플 요소값 삭제시
t1 = (1, 2, 'a', 'b')
# del t1[0]   # TypeError: 'tuple' object doesn't support item deletion

# 1-2) 튜플 요소값 수정시
t1 = (1, 2, 'a', 'b')
# t1[0] = 'c'
# print(t1)   # TypeError: 'tuple' object does not support item assignment

# 2. 튜플 사용하기
# 2-1) 튜플 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])    # 1
print(t1[3])    # 'b'

# 2-2) 튜플 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[:3])   # 1, 2, 'a'
print(t1[1:])   # 2, 'a' 'b'

# 2-3) 튜플 더하기
# 튜플의 요소값이 변경되는 것이 아니고, t3라는 새로운 튜플을 생성한 것
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)       # (1, 2, 'a', 'b', 3, 4)

# 2-4) 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
print(len(t1))  # 4

# ** 튜플은 요소값을 변경할 수 없기 때문에
# sort, insert, remove, pop 같은 내장함수가 존재하지 않음

'''
Q. (1, 2, 3)이라는 튜플에 값 4를 추가하여 (1, 2, 3, 4)라는 새로운 튜플을 출력
'''
# 내가 작성한 답
t1 = (1, 2, 3)
t2 = (4,)
t3 = t1 + t2
print("result : ", t3)  # (1, 2, 3, 4)

# 문제 답
a = (1, 2, 3)
print(a + (4, ))        # (1, 2, 3, 4)