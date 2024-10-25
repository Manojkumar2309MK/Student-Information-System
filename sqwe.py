from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
#  page 2 #

    
class Student():
  def __init__(self,root):
    self.root=root
    self.root.title('student Information System')
    self.root.geometry('1370x700')
    title=Label(self.root,text='student Information System',bd=9,relief=GROOVE,font=('times new roman',50,'bold'),bg='yellow',fg='red')
    title.pack(side=TOP,fill=X)
    #########All variables##########
    self.Roll_No_var=StringVar()
    self.name_var=StringVar()
    self.email_var=StringVar()
    self.gender_var=StringVar()
    self.contact_var=StringVar()
    self.dob_var=StringVar()
    self.search_by=StringVar()
    self.search_txt=StringVar()
    self.page1()

    #########Manage Frame page 1##########
  def page1(self):
    self.Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='blue')
    self.Manage_Frame.place(x=550,y=150,width=450,height=585)

    m_title=Label(self.Manage_Frame,text=' Student Info',bg='yellow',fg='black',font=('times new roman',40,'bold'))
    m_title.grid(row=0,columnspan=2,pady=20)

    lbl_roll=Label(self.Manage_Frame,text='Roll No',bg='blue',fg='white',font=('times new roman',20,'bold'))
    lbl_roll.grid(row=1,column=0,pady=10,padx=20)
    txt_roll=Entry(self.Manage_Frame,textvariable=self.Roll_No_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
    txt_roll.grid(row=1,column=1,pady=10,padx=20)

    lbl_name=Label(self.Manage_Frame,text='Name:',bg='blue',fg='white',font=('times new roman',20,'bold'))
    lbl_name.grid(row=2,column=0,pady=10,padx=20)
    txt_name=Entry(self.Manage_Frame,textvariable=self.name_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
    txt_name.grid(row=2,column=1,pady=10,padx=20)

    lbl_Email=Label(self.Manage_Frame,text='Email',bg='blue',fg='white',font=('times new roman',20,'bold'))
    lbl_Email.grid(row=3,column=0,pady=10,padx=20)
    txt_Email=Entry(self.Manage_Frame,textvariable=self.email_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
    txt_Email.grid(row=3,column=1,pady=10,padx=20)
 
    lbl_Gender=Label(self.Manage_Frame,text='Gender',bg='blue',fg='white',font=('times new roman',20,'bold'))
    lbl_Gender.grid(row=4,column=0,pady=10,padx=20)

    combo_gender=ttk.Combobox(self.Manage_Frame,textvariable=self.gender_var,font=('times new roman',13,'bold'),state='readonly')
    combo_gender['values']=('male','female','other')
    combo_gender.grid(row=4,column=1,pady=10,padx=20)

    lbl_Contact=Label(self.Manage_Frame,text='Contact',bg='blue',fg='white',font=('times new roman',20,'bold'))
    lbl_Contact.grid(row=5,column=0,pady=10,padx=20)
    txt_Contact=Entry(self.Manage_Frame,textvariable=self.contact_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
    txt_Contact.grid(row=5,column=1,pady=10,padx=20)

    lbl_Dob=Label(self.Manage_Frame,text='D.O.B',bg='blue',fg='white',font=('times new roman',20,'bold'))
    lbl_Dob.grid(row=6,column=0,pady=10,padx=20)
    txt_Dob=Entry(self.Manage_Frame,textvariable=self.dob_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
    txt_Dob.grid(row=6,column=1,pady=10,padx=20)

    lbl_Address=Label(self.Manage_Frame,text='Address',bg='blue',fg='white',font=('times new roman',20,'bold'))
    lbl_Address.grid(row=7,column=0,pady=10,padx=20)
    self.txt_Address=Text(self.Manage_Frame,font=('times new roman',10,'bold'),width=30,height=3)
    self.txt_Address.grid(row=7,column=1,pady=10,padx=20)

    #   Button frame
    btn_frame=Frame(self.Manage_Frame,bd=3,relief=RIDGE,bg='black')
    btn_frame.place(x=15,y=525,width=420)

    Addbtn=Button(btn_frame,text='Add',width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
    updatebtn=Button(btn_frame,text='Update',width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
    deletebtn=Button(btn_frame,text='Get Details',width=10,command=self.page2).grid(row=0,column=3,padx=10,pady=10)
    clearbtn=Button(btn_frame,text='Clear',command=self.clear,width=10).grid(row=0,column=2,padx=10,pady=10)
     #########details Frame page 2##########
  def call(self):
    self.Details_Frame.destroy()
    self.page1()
    messagebox.showinfo('info','fill the required detials \n then press the add button')
  def page2(self):
    self.Manage_Frame.destroy()
    self.Details_Frame=Frame(self.root,bd=4,relief=RIDGE,bg='blue')
    self.Details_Frame.place(x=350,y=100,width=1000,height=1000)
    
    lbl_search=Label(self.Details_Frame,text='Search By',bg='blue',fg='white',font=('times new roman',20,'bold'))
    lbl_search.grid(row=0,column=0,pady=10,padx=20)

    combo_search=ttk.Combobox(self.Details_Frame,textvariable=self.search_by,font=('times new roman',13,'bold'),width=10,state='readonly')
    combo_search['values']=('roll_no','name','contact')
    combo_search.grid(row=0,column=1,pady=10,padx=20)

    txt_search=Entry(self.Details_Frame,textvariable=self.search_txt,font=('times new roman',10,'bold'),width=20,bd=5,relief=GROOVE)
    txt_search.grid(row=0,column=2,pady=10,padx=20)

    searchbtn=Button(self.Details_Frame,text='Search',width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
    showallbtn=Button(self.Details_Frame,text='Show All',width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

      #########Table Frame##########
    Table_Frame=Frame(self.Details_Frame,bd=4,relief=RIDGE,bg='crimson')
    Table_Frame.place(x=10,y=70,width=760,height=500)

    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)

    self.student_table=ttk.Treeview(Table_Frame,column=('roll','name','email','gender','contact','dob','Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=self.student_table.xview)
    scroll_y.config(command=self.student_table.yview)

    self.student_table.heading('roll',text='Roll NO.')
    self.student_table.heading('name',text='Name')
    self.student_table.heading('email',text='Email')
    self.student_table.heading('gender',text='Gender')
    self.student_table.heading('contact',text='Contact')
    self.student_table.heading('dob',text='D.O.B')
    self.student_table.heading('Address',text='Address')

    self.student_table['show']='headings'
    self.student_table.column('roll',width=100)
    self.student_table.column('name',width=100)
    self.student_table.column('email',width=100)
    self.student_table.column('gender',width=100)
    self.student_table.column('contact',width=100)
    self.student_table.column('dob',width=100)
    self.student_table.column('Address',width=150)

    self.student_table.pack(fill=BOTH,expand=1)
    self.student_table.bind('<ButtonRelease-1>',self.get_cursor1)
    self.fetch_data()
    btn_frame=Frame(self.Details_Frame,bd=3,relief=RIDGE,bg='black')
    btn_frame.place(x=300,y=600,width=200)

    add2btn=Button(btn_frame,text='Add',command=self.call).grid(row=0,column=0,padx=10)
    delete2btn=Button(btn_frame,text='Delete',command=self.delete2).grid(row=0,column=1,padx=10)
    update2btn=Button(btn_frame,text='Update',command=self.update2).grid(row=0,column=2,padx=10)
    
  def add_students(self):
    con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
    cur=con.cursor()
    cur.execute('select roll_no from student')
    self.row=cur.fetchall()
    con.close()
    a=self.Roll_No_var.get().isnumeric()
    b=self.contact_var.get().isnumeric()
    c=str(self.txt_Address.get('0.0',END))
    d=c.isspace()
    print(d)
    if self.Roll_No_var.get()==''or self.name_var.get()==''or self.email_var.get()==''or self.gender_var.get()==''or self.contact_var.get()==''or self.dob_var.get()==''or d==True:
      messagebox.showerror('error','all fields are required to fill')
    elif a==False:
      messagebox.showerror('error','roll no should contain only numbers')
    elif b==False:
      messagebox.showerror('error','contact no should contain only numbers')
    elif len(self.row)!=0:
      a=list()
      for rows in self.row:
        e=list()
        a.append(rows[0])
        r=set(a)
        b=len(r)
        e.append(int(self.Roll_No_var.get()))
        f=set(e)
        s=r.difference(f)
        type(self.Roll_No_var.get())
        d=len(s)
      if d<b:
           messagebox.showerror('error','this roll_no already exist \n please enter new roll_no')
      else:
          con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
          cur=con.cursor()
          cur.execute('insert into student values (%s,%s,%s,%s,%s,%s,%s)',(self.Roll_No_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get('1.0',END)))
          con.commit()
          self.clear()
          con.close()
          messagebox.showinfo('success','Record has been inserted')
    else:
       con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
       cur=con.cursor()
       cur.execute('insert into student values (%s,%s,%s,%s,%s,%s,%s)',(self.Roll_No_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get('1.0',END)))
       con.commit()
       self.fetch_data()
       self.clear()
       con.close()
       messagebox.showinfo('success','Record has been inserted')
     
       
      
          
  def fetch_data(self):
    con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
    cur=con.cursor()
    cur.execute('select * from student order by roll_no')
    self.rows=cur.fetchall()
    if len(self.rows)!=0:
      self.student_table.delete(*self.student_table.get_children())
      for row in self.rows:
        self.student_table.insert('',END,values=row)
      con.commit()
    con.close()
  def clear(self):
    self.Roll_No_var.set('')
    self.name_var.set('')
    self.email_var.set('')
    self.gender_var.set('')
    self.contact_var.set('')
    self.dob_var.set('')
    self.txt_Address.delete('1.0',END)
  def get_cursor(self,event):
    cursor_row=self.student_table.focus()
    contents=self.student_table.item(cursor_row)
    row=contents['values']
    if len(row)!=0:
      self.Roll_No_var.set(row[0])
      self.name_var.set(row[1])
      self.email_var.set(row[2])
      self.gender_var.set(row[3])
      self.contact_var.set(row[4])
      self.dob_var.set(row[5])
      self.txt_Address.delete('0.0',END)
      self.txt_Address.insert(row[6])
  def get_cursor1(self,event):
    cursor_row=self.student_table.focus()
    contents=self.student_table.item(cursor_row)
    self.row=contents['values']
    if len(self.row)!=0:
      self.a=self.row[0]
      self.b=self.row[1]
      self.c=self.row[2]
      self.d=self.row[3]
      self.e=self.row[4]
      self.f=self.row[5]
      self.g=self.row[6]
  
    
    



  def update_data(self):
     a=str(self.txt_Address.get('0.0',END))
     d=a.isspace()
     b=self.contact_var.get().isnumeric()
     if  self.name_var.get()==''or self.email_var.get()==''or self.gender_var.get()==''or self.contact_var.get()==''or self.dob_var.get()==''or d==True:
       messagebox.showerror('error','all fields are required to fill')
       '''elif a==False:
       messagebox.showerror('error','roll no should contain only numbers')'''
     elif b==False:
       messagebox.showerror('error','contact no should contain only numbers')
     else:
       con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
       cur=con.cursor()
       cur.execute('update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s',(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get('1.0',END),self.Roll_No_var.get()))
       con.commit()
       self.clear()
       con.close()
       messagebox.showinfo('success','Record has been updated')

  def delete_data(self):
     con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
     cur=con.cursor()
     cur.execute('delete from student where roll_no=%s',self.Roll_No_var.get())
     con.commit()
     con.close()
     self.fetch_data()
     self.clear()
  def delete2(self):
    self.get_cursor1('event')
    if len(self.row)==0:
      messagebox.showerror('error','please select the row using cursor \n then press the delete button')
    elif len(self.row)!=0:
      con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
      cur=con.cursor()
      cur.execute('delete from student where roll_no=%s',self.a)
      con.commit()
      con.close()
      self.fetch_data()
     
  def update2(self):
    self.get_cursor1('event')
    if len(self.row)==0:
      messagebox.showerror('error','please select the row using cursor \n then press the update button')
    elif len(self.row)!=0:
      self.Details_Frame.destroy()
      self.page1()
      self.Roll_No_var.set(self.a)
      self.name_var.set(self.b)
      self.email_var.set(self.c)
      self.gender_var.set(self.d)
      self.contact_var.set(self.e)
      self.dob_var.set(self.f)
      self.txt_Address.delete('0.0',END)
      self.txt_Address.insert(END,self.g)
      messagebox.showinfo('info','enter the required change \n then press update button')
      
  
    
    
  def search_data(self):
     if self.search_txt.get()=='':
       messagebox.showerror('error','please fill the search box')
     elif self.search_by.get()=='roll_no':    
       con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
       cur=con.cursor()
       cur.execute('select roll_no from student')
       self.row=cur.fetchall()
       con.close()
       if len(self.row)!=0:
        a=list()
        if self.search_txt.get().isnumeric()==False:
          messagebox.showerror('error','Roll_no should not contain any alphabets or special characters') 
        else:
          for rows in self.row:
            e=list()
            a.append(rows[0])
            r=set(a)
            b=len(r)
            e.append(int(self.search_txt.get()))
            f=set(e)
            s=r.difference(f)
            d=len(s)
          if d>=b:
             messagebox.showerror('error','There is no such roll_no \n please enter the correct roll_no')
          else:
            self.search_in()
     elif self.search_by.get()=='name':
       con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
       cur=con.cursor()
       cur.execute('select name from student')
       self.row=cur.fetchall()
       con.close()
       if len(self.row)!=0:
        a=list()
        for rows in self.row:
          e=list()
          a.append(rows[0])
          r=set(a)
          b=len(r)
          e.append(self.search_txt.get())
          f=set(e)
          s=r.difference(f)
          d=len(s)
        if d>=b:
             messagebox.showerror('error','There is no such name \n please enter the correct name')
        else:
            self.search_in()
     elif self.search_by.get()=='contact':
       con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
       cur=con.cursor()
       cur.execute('select contact from student')
       self.row=cur.fetchall()
       con.close()
       if len(self.row)!=0:
        a=list()
        if self.search_txt.get().isnumeric()==False:
          messagebox.showerror('error','Roll_no should not contain any alphabets or special characters') 
        else:
          for rows in self.row:
            e=list()
            a.append(rows[0])
            r=set(a)
            b=len(r)
            e.append(self.search_txt.get())
            f=set(e)
            s=r.difference(f)
            d=len(s)
          if d>=b:
             messagebox.showerror('error','There is no such contact no \n please enter the correct contact no')
          else:
            self.search_in()
  def search_in(self):
       con=pymysql.connect(host='localhost',user='root',password='',database='sms2')
       cur=con.cursor()
       cur.execute("select * from student where "+str(self.search_by.get())+"="+"'"+str(self.search_txt.get())+"'")
       self.rows=cur.fetchall()
       if len(self.rows)!=0:
         self.student_table.delete(*self.student_table.get_children())
         for row in self.rows:
          self.student_table.insert('',END,values=row)
         con.commit()
       con.close()
    
    
class Student():
  root=Tk()
  obj=Student(root)
  root.mainloop()
  
 
