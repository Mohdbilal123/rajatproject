from tkinter import *
from tkinter import messagebox as msg
from KEEpydb import KEEpydb
from PIL import ImageTk, Image

class All_FUNCTION:
    def about(self):
       f=Frame(root,width=500,height=500).place(x=0,y=0)
       Button(f,text='Back',command=self.home).place(x=20,y=20)
       
    def ITEMS(self):
        #msg.showinfo('INFO','This is RAJAT\'s BAKERY')

        print('\titems\n')
        product=self.items.keys()
        for i in product:
            print(i+'\t'+str(self.items[i][0])+'\t'+str(self.items[i][1]))


    
        

class Main(All_FUNCTION):
    def __init__(self,root):
        self.yellow='white'
        self.height='500'
        self.width='500'
        self.root=root
        self.root.geometry('500x500')
        self.root.config(bg=self.yellow)
        self.root.title('rajat')
        #database initialise
        self.query=KEEpydb.query('sriganeshbakery','rajat123',324146566)
        
        #load items
        self.img=ImageTk.PhotoImage(Image.open('assets\\rajat.jpg').resize((800,700), Image.ANTIALIAS))
        self.items={}

        c=2
        for i in range(6):
            self.items[self.query.get_cell('a'+str(c))]=[self.query.get_cell('b'+str(c)),self.query.get_cell('c'+str(c)),self.query.get_cell('d'+str(c))]
            c+=1                      
            
        
        

        self.home()
        
    def home(self):
        frame=Frame(self.root,width=self.width,
                    height=self.height,bg='white').place(x=0,y=0)
        a=Label(frame,image=self.img)
        a.image=self.img
        a.place(x=-100,y=-100)
        Label(frame,text='SRI GANESH BAKERY  !',font='verdana 20 bold',bg=self.yellow).place(x=20,y=70)
        Button(frame,text='  ABOUT',bg='white',padx=50,command=self.about).place(x=50,y=150)
        Button(frame,text='BUY',bg='white',padx=60,command=self.buyitems).place(x=50,y=190)
        Button(frame,text='ITEMS',bg='white',padx=54,command=self.buyitems).place(x=50,y=230)
        Button(frame,text='PAYMENT',bg='white',padx=45).place(x=50,y=270)
        Button(frame,text='CUSTOMER DETAILS',bg='white',padx=20).place(x=50,y=310)
        Button(frame,text='EXIT',bg='white',padx=57).place(x=50,y=350)
        
    def buyitems(self):
        self.img=ImageTk.PhotoImage(Image.open('assets\\d.jpg').resize((800,700), Image.ANTIALIAS))
        frame=Frame(self.root,width=self.width,
                    height=self.height,bg='white').place(x=0,y=0)
        l=Listbox(frame)
        Label(frame,text='Select Items',font='verdana 15 bold',bg='white',fg='grey50').place(x=20,y=20)
        l.place(x=20,y=60,width=200,height=400)
        for i in self.items.keys():
            l.insert(END,i)
        global quantity
        self.q=0
        quantity=Label(frame,text='Quantity : '+str(self.q),font='verdana 13 bold')
        quantity.place(x=300,y=400)
        
    

        Button(frame,text='Add TO Cart',bg='yellow',command=self.inc).place(x=300,y=50,width=100)
        Button(frame,text='Next',bg='yellow',command=self.bookings).place(x=300,y=80,width=100)
    def inc(self):
        global quantity
        self.q+=1
        quantity.config(text='Quantity : '+str(self.q))
    def bookings(self):
        frame=Frame(self.root,width=self.width,
                    height=self.height,bg='white').place(x=0,y=0)
        Button(frame,text='back',bg='red',command=self.home).place(x=20,y=475)
        Label(frame,text='Booking Screen',font='verdana 15 bold',bg='white',fg='grey50').place(x=20,y=20)
        name=StringVar()
        address=StringVar()
        number=StringVar()
        a1=Entry(frame,textvariable=name)
        a1.place(x=20,y=100)
        a2=Entry(frame,textvariable=address)
        a2.place(x=20,y=100+50)
        a3=Entry(frame,textvariable=number)
        a3.place(x=20,y=100+100)
        
        name.set('name')
        address.set('address')
        number.set('number')

        a1.bind('<Button-1>',lambda e:name.set(''))
        a2.bind('<Button-1>',lambda e:address.set(''))
        a3.bind('<Button-1>',lambda e:number.set(''))

        Button(frame,text='Submit').place(x=20,y=445)
        
        
if __name__=='__main__':
    root=Tk()
    Main(root)
    root.mainloop()
