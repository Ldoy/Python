# for문 공부하기

python_list = [1, 2, 3, 4, 5]

for number in python_list:
    print(number)

for number in python_list:
    print('치킨', number, '마리')

# for 변수 in 문자열:

for character in '푸라닭치킨맛있다':
    print(character,'👏')

# 들여쓰기

for character in '푸라닭치킨맛있다':
    print(character,'👏')
    print('🍗')

for character in '푸라닭치킨맛있다':
    print(character,'👏')
print('🍗')

# 순서열 만들기 range(끝_값+1)
for num in range(3):
    print(num)

for num in range(1, 5):
  print(num)

# 퀴즈 

roses = ['하얀장미', '하얀장미','하얀장미']
for i in range(3):
  roses[i] = '빨간장미'
print(roses)

# chapter5

# if, elif
if python_list.count == 5:
  print("참!")
else:
  print("거짓")

chicken = 'puradak'
if chicken == 'GoopNe':
  print('치킨은 굽네치킨~')
elif chicken == 'NoRang':
  print('추억의노랑치킨')
else:
  print('역시 치킨은 푸라닥')

total_price = 0
over_20 = 8000
between_10_19 = 5000
under_9 = 2500
ages = [22, 21, 17, 32, 4, 28, 19, 8]
for age in ages:
  if age <= 9:
    total_price += 2500
  elif age >= 20:
    total_price += 8000
  else:
    total_price += 5000

print(total_price)

# and, or, not, 
# while

num = 0
while num < 3:
  print('치킨', num, '마리')
  num = num + 1

# input(), 항상 문자열로 입력을 받음
name = input('이름뭐야?')
print(name, '안녕')

city_name = ''
while city_name != '런던':
  city_name = input('영국의 수도는?')
print('정답입니다!')

