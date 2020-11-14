def parabola(x):
	return(x**2)
def line(x):
	return(2*x)
def coob(x):
	return(x**3)
	
def extremum(a,b,*,func,**kwargs):
	min=func(a)
	max=func(a)
	for i in range(-100,101):
		if func(i)<=min:
			min=func(i)
			xmin=i
		elif func(i)>=max:
			max=func(i)
			xmax=i
	if not a<=xmin<=b:
		min=None
	if not a<=xmax<=b:
		max=None
	f="minimum = {}".format(min)
	g="maximum = {}".format(max)
	return f,g

result=extremum(-2,2, func=parabola)
for k in result:
	print(k)
print('')
result=extremum(-2,2, func=line)
for k in result:
	print(k)
print('')
result=extremum(-10,10, func=coob)
for k in result:
	print(k)