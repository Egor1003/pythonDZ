#Ввод данных
n = int(input('input n  '))
num=[]
#Заполнение списка
for i in range (n+1):
	num.append(i)
num[1]=0
i=2
#Обработка списка
while i<=n:
	if num[i]!=0:
		j=i+i
		while j<=n:
			num[j]=0
			j=j+i
	i+=1
#Преобразование списка и его вывод
num = set(num)
num.remove(0)
print(num)