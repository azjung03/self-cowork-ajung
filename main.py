
import  random

print("로또번호다섯개!!")

for i in range(5) :
	lotto = random.sample(range(1,46),6)
	print(lotto)
