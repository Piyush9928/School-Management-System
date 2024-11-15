import mysql.connector
from tkinter import *
import csv
import os
from tkinter import messagebox

conn = mysql.connector.connect(user='root',password='piyush',host='localhost',port=3306,database='school')
cursor=conn.cursor()

cursor.execute("create table if not exists faculty(serial_number int PRIMARY KEY Not Null,name char(20) Not Null,username varchar(10) Not Null,email_id varchar(20), contact int(10), address text ,subject varchar(10), gender char(6), class int(2),passw varchar(10) Not Null);")
cursor.execute("create table if not exists class_table(roll_no int(10),name varchar(30),class int(2),contact int Not Null,email_id varchar(40),address text,age int(2),gender char(5),dob date,doa date,PRIMARY KEY(roll_no,class));")

main_window = Tk()
main_window.title("School Management System")
p1 = PhotoImage(file ='D:/PIYUSH/Py/pic.png')
main_window.iconphoto(True,p1)
main_window.geometry('1024x600')
main_window.withdraw()

def remove(event):
              a.delete(0, END)
def remove1(event):
              b.delete(0, END)
def remove2(event):
              c.delete(0, END)
def remove3(event):
              d.delete(0, END)
def remove4(event):
              e.delete(0, END)
def remove5(event):
              f.delete(0, END)
def remove6(event):
              g.delete(0, END)
def remove7(event):
              h.delete(0, END)
def on_closing():
              if messagebox.askokcancel("Quit", "Do you want to quit?"):
                            conn.close()
                            main_window.destroy()

def logout():
              login_window.deiconify()
              main_window.withdraw()
###############################################################################
# submit user detials into database
###############################################################################
def delete_data():
              del_data=Entry_rollno3.get()
              show_data_command = "SELECT * FROM class_table WHERE roll_no = " + del_data
              de_command = " DELETE FROM class_table WHERE roll_no = " + del_data
              cursor.execute(show_data_command)
              records=cursor.fetchall()
              individual_deatil1 = records
              cursor.execute(de_command)
              cursor.execute(show_data_command)
              records=cursor.fetchall()
              individual_deatil2 = records
              status_msg.place(x = 700,y = 380)
                            
              if len(individual_deatil1) == 0 :
                            status_msg.config(text = "User does not exist")
              else:
                            if len(individual_deatil1) >= len(individual_deatil2):
                                           status_msg.config(text = "user account deleted successfully")
                            else:
                                           status_msg.config(text = "Error in deleteing user account")
              conn.commit()
###############################################################################
# submit user detials into database
###############################################################################
def show_class_list():
              spin_class1 = spin_class.get()
              show_data_command2 = "SELECT * FROM class_table WHERE class = " + spin_class1
              cursor.execute(show_data_command2)
              record=cursor.fetchall()
              class_deatil = record
              conn.commit()
              file=open("D://PIYUSH/Py/class_list.csv",'w',newline="")

              a = []
              c=["roll_no","name","class","contact","email","address","age","gender","dob","doa"]
              writerobj=csv.writer(file)
              writerobj.writerow(c)
              for i in range(len(class_deatil)):
                            a.insert(1,class_deatil[i])
                            writerobj.writerows(a)
                            a=[]
                            abc = "SELECT * FROM class_table WHERE class = '%s'" % spin_class1
                            cursor.execute(abc)
                            record=cursor.fetchall()
                            userdeatil=record
                            status_msg.place(x = 700, y = 40)
              if len(userdeatil) == 0:
                            status_msg.config(text = "No list exist")
              else:
                            status_msg.config(text = "list generated successfull")
              file.close()
              
###############################################################################
# submit user detials into database
###############################################################################
def show_class_details():
              os.startfile("D://PIYUSH/Py/class_list.csv")
###############################################################################
# submit user detials into database
###############################################################################
def show_data_sub():
              roll_no=Entry_rollno4.get()
              spin_class=spin_class1.get()
              show_data_command = "SELECT * FROM class_table WHERE roll_no = " + roll_no + " and class = " + spin_class
              print(show_data_command)
              cursor.execute(show_data_command)
              record=cursor.fetchall()
              individual_deatil =record
              conn.commit()
              if len(individual_deatil) >= 1 :
                            table_window_tp = Toplevel(main_window)
                            for i in range(len(individual_deatil)):
                                          for j in range(8):
                                                        e = Entry(table_window_tp, width=10, fg='blue',
                                                        font=('Helvetica',15))
                                                        e.grid(row=i, column=j)
                                                        e.insert(END, individual_deatil[i][j])
              else:
                            status_msg.config(text = "No details found")
                            status_msg.place(x = 715,y = 150)
###############################################################################
# submit user detials into database
###############################################################################
def modify_table_entry():
              roll_no = Entry_rollno1.get()
              entry_type = str(clicked.get())
              table_entry = str(entry.get())
              table_entry_temp = table_entry
              print(type(entry_type))
              print(type(table_entry_temp))
              if entry_type==("name" or "email" or "address" or "contact" or "gender"):
                            table_entry_temp = "'" + table_entry + "'"
                            str_command = "UPDATE class_table SET " + entry_type + " = " + table_entry_temp + " WHERE roll_no " + " = " + roll_no
                            cursor.execute(str_command)
                            conn.commit()
                            com = "SELECT "+ entry_type + " FROM class_table WHERE roll_no = " + roll_no
                            cursor.execute(com)
                            record=cursor.fetchall()
                            cm1 = record
                            print(cm1)
                            print(table_entry)
                            status_msg.place(x = 715,y = 265)
              if len(cm1) != 0 and str(cm1[0][0]) == table_entry:
                            status_msg.config(text = "updated successfull")
              else:
                            status_msg.config(text = "updated unsuccessfull")
              conn.commit()
###############################################################################
# submit user detials into database
###############################################################################
def btn_su_submit_click():
              serial_no =entry_su_serialno.get()
              name=entry_su_name.get()
              username=entry_su_username.get()
              email_id=entry_su_email.get()
              contact=entry_su_contact.get()
              address=entry_su_address.get()
              gender=entry_su_gender.get()
              clas=entry_su_class.get()
              subject=entry_su_subject.get()
              passw=entry_su_pass.get()
              cursor.execute("INSERT INTO faculty (serial_number, name,username,address, class ,subject, contact, email_id, gender,passw) values('{}','{}','{}' ,'{}' ,'{}' ,'{}','{}' ,'{}' ,'{}' ,'{}')".format(serial_no, name, username,address, clas ,subject,contact, email_id, gender,passw))
              conn.commit()
              if(btn_su_submit['text']=='Submit'):
                            btn_su_submit['text']='Submitted'
              else:
                            btn_su_submit['text']='Submit'
###############################################################################
# submit user detials into database
###############################################################################
def btn_ad_submit_click():
              roll_no2 =entry_ad_serialno2.get()
              name2=entry_ad_name2.get()
              email_id2=entry_ad_email2.get()
              contact2=entry_ad_contact2.get()
              address2=entry_ad_address2.get()
              age2= entry_ad_userage2.get()
              gender2=entry_ad_gender2.get()
              clas2=entry_ad_class2.get()
              doa=entry_ad_doa2.get()
              dob=entry_ad_dob2.get()
              cursor.execute("insert into class_table(roll_no, name, class, contact,email_id, address ,age,gender,dob,doa) VALUES( {},'{}','{}',{},'{}','{}',{},'{}','{}','{}')".format(roll_no2,name2,clas2,contact2,email_id2,address2,age2,gender2,dob,doa))
              conn.commit()
              if(btn_ad_submit['text']=='Submit'):
                            btn_ad_submit['text']='Submitted'
              else:
                            btn_ad_submit['text']='Submit'
###############################################################################
# show signup window
###############################################################################
def btn_signup_click():
              signup_TL.deiconify()
              login_window.withdraw()
###############################################################################
# Add student data
###############################################################################
def add_student_details():
              add_details_TL.deiconify()
              main_window.withdraw()
##############################################################################
# user login submit button function
##############################################################################
def btn_submit_click():

    user = entry_username.get()
    passs = entry_password.get()
    
    if user == 'a' and passs == "a" :
        login_window.withdraw()
        main_window.deiconify()

    sql_select_Query = "select username from faculty where username = '%s'" % user 
    cursor.execute(sql_select_Query) 
    records = cursor.fetchall() 
    userdeatil = records 
    sql_select_Query2 = "select passw from faculty where passw = '%s' and username= '%s'" % (passs, user) 
    cursor.execute(sql_select_Query2) 
    records = cursor.fetchall() 
    passworddetail = records 
    conn.commit()
   
    # 
    status_msg1=Message(login_window)
    status_msg1.place(x=400,y=30)
    

    if len(userdeatil) != 0 and len(passworddetail) !=0:
        if userdeatil[0][0] == user:
            
            if passworddetail[0][0] == passs:
               login_window.withdraw()
               main_window.deiconify()
            else:
                status_msg1.config(text = "enterd password is incorrect!! please eneter a valid password")    
        else:
            status_msg1.config(text = "User does not exist") 
    else:
        status_msg1.config(text = "enterd  username or password is incorrect!!") 









##############################################################################
# frame compartment
###############################################################################
frame_box=Frame(main_window,borderwidth = 2,relief="ridge",width=1000,height=90)
frame_box.place(x=10,y=10)
frame_box=Frame(main_window,borderwidth = 2,relief="ridge",width=1000,height=90)
frame_box.place(x=10,y=120)
frame_box=Frame(main_window,borderwidth = 2,relief="ridge",width=1000,height=90)
frame_box.place(x=10,y=230)
frame_box=Frame(main_window,borderwidth = 2,relief="ridge",width=1000,height=90)
frame_box.place(x=10,y=340)
status_msg = Message(main_window,width=200)
position_y = 50
position_x = 40
position_x_opset = 140
###############################################################################
# 1 compartment
###############################################################################
lbl_class_list = Label(main_window,text="Class list")
lbl_class_list.place(x=16,y=16)
spin_class = Spinbox(main_window, from_= 0, to = 12, bd="1",width = 11,font =
"1",fg="grey")
spin_class.place(x = position_x ,y = position_y)
g=spin_class
g.insert(0,"Select class ")
g.bind('<FocusIn>',remove6)
btn_generate = Button(main_window, width = 20,bd="1",height = 1,text="Generate",command = show_class_list)
btn_generate.place(x = position_x + position_x_opset ,y=position_y)
btn_show = Button(main_window,text = "show list",bd="1",width = 20,command = show_class_details)
btn_show.place(x = 2 * position_x + 2 * position_x_opset , y = position_y)
lbl_status1 = Label(main_window,text = "Status")
lbl_status1.place(x = 4 * position_x + 4* position_x_opset , y = position_y-34)
###############################################################################
# 2 compartment
###############################################################################
lbl_show_individual = Label(main_window,text="Table of individual student")
lbl_show_individual.place(x = position_x-24,y = 3*position_y-20)
Entry_rollno4 = Entry(main_window,width = 11,font = "1",fg="grey")
Entry_rollno4.place(x = position_x , y = 3 * position_y + 10)
c = Entry_rollno4
c.insert(0, "Enter Roll no ")
c.bind('<FocusIn>', remove2)
spin_class1 = Spinbox(main_window, from_= 0, to = 12,bd="1",width = 14 , font ="1",fg="grey")
spin_class1.place(x = position_x + position_x_opset, y = 3* position_y + 10)
h=spin_class1
h.insert(0,"Select class ")
h.bind('<FocusIn>',remove7)
btn_submit = Button(main_window ,text = "Submit", bd="1",width = 18,command = show_data_sub)
btn_submit.place(x = 2 * position_x + 2 * position_x_opset , y = 3 * position_y + 10)
lbl_status2 = Label(main_window,text = "Status")
lbl_status2.place(x = 4 * position_x + 4 * position_x_opset , y = 3 *position_y - 20)
###############################################################################
# 3 compartment
###############################################################################
lbl_modify = Label(main_window,text="Modify details")
lbl_modify.place(x = position_x-24,y = 5 * position_y - 10)
Entry_rollno1 = Entry(main_window,width = 11, font = "1",fg="grey")
Entry_rollno1.place(x = position_x , y = 5* position_y + 20)
d=Entry_rollno1
d.insert(0, "Enter Roll no ")
d.bind('<FocusIn>', remove3)
options = ['name','contact', 'email id', 'address', 'age', 'gender',]
clicked = StringVar()
clicked.set( "Options" )
entry_type = OptionMenu(main_window , clicked , *options , )
entry_type.place(x = position_x + position_x_opset, y = 5* position_y + 20)
entry_type.config(width=10)
entry = Entry(main_window,width = 15, font = "1",fg="grey")
entry.place(x = 2 * position_x + 2 * position_x_opset, y = 5* position_y +20)
e=entry
e.insert(0, "Modify Details ")
e.bind('<FocusIn>', remove4)
btn_submit = Button(main_window,text="Generate1",bd="1",width=20,command = modify_table_entry)
btn_submit.place(x = 2* position_x + 3 * position_x_opset + 20 , y = 5 * position_y + 20)
lbl_status2 = Label(main_window,text="Status")
lbl_status2.place(x = 4 * position_x + 4 * position_x_opset , y = 5 * position_y - 11)
###############################################################################
# 4 compartment
###############################################################################
lbl_modify = Label(main_window,text="Delete details")
lbl_modify.place(x = position_x - 24 , y = 7 * position_y )
Entry_rollno3 = Entry(main_window,text="Add record3",width = 11, font ="1",fg="grey")
Entry_rollno3.place(x = position_x ,y = 7 * position_y + 30 )
f=Entry_rollno3
f.insert(0, "Enter Roll no ")
f.bind('<FocusIn>', remove5)
btn_del=Button(main_window,text="Delete",bd=1,width=20,command=delete_data)
btn_del.place(x = position_x + position_x_opset , y = 7 * position_y + 30)
lbl_status2 = Label(main_window,text="Status")
lbl_status2.place(x = 4 * position_x + 4 * position_x_opset, y = 7*position_y )
###############################################################################
# 5 compartment
###############################################################################
btn_close1=Button(main_window,text="close",bd="1",command =
main_window.destroy,width = 18)
btn_close1.place(x = position_x - 30 , y = 9 * position_y)
btn_log_out=Button(main_window,text="Log Out",bd="1",command=logout,width = 18)
btn_log_out.place(x = position_x_opset + 170 , y = 9 * position_y)
btn_add_student = Button(main_window,text="Add Details",bd="1",command=add_student_details,width = 18)
btn_add_student.place(x = position_x_opset + 20 , y = 9 * position_y)
###############################################################################
# login window design
###############################################################################
login_window = Toplevel(main_window)
login_window.geometry("480x300")
login_window_V0 = PanedWindow(login_window ,orient = VERTICAL)
login_window_H1 = PanedWindow(login_window_V0 ,orient = HORIZONTAL)
login_window_V1 = PanedWindow(login_window_H1 ,orient = VERTICAL)
login_window_V2 = PanedWindow(login_window_H1 ,orient = VERTICAL)
signup_PW_H2 = PanedWindow(login_window_V0 ,orient = HORIZONTAL)
login_window_V0.pack(pady=20)
lbl_username=Label(login_window_V1,text="Username",font = "1")
lbl_pass=Label(login_window_V1,text="Password", font = "1")
entry_username =Entry(login_window_V2,font = "1",fg="grey",bd=0)
entry_username.insert(0, "Enter username ")


a=entry_username
a.bind('<FocusIn>', remove)
entry_password=Entry(login_window_V2,font = "1",fg="grey",bd=0)
entry_password.insert(0, "Enter password ")
b=entry_password
b.bind('<FocusIn>', remove1)
btn_cancel=Button(signup_PW_H2,text='Cancel',bd="1",width=10,command=main_window.destroy,fg="black")
btn_submit=Button(signup_PW_H2,text='Submit',bd="1",width=10,command=btn_submit_click,fg="black")
btn_signup=Button(signup_PW_H2,text='SignUp',bd="1",width=10,command=btn_signup_click,fg="black")
login_window_V1.add(lbl_username)
login_window_V1.add(lbl_pass)
login_window_V2.add(entry_username)
login_window_V2.add(entry_password)
login_window_H1.add(login_window_V1)
login_window_H1.add(login_window_V2)
signup_PW_H2.add(btn_submit)
signup_PW_H2.add(btn_signup)
signup_PW_H2.add(btn_cancel)
login_window_V0.add(PanedWindow(login_window ,orient = VERTICAL) )
login_window_V0.add(login_window_H1)
login_window_V0.add(signup_PW_H2)
# login_window_V1.add(lbl_name)

###############################################################################
# signup window design
###############################################################################
signup_TL= Toplevel()
signup_TL.geometry("400x410")
signup_TL.withdraw()
signup_PW_H = PanedWindow(signup_TL)
signup_PW_V = PanedWindow(signup_PW_H,orient = VERTICAL)
signup_PW_V1 = PanedWindow(signup_PW_H,orient = VERTICAL)
signup_PW_H.pack()
signup_PW_H.add(signup_PW_V)
signup_PW_H.add(signup_PW_V1)
btn_su_submit = Button(signup_PW_V,text='Submit',bd="1", command =btn_su_submit_click) #btn_su_submit_click
lbl_su_serialno=Label(signup_PW_V,text="serialno.")
lbl_su_name=Label(signup_PW_V,text="Name")
lbl_su_username=Label(signup_PW_V,text="Username")
lbl_su_address=Label(signup_PW_V,text="Adress")
lbl_su_class=Label(signup_PW_V,text="Class")
lbl_su_subject=Label(signup_PW_V,text="subject")
lbl_su_contact=Label(signup_PW_V,text="Contact")
lbl_su_email=Label(signup_PW_V,text="Email id")
lbl_su_gender=Label(signup_PW_V,text="Gender")
lbl_su_pass=Label(signup_PW_V,text="Password")
lbl_su_cpass=Label(signup_PW_V,text="Confirm Password")
entry_su_serialno=Entry(signup_PW_V1,text="serialno",font = "1",bd=1)
entry_su_username=Entry(signup_PW_V1,text="Username",font = "1",bd=1)
entry_su_name=Entry(signup_PW_V1,text="name",font = "1",bd=1)
entry_su_gender=Entry(signup_PW_V1,text="gender",font = "1",bd=1)
entry_su_address=Entry(signup_PW_V1,text="address",bd=1)
entry_su_class=Entry(signup_PW_V1,text="class",bd=1,font = "1")
entry_su_subject = Entry(signup_PW_V1,text="subject",bd=1)
entry_su_contact=Entry(signup_PW_V1,text="contact",bd=1)
entry_su_email=Entry(signup_PW_V1,text="email",bd=1)
entry_su_pass=Entry(signup_PW_V1,text="Password",font = "1",bd=1)
entry_su_cpass=Entry(signup_PW_V1,text="Confirm Password",font = "1",bd=1)
signup_PW_V.add(lbl_su_serialno)
signup_PW_V.add(lbl_su_name)
signup_PW_V.add(lbl_su_username)
signup_PW_V.add(lbl_su_address)
signup_PW_V.add(lbl_su_class)
signup_PW_V.add(lbl_su_subject)
signup_PW_V.add(lbl_su_contact)
signup_PW_V.add(lbl_su_email)
signup_PW_V.add(lbl_su_gender)
signup_PW_V.add(lbl_su_pass)
signup_PW_V.add(lbl_su_cpass)
signup_PW_V.add(btn_su_submit)
signup_PW_V1.add(entry_su_serialno)
signup_PW_V1.add(entry_su_name)
signup_PW_V1.add(entry_su_username)
signup_PW_V1.add(entry_su_address)
signup_PW_V1.add(entry_su_class)
signup_PW_V1.add(entry_su_subject)
signup_PW_V1.add(entry_su_contact)
signup_PW_V1.add(entry_su_email)
signup_PW_V1.add(entry_su_gender)
signup_PW_V1.add(entry_su_pass)
signup_PW_V1.add(entry_su_cpass)
signup_PW_V1.add(Label(signup_PW_V1,text=""))
###############################################################################
# add student data
###############################################################################
add_details_TL= Toplevel()
add_details_TL.geometry("350x300")
add_details_TL.withdraw()
add_PW_H = PanedWindow(add_details_TL)
add_PW_V = PanedWindow(add_PW_H,orient = VERTICAL)
add_PW_V1 = PanedWindow(add_PW_H,orient = VERTICAL)
add_PW_H.pack()
add_PW_H.add(add_PW_V)
add_PW_H.add(add_PW_V1)
# #
btn_ad_submit =Button(add_PW_V,text='Submit',bd="1",command=btn_ad_submit_click)
lbl_ad_serialno2=Label(add_PW_V,text="Rollno.")
lbl_ad_name2=Label(add_PW_V,text="Name")
lbl_ad_userage2=Label(add_PW_V,text="Age")
lbl_ad_gender2=Label(add_PW_V,text="Gender")
lbl_ad_address2=Label(add_PW_V,text="Adress")
lbl_ad_class2=Label(add_PW_V,text="Class")
lbl_ad_contact2=Label(add_PW_V,text="Contact")
lbl_ad_email2=Label(add_PW_V,text="Email id")
lbl_ad_dob2=Label(add_PW_V,text="Date of birh")
lbl_ad_doa2=Label(add_PW_V,text="Date of admission")
entry_ad_serialno2=Entry(add_PW_V1,text="Rollno",font = "1",bd=1)
entry_ad_name2=Entry(add_PW_V1,text="name",font = "1",bd=1)
entry_ad_userage2=Entry(add_PW_V1,text="age",font = "1",bd=1)
entry_ad_gender2=Entry(add_PW_V1,text="gender",font = "1",bd=1)
entry_ad_address2=Entry(add_PW_V1,text="address",bd=1)
entry_ad_class2=Entry(add_PW_V1,text="class",bd=1,font = "1")
entry_ad_contact2=Entry(add_PW_V1,text="contact",bd=1)
entry_ad_email2=Entry(add_PW_V1,text="email",bd=1)
entry_ad_dob2=Entry(add_PW_V1,text="Date of birth",bd=1)
entry_ad_doa2=Entry(add_PW_V1,text="Date of admission",bd=1)
add_PW_V.add(lbl_ad_serialno2)
add_PW_V.add(lbl_ad_name2)
add_PW_V.add(lbl_ad_address2)
add_PW_V.add(lbl_ad_userage2)
add_PW_V.add(lbl_ad_class2)
add_PW_V.add(lbl_ad_contact2)
add_PW_V.add(lbl_ad_email2)
add_PW_V.add(lbl_ad_gender2)
add_PW_V.add(lbl_ad_dob2)
add_PW_V.add(lbl_ad_doa2)
add_PW_V.add(btn_ad_submit)
add_PW_V1.add(entry_ad_serialno2)
add_PW_V1.add(entry_ad_name2)
add_PW_V1.add(entry_ad_address2)
add_PW_V1.add(entry_ad_userage2)
add_PW_V1.add(entry_ad_class2)
add_PW_V1.add(entry_ad_contact2)
add_PW_V1.add(entry_ad_email2)
add_PW_V1.add(entry_ad_gender2)
add_PW_V1.add(entry_ad_dob2)
add_PW_V1.add(entry_ad_doa2)
add_PW_V1.add(Label(add_PW_V1,text=""))
login_window.protocol("WM_DELETE_WINDOW", on_closing)
signup_TL.protocol("WM_DELETE_WINDOW", on_closing)
main_window.protocol("WM_DELETE_WINDOW", on_closing)
login_window.mainloop()