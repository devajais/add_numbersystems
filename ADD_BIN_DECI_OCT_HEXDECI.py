x = []
n = input("Enter b for Binary addition\nEnter d for decimal addition\nEnter o for octal addition\nEnter h for hexadecimal addition\n")
def hexa_12(zz):
    if zz == 'A':
        return 10
    elif zz == 'B':
        return 11
    elif zz == 'C':
        return 12
    elif zz == 'D':
        return 13
    elif zz == 'E':
        return 14
    elif zz == 'F':
        return 15
    else:
        return int(zz)

def hexa_AB(zz):
    if zz == 10:
        return 'A'
    elif zz == 11:
        return 'B'
    elif zz == 12:
        return 'C'
    elif zz == 13:
        return 'D'
    elif zz == 14:
        return 'E'
    elif zz == 15:
        return 'F'
    else:
        return int(zz)

     
#add decimal numbers
def add_decimal(n1,n2):
    for i in range(len(n1)-1,-1,-1):
        a = n1[i]+n2[i]
        if a>=10:
            if i == 0:
                z = a-10
                x.append(z)
                x.append(1)
            else:
                z = a-10
                x.append(z)
                n1[i-1]+=1
        else:
            x.append(a)
            
#add binary numbers
def add_binary(n1,n2):
    for i in range(len(n1)-1,-1,-1):
        a = n1[i]+n2[i]
        if a>=2:
            if i == 0:
                z = a-2
                x.append(z)
                x.append(1)
            else:
                z = a-2
                x.append(z)
                n1[i-1]+=1
        else:
            x.append(a)
            
#add octal numbers
def add_octal(n1,n2):
    for i in range(len(n1)-1,-1,-1):
        a = n1[i]+n2[i]
        if a>=8:
            if i == 0:
                z = a-8
                x.append(z)
                x.append(1)
            else:
                z = a-8
                x.append(z)
                n1[i-1]+=1
        else:
            x.append(a)

#add hexadecimal numbers
def add_hexadecimal(n1,n2):
    for i in range(len(n1)-1,-1,-1):
        n1[i] = hexa_12(n1[i])
        n2[i] = hexa_12(n2[i])
        a = n1[i]+n2[i]
        if a>=16:
            if i == 0:
                z = a-16
                z = hexa_12(z)
                x.append(z)
                x.append(1)
            else:
                z = a-16
                n1[i-1] = hexa_12(n1[i-1])
                n1[i-1]+=1
                z = hexa_AB(z)
                x.append(z)
        else:
            a = hexa_AB(a)
            x.append(a)


if n.lower()=='b':
    n1 = [int(i) for i in input()]
    n2 = [int(i) for i in input()]
    add_binary(n1,n2)
elif n.lower()=='d':
    n1 = [int(i) for i in input()]
    n2 = [int(i) for i in input()]
    add_decimal(n1,n2)
elif n.lower()=='o':
    n1 = [int(i) for i in input()]
    n2 = [int(i) for i in input()]
    add_octal(n1,n2)
elif n.lower()=='h':
    n1 = [i for i in input()]
    n2 = [i for i in input()]
    add_hexadecimal(n1,n2)
print(x)
for i in range(len(x)-1,-1,-1):
    print(x[i],end='')
