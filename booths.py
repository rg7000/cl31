bits = 32
length = 2*bits + 1
def dec_to_bin(num):
    b = [0 for i in range(bits)]
    print("in dec to bin, num is: ", num)
    i = bits - 1
    while i >= 0 and num != 0:
        b[i] = num%2
        print("b[i]", b[i])
        num = num / 2
        i -= 1
    return b

def add_bin(a, b):
    #to add 2 numbers of length = length
    i = length - 1
    sum = [0 for i in range(length)]
    temp = 0
    c = 0
    while i>=0:
        temp = a[i] + b[i] + c
        sum[i] = temp % 2
        c = temp / 2
        i -= 1
    return sum

def bin_to_dec(b):
    i = len(b) - 1
    j = 0
    temp = 0
    while i >= 0:
        temp += b[i] * pow(2, j)
        j += 1
        i -= 1
    if temp > (pow(2, bits) - 1):
        temp = -(pow(2, length) - temp)
    return temp

'''def bin_to_dec(num):
	neg=0
	if num[0]==1:
		neg=1
		x=length-2 #15
		while(x>=1):
			if(num[x]==0):
				x=x-1
			else:
				break
		for i in range(0,x):
			num[i]=1-num[i]
	ans=0
	temp=0
	i=length-2 #15
	while(i>=0):
		if(num[i]==1):
			ans=ans+pow(2,temp)
		temp=temp+1
		i=i-1
	if neg:
		return -ans
	return ans'''

def right_shift(a):
    i = len(a) - 1
    while i >= 1:
        a[i] = a[i-1]
        i -= 1
    return a

def booths(num1,num2):
    m = dec_to_bin(num1)
    q = dec_to_bin(num2)
    x = dec_to_bin(-num1)
    print(m, q, x)

    P = [0 for i in range(bits)]
    for i in range(bits):
        P.append(q[i])
    P.append(0)
    print(P)
    A = [0 for i in range(length)]
    S = [0 for i in range(length)]
    for i in range(bits):
        A[i] = m[i]
        S[i] = x[i]

    for i in range(bits):
        if(P[-2] == 0 and P[-1] == 1):
            P = add_bin(P,A)
        elif(P[-2] == 1 and P[-1] == 0):
            P = add_bin(P, S)
        right_shift(P)
    P = P[:-1]
    P_dec = bin_to_dec(P)
    P_bin = ""
    for elem in P:
        P_bin += str(elem)
    print(P_dec)
    print(P_bin)
    return P_dec, P_bin

'''num1 = input("1st: ")
num2 = input("2nd: ")
booths(num1, num2)'''
