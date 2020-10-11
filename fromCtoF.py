# ввод температуры
temp = input('input temperature ')

# проверка корректности ввода 
if len(temp)==0 or len(temp)==1 or (len(temp)==2 and "-" in temp):
	print('invalid input')
	exit(1)
	
# перевод из строки в число
degree = float(temp[:-1])

# перевод из Цельсий в Фаренгейты
if "C" in temp:
	degree = degree*1.8+32
	print("%.1f" % degree,"F")
	exit(3)

# перевод из Фаренгейта в Цельсии
elif "F" in temp:
	degree = (degree-32)/1.8
	print("%.1f" % degree,"C")
	exit(4)
	
# проверка ввода шкалы измерения	
elif "C" or "F" not in temp:
	print('invalid input')
	exit(5)