ed={1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',9: 'девять', 0: 'ноль'}
des={2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
desed={10: 'десять', 11: 'одиннацать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
while True:
	try:
		a=int(input('Введите число:  '))
		if a//10==0:
			print(ed[a%10])
		if a//10==1:
			print(desed[a])
		if a//10>1:
			if a%10==0:
				print(des[a//10])
			else:
				 print(des[a//10], ed[a%10])
	except ValueError:
		print('Вы ввели не число!')