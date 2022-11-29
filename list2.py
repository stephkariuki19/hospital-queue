from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()

root.title('Hospital Priority Queue')

my_canvas = Canvas(root, width=1000, height=700, bg='pink')
my_canvas.grid(column=0, row=0, pady=20, padx=20)
#hospital image
icon1=PhotoImage(file="C:/Users/HP/Desktop/IBM-Z/hospital.png")
image1 = Label(root,image=icon1,bg="pink")
image1.place( x=50,y=400,height=200,width=200)

#patients
photo=PhotoImage(file="C://Users//HP//Downloads//patient.png")

class myList:
    def __init__(self):
        self.storage = []
        #self.capacity = capacity
        self.size = 0
    # def isFull(self): removing capacity concept
    #     return self.size == self.capacity
    def isEmpty(self):
        return len(self.storage) ==0
    def addPatient(self,item):
        # if (self.isFull()):
        #     raise Exception("Queue is Full")
        #self.storage[self.size] = item  # put data at last pos
        self.storage.append(item)
        self.size += 1
        self.sortList(self.storage)
    def sortList(self,list):
        n = len(self.storage)
        for pass_num in range(n-1,0,-1):
            for i in range(pass_num):
                if list[i] > list[i+1]:
                    list[i],list[i+1]=list[i+1],list[i]
    def removePatient(self,item):
        # if self.size==0:
        #     raise Exception("Queue is empty")
        for i in range(len(self.storage)-1):
            if self.storage[i] ==item:
                print(f"found and removing {item}")
                self.storage.pop(i)#reduces capacity
        last_index=len(self.storage)-1
        if self.storage[last_index] ==item:
            print(f"found and removing {item}")
            self.storage.pop(last_index)
                #self.storage[self.size+1]=0

    def replace(self,item,newitem):# new item=new key,old value
        if self.size==0:
            raise Exception("Queue is empty")
        for i in range(len(self.storage)):
            if self.storage[i] ==item:
                print(f"found {item}")
                self.storage.pop(i)#reduces capacity
                self.storage.append(newitem)
                self.sortList(self.storage)

    def Queuesize(self):
        return len(self.storage)
    def peekQueue(self):
        return self.storage[0]
    def pollQueue(self):
        first_item = self.storage[0]
        self.removePatient(first_item)
        return first_item
#FUNCTIONS FOR BUTTONS
def show_size():
    if (m.Queuesize()>0):
        messagebox.showinfo("Status",f"SIZE = {m.Queuesize()}")
    else:
        messagebox.showinfo("Error","SIZE=0")

def show_isempty():
    if (m.Queuesize()==0):
        messagebox.showinfo("Status","TRUE")
    else:
        messagebox.showinfo("Status","FALSE")

def top():
    if(m.Queuesize()>0):
        messagebox.showinfo("Status", f" TOP= {m.peekQueue()}")
    else:
        messagebox.showinfo("Error", "Empty Line")

def finish_poll():
    if (m.Queuesize()==0):
        messagebox.showinfo("Error","Empty line")
    else:
        messagebox.showinfo("Status",f"Removed={m.peekQueue()}")
        m.pollQueue()
        print(m.storage)

def finish_admit():
    if (m.Queuesize() == 7):
        messagebox.showinfo("Error", "Queue full")
    else:
        res = txt.get()
        y=res.split(',')
        changed = int(y[0])
        y.pop(0)
        y.insert(0,changed)
        m.addPatient(y)
        # DRAWING
        inter = 120
        starting = 250
        s = m.Queuesize()
        p = 0
        while p < s:
            my_canvas.create_image((starting + (inter * p)), 490, image=photo, anchor='center')
            p += 1
        print(m.storage)
def finish_remove():
    if (m.Queuesize()==0):
        messagebox.showinfo("Error","Empty line")
    removed = txt2.get()
    z = removed.split(',')
    new_int = int(z[0])
    z.pop(0)
    z.insert(0, new_int)
    m.removePatient(z)
    # DRAWING
    my_canvas.delete("all")
    inter = 120
    starting = 250
    s = m.Queuesize()
    p = 0
    while p < s:
        my_canvas.create_image((starting + (inter * p)), 490, image=photo, anchor='center')
        p += 1
    print(m.storage)
def finish_changeprio():
    #get data
    old_data = txt3.get()
    a=old_data.split(',')
    old_data_int =int(a[0])
    a.pop(0)
    a.insert(0,old_data_int)
    #change with new_data
    new_data = txt4.get()
    b = new_data.split(',')
    new_data_int= int(b[0])
    b.pop(0)
    b.insert(0, new_data_int)
    m.replace(a,b)
    print(m.storage)

def finish_changeval():
    #get data
    old_val = txt5.get()
    c=old_val.split(',')
    old_val_int =int(c[0])
    c.pop(0)
    c.insert(0,old_val_int)
    #change with new_data
    new_val = txt6.get()
    d = new_val.split(',')
    new_val_int= int(d[0])
    d.pop(0)
    d.insert(0, new_val_int)
    m.replace(c,d)
    print(m.storage)

txt=Entry(root,width=15)#add
txt.place(x=150,y=30)

txt2=Entry(root,width=15)#remove
txt2.place(x=160,y=80)

txt3=Entry(root,width=15)#old p
txt3.place(x=210,y=130)

txt4=Entry(root,width=15)#new p
txt4.place(x=320,y=130)

txt5=Entry(root,width=15)#old v
txt5.place(x=210,y=180)

txt6=Entry(root,width=15)#new v
txt6.place(x=320,y=180)


#BUTTONS
peek=Button(root, text ="PEEK", bg="white", font=("Arial", 8),command=top)
peek.place(x=25, y=20, width=40, height=40)

empty = Button(root,text = "EMPTY", bg="white", font=("Arial", 8),command=show_isempty)
empty.place(x=25, y=70, width=40, height=40)

size=Button(root,text ="SIZE", bg="white", font=("Arial", 8),command=show_size)
size.place(x=25, y=120, width=40, height=40)

poll=Button(root,text ="POLL", bg="white", font=("Arial", 8),command=finish_poll)
poll.place(x=25, y=170, width=40, height=40)

admit=Button(root, text ="ADMIT", bg="white", font=("Arial", 8),command=finish_admit)
admit.place(x=100, y=20, width=40, height=40)

remove=Button(root, text ="REMOVE", bg="white", font=("Arial", 8),command=finish_remove)
remove.place(x=100, y=70, width=50, height=40)

change_prio=Button(root, text ="CHANGE PRIORITY", bg="white", font=("Arial", 8),command=finish_changeprio)
change_prio.place(x=100, y=120, width=100, height=40)

change_val=Button(root, text ="CHANGE VALUE", bg="white", font=("Arial", 8),command=finish_changeval)
change_val.place(x=100, y=170, width=100, height=40)

m = myList()

root.mainloop()