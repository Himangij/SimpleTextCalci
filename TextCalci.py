moreOperations='True'
while moreOperations=='True':
    no1=int(input('Enter 1st num: '))
    no2=int(input('Enter 2nd num: '))
    oper=input('Enter Operation (+,-,/,*) : ')
    if oper == '+':
        print(no1+no2)
    elif oper=='-':
        print(no1-no2)
    elif oper=='/':
        print(no1//no2)
    elif oper=='*':
        print(no1*no2)
    else:
        print('Select proper operation from list')
    moreOperations=input('Do you want to continue(True/False) :')
    

