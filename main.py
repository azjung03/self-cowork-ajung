
import  random

# 충돌이 났었는데요, 다음과 같이 수정했어요
print("로또번호다섯개추첨합시다 !^^")

for i in range(5) :
	lotto = random.sample(range(1,46),6)
	print(lotto)
