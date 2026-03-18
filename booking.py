def SingleTon(arg):
    D={}
    def inner():
        if len(D)==0:
            D['a']=arg()
        return D['a']
    return inner
@SingleTon
class movie1:
    def __init__(self):
        self.maxtic=200
    def Booking(self):
        print(f'avl tickets{self.maxtic}')
        count=int(input('enter the no of ticket'))
        if 0<count<=self.maxtic:
            print('sucessfull')
            self.maxtic-=count
        else:
            print('invalid')
@SingleTon
class movie2:
    def __init__(self):
        self.maxtic=200
    def Booking(self):
        print(f'avl tickets{self.maxtic}')
        count=int(input('enter the no of ticket'))
        if 0<count<=self.maxtic:
            print('sucessfull')
            self.maxtic-=count
        else:
            print('invalid')
@SingleTon
class movie3:
    def __init__(self):
        self.maxtic=200
    def Booking(self):
        print(f'avl tickets{self.maxtic}')
        count=int(input('enter the no of ticket'))
        if 0<count<=self.maxtic:
            print('sucessfull')
            self.maxtic-=count
        else:
            print('invalid')
@SingleTon
class movie4:
    def __init__(self):
        self.maxtic=200
    def Booking(self):
        print(f'avl tickets{self.maxtic}')
        count=int(input('enter the no of ticket'))
        if 0<count<=self.maxtic:
            print('sucessfull')
            self.maxtic-=count
        else:
            print('invalid')
@SingleTon
class movie5:
    def __init__(self):
        self.maxtic=200
    def Booking(self):
        print(f'avl tickets{self.maxtic}')
        count=int(input('enter the no of ticket'))
        if 0<count<=self.maxtic:
            print('sucessfull')
            self.maxtic-=count
        else:
            print('invalid')
def BMYS():
    print('1) movie1 \n 2) movie2 \n 3) movie3 \n 4) movie4 \n 5) movie5')
    choice=int(input('enter your choice :'))
    if choice==1:
        user=movie1()
        user.Booking()
    elif choice==2:
        user=movie2()
        user.Booking()
    elif choice==3:
        user=movie3()
        user.Booking()
    elif choice==4:
        user=movie4()
        user.Booking()
    elif choice==5:
        user=movie5()
        user.Booking()
    else:
        print('there is no movie')
def payTM():
    print('1) movie1 \n 2) movie2 \n 3) movie3 \n 4) movie4 \n 5) movie5')
    choice=int(input('enter your choice :'))
    if choice==1:
        user=movie1()
        user.Booking()
    elif choice==2:
        user=movie2()
        user.Booking()
    elif choice==3:
        user=movie3()
        user.Booking()
    elif choice==4:
        user=movie4()
        user.Booking()
    elif choice==5:
        user=movie5()
        user.Booking()
    else:
        print('there is no movie')

cust1=BMYS()
cust2=payTM()
cust3=BMYS()
cust3=BMYS()
