# 讓使用者輸入年齡、國家，並讓他知道可不可以開車
age = input('請輸入年齡: ')
age = int(age)
country = input('請輸入你的國家: ')

if country == '台灣':
	if age >= 18:
		print('可以開車')
	else:
		print('不可以開車')
elif country == '美國':
	if age >= 16:
		print('可以開車')
	else:
		print('不可以開車')