#range
# python 內建功能:清單產生器
import random
r = random.randint(1, 1000) #產生隨機的整數1至100
count = 0
while True:
	count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜對了!嘺孟芩我愛你!')
		break
	elif num < r :
		print('再猜大一點')
	elif num > r :
		print ('再猜小一點')


	print('加油!這是你猜的第', count , '次產生隨機數 ')

