import tkinter as tk



h=720

w=1280



root = tk.Tk()

can = tk.Canvas(root,width=w,height=h)

can.pack()







def round_rectangle(x1, y1, x2, y2, radius=50, **kwargs):



    points = [x1+radius, y1,

              x1+radius, y1,

              x2-radius, y1,

              x2-radius, y1,

              x2, y1,

              x2, y1+radius,

              x2, y1+radius,

              x2, y2-radius,

              x2, y2-radius,

              x2, y2,

              x2-radius, y2,

              x2-radius, y2,

              x1+radius, y2,

              x1+radius, y2,

              x1, y2,

              x1, y2-radius,

              x1, y2-radius,

              x1, y1+radius,

              x1, y1+radius,

              x1, y1]



    return can.create_polygon(points, **kwargs, smooth=True,fill='#c4ffef')



def frame2():
    global prihlasit_btn, ID_entry, ucty_list,karty_list,transakcia_btn,platprik_btn,potvrdplatbu_btn,prijmy_btn,splatdlh_btn,prijemca_entry,suma_entry
    can.delete('all')
    prihlasit_btn.destroy()
    ID_entry.destroy()

    

    ucty_list = tk.Listbox(root, width=43, height = 8, font='Arial 13',selectmode='SINGLE', xscrollcommand=True)
    ucty_list.insert(1, "BEZNY UCET, SK68 0651 0000 0000 0000 0000")
    ucty_list.insert(2, "FIREMNY UCET, SK68 0651 0000 0000 0000 0000")
    ucty_list.place(x=20,y=70)


    karty_list = tk.Listbox(root, width=43, height = 8, font='Arial 13',selectmode='SINGLE', xscrollcommand=True)
    karty_list.insert(1, "KREDITNA KARTA, dlh = 120$")
    karty_list.insert(2, "DEBETNA KARTA")
    karty_list.place(x=(w//3)*2+20,y=70)


    transakcia_btn=tk.Button(root,text='TRANSAKCIA',command=frame3)
    transakcia_btn.place(width=200,height=25,x=w//6-100,y=430)

    

    platprik_btn=tk.Button(root,text='PLATOBNY PRIKAZ',command=frame2)
    platprik_btn.place(width=200,height=25,x=w//6-100,y=480)

    

    prijmy_btn=tk.Button(root,text='PRIJMY',command=frame2)
    prijmy_btn.place(width=200,height=25,x=w//6-100,y=530)

    

    potvrdplatbu_btn=tk.Button(root,text='potvrdit platbu',command=frame2)
    potvrdplatbu_btn.place(width=200,height=25,x=w//2-100,y=210)

    

    splatdlh_btn=tk.Button(root,text='splatit dlh',command=frame2)
    splatdlh_btn.place(width=200,height=25,x=(w//6)*5-100,y=240)

    

    prijemca_entry = tk.Entry(root)
    prijemca_entry.place(width=200,height=25,x=w//2-100,y=100)

    

    suma_entry = tk.Entry(root)
    suma_entry.place(width=200,height=25,x=w//2-100,y=170)

    

    can.create_text(w//2,80,text='Prijemca')

    can.create_text(w//2,150,text='Suma')

    can.create_text(w//6,40,text='ÚČTY',font='Arial 25')

    can.create_text(w//2,40,text='PLATOBNY PRIKAZ',font='Arial 25')

    can.create_text((w//6)*5,40,text='KARTY',font='Arial 25')

    can.create_text(w//6,300,text='zostatok na ucte: 1234$6',font='Arial 20')



##    round_rectangle(400, 200, w-400, h-200, radius=50)

##    round_rectangle(400, 200, w-400, h-200, radius=50)

##    round_rectangle(400, 200, w-400, h-200, radius=50)

from tkinter import *
def frame3():
    global prihlasit_btn, ID_entry, ucty_list,karty_list,transakcia_btn,platprik_btn,potvrdplatbu_btn,prijmy_btn,splatdlh_btn,prijemca_entry,suma_entry,can
    can.delete('all')
    ucty_list.destroy()
    karty_list.destroy()
    transakcia_btn.destroy()
    platprik_btn.destroy()
    prijmy_btn.destroy()
    potvrdplatbu_btn.destroy()
    splatdlh_btn.destroy()
    prijemca_entry.destroy()
    suma_entry.destroy()
    
    window=can
    window = Tk() # create window
    window.configure(bg='white')
    window.title("Transakcie")
    window.geometry("1280x720")
    lbl1 = Label(window, text="Transakcie", fg='black', font=("Arial 13 bold"))
    lbl1.grid(row=0, column=0, sticky=W)
    
    frm = Frame(window)
    frm.grid(row=1, column=0, sticky=N+S)

    window.rowconfigure(1, weight=1)
    window.columnconfigure(1, weight=1)
    scrollbar = Scrollbar(frm, orient="vertical")
    scrollbar.pack(side=RIGHT, fill=Y)
    listNodes = Listbox(frm, width=60, yscrollcommand=scrollbar.set, font=("Arial", 12))
    listNodes.pack(expand=True, fill=Y)
    scrollbar.config(command=listNodes.yview)


    for x in range(100):
        
        listNodes.insert(END, 'Ucet'+100*' ' +'Ostatok')
        listNodes.insert(END, 'Komu')
        listNodes.insert(END, '')

    #graf + a -


##    transakcia=suma
##    p=transakcia//10
##    if transakcia>0:
##        can.create_rectangle(700,600,800,600-p*10,fill='green')
##    else:
##        can.create_rectangle(w-330,h-100,w-230,h-100-20-p,fill='red')
    root.mainloop()
 

def login():

    global prihlasit_btn, ID_entry
    prihlasit_btn=tk.Button(root,text='PRIHLASIT SA',command=frame2)
    prihlasit_btn.place(width=200,x=w//2-100,y=h//2+50)



    ID_entry=tk.Entry(root,width=200)
    ID_entry.place(width=60,x=w//2-30,y=h//2+20)

    

    round_rectangle(400, 200, w-400, h-200, radius=50)
    can.create_text(w//2,h//2-20,text='LOGIN',font='Arial 30')

login()



#bez frame, vandak style riesenie na widgety :D menej prace, menej errorov...
