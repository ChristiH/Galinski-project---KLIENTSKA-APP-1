import tkinter as tk

h=720
w=1280

root = tk.Tk()
canv = tk.Canvas(root,width=w,height=h)
canv.pack()
def frame1():
    global frame, can
    frame = tk.Frame(root, bg='white',width=w,height=h)
    frame.place(x=0,y=0)
    can = tk.Canvas(frame,width=w,height=h)
    can.pack()
frame1()
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
    global frame, can, Lb1
    frame.destroy
    can.destroy
    frame = tk.Frame(root, bg='white',width=w,height=h)
    frame.place(x=0,y=0)
    can = tk.Canvas(frame,width=w,height=h)
    can.pack()
    Lb1 = tk.Listbox(frame, width=43, height = 8, font='Arial 13',selectmode='SINGLE', xscrollcommand=True)
    Lb1.insert(1, "BEZNY UCET, SK68 0651 0000 0000 0000 0000")
    Lb1.insert(2, "FIREMNY UCET, SK68 0651 0000 0000 0000 0000")
    Lb1.place(x=20,y=70)
    Lb2 = tk.Listbox(frame, width=43, height = 8, font='Arial 13',selectmode='SINGLE', xscrollcommand=True)
    Lb2.insert(1, "KREDITNA KARTA, dlh = 120$")
    Lb2.insert(2, "DEBETNA KARTA")
    Lb2.place(x=(w//3)*2+20,y=70)
    button1=tk.Button(frame,text='TRANSAKCIA',command=frame2)
    button1.place(width=200,height=25,x=w//6-100,y=430)
    button2=tk.Button(frame,text='PLATOBNY PRIKAZ',command=frame2)
    button2.place(width=200,height=25,x=w//6-100,y=480)
    button3=tk.Button(frame,text='PRIJMY',command=frame2)
    button3.place(width=200,height=25,x=w//6-100,y=530)
    button4=tk.Button(frame,text='potvrdit platbu',command=frame2)
    button4.place(width=200,height=25,x=w//2-100,y=210)
    button5=tk.Button(frame,text='splatit dlh',command=frame2)
    button5.place(width=200,height=25,x=(w//6)*5-100,y=240)
    E1 = tk.Entry(frame)
    E1.place(width=200,height=25,x=w//2-100,y=100)
    E2 = tk.Entry(frame)
    E2.place(width=200,height=25,x=w//2-100,y=170)
    can.create_text(w//2,80,text='Prijemca')
    can.create_text(w//2,150,text='Suma')
    can.create_text(w//6,40,text='ÚČTY',font='Arial 25')
    can.create_text(w//2,40,text='PLATOBNY PRIKAZ',font='Arial 25')
    can.create_text((w//6)*5,40,text='KARTY',font='Arial 25')
    can.create_text(w//6,300,text='zostatok na ucte: 1234$6',font='Arial 20')

    
def login():
    button=tk.Button(frame,text='BUTONIK',command=frame2)
    button.place(width=200,x=w//2-100,y=h//2+50)
    entry=tk.Entry(frame,width=200)
    entry.place(width=60,x=w//2-30,y=h//2+20)
    round_rectangle(400, 200, w-400, h-200, radius=50)
    can.create_text(w//2,h//2-20,text='LOGIN',font='Arial 30')


#.............................
login()

