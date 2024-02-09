voltage=input('enter the value of voltage ')
resistence=input('enter the value of resistence ')
current=float(voltage)/float(resistence)
print(current)
#or to implement ohm's law
print("enter '1' to calculate voltage")
print("enter '2' to calculate current")
print("enter '3' to calculate resistence")
print("enter '4' to exit")
num=float(input('enter the number[1-4]'))
if num==1:
    r=float(input('enter the value of resistence '))
    i=float(input('enter the value of current '))
    v=i*r
    print("voltage ",v )
elif num==2:
    r=float(input('enter the value of resistence '))
    v=float(input('enter the value of voltage '))
    i=v/r
    print("current ",i)
elif num==3:
    v=float(input('enter the value of voltage '))
    i=float(input('enter the value of current '))
    r=v/i
    print("resistence ",r)
elif num==4:
    print('exit')
else:
    print('invalid input')

