l=[]
n=int(input("Enter the limit :"))
print("enter numbers:")
for i in range(0,n):
	x=int(input())
	if (x<100):
		l.append("over")
	else:
		l.append(x)
		print(l)
