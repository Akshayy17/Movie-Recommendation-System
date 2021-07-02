import tkinter as tk
from tkinter import ttk
from tkinter import StringVar, font, IntVar
from ttkbootstrap import Style
from tkinter.constants import ACTIVE, ANCHOR, CENTER, DISABLED, E, END, GROOVE, HORIZONTAL, LEFT, N, RAISED, RIDGE, RIGHT, S, SUNKEN, W
import numpy

from database import Top_List

def CheckState(x):
    if(x.get()[-1] == 'Y'):
        genre_set.add(x.get()[:-1:])
        print(genre_set)

    else:
        genre_set.remove(x.get()[:-1:])
        print(genre_set)

def Button_1():
    tree.delete(*tree.get_children())

    q_movies = Top_List()
    #df = q_movies['title'].tolist()
    #print(df)
    for item in q_movies['title']:
        #print(item)
        tree.insert('', 'end', values=(item,))#------------------------------------------Important(item,)---See screenshot - 02-07-21
    #for index, row in q_movies.iterrows():
     #   tree.insert("",0,text=index,values=list(row))

    #print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(5))

def Button_2():
    tree.delete(*tree.get_children())

    print('btn2')

def Button_3():
    print('btn2')

def Button_4():
    print('btn2')

#if __name__ == '__main__':
root = tk.Tk()
root.title('Movie Recommender System')
root.geometry('1100x670')
root.resizable(0,0)

style = Style(theme = 'lumen')
#style.configure('.', font = ('Helvetica', 50))
##########################################
genre_set = set()
##########################################
upper_panel = tk.Frame(root, height=35, width=1100, bg='#ed522b')#, style='info.TFrame')
upper_panel.place(x=0, y=0)
left_panel = tk.Frame(root, height=670, width=300, bg='#e3e3e3')#, style='secondary.TFrame')
left_panel.place(x=0, y=0)

_x, _y = 0, 10

lab_1 = tk.Label(root, text = 'Top Rated Collection', anchor=CENTER, font=('Impact', 12), bg= '#a6a6a6', fg='#fafafa', padx=5, pady=5)#, style='TLabel')
lab_1.place(x=73, y=10)
style.configure('a.primary.Outline.TButton', font=('Helvetica',20), padding=2, width=8)
btn_1 = ttk.Button(root, text='Search', style='a.primary.Outline.TButton', command=Button_1)
btn_1.place(x=82, y=60)

tk.Frame(root, height=3, width=280, bg='#437291').place(x=10, y=118)

lab_1 = tk.Label(root, text = 'Genre Search', anchor=CENTER, font=('Impact', 13), bg= '#a6a6a6', fg='#fafafa', padx=5, pady=5)#, style='TLabel')
lab_1.place(x=_x+95, y=_y+130)
style.configure('warning.Outline.Toolbutton', font=('Helvetica',12), padding=5)#, width=8)
chb1 = StringVar()
chbtn_1 = ttk.Checkbutton(root, text='Action', style='warning.Outline.Toolbutton', variable=chb1, onvalue='actionY', offvalue='actionN', command=lambda: CheckState(chb1))
chbtn_1.place(x=_x+5, y=_y+180)
chb2 = StringVar()
chbtn_2 = ttk.Checkbutton(root, text='Comedy', style='warning.Outline.Toolbutton', variable=chb2, onvalue='comedyY', offvalue='comedyN', command=lambda: CheckState(chb2))
chbtn_2.place(x=_x+75, y=_y+180)
chb3 = StringVar()
chbtn_3 = ttk.Checkbutton(root, text='Thriller', style='warning.Outline.Toolbutton', variable=chb3, onvalue='thrillerY', offvalue='thrillerN', command=lambda: CheckState(chb3))
chbtn_3.place(x=_x+159, y=_y+180)
chb4 = StringVar()
chbtn_4 = ttk.Checkbutton(root, text='Drama', style='warning.Outline.Toolbutton', variable=chb4, onvalue='dramaY', offvalue='dramaN', command=lambda: CheckState(chb4))
chbtn_4.place(x=_x+230, y=_y+180)
chb5 = StringVar()
chbtn_5 = ttk.Checkbutton(root, text='Adventure', style='warning.Outline.Toolbutton', variable=chb5, onvalue='adventureY', offvalue='adventureN', command=lambda: CheckState(chb5))
chbtn_5.place(x=_x+20, y=_y+222)
chb6 = StringVar()
chbtn_6 = ttk.Checkbutton(root, text='Animation', style='warning.Outline.Toolbutton', variable=chb6, onvalue='animationY', offvalue='animationN', command=lambda: CheckState(chb6))
chbtn_6.place(x=_x+115, y=_y+222)
chb7 = StringVar()
chbtn_7 = ttk.Checkbutton(root, text='History', style='warning.Outline.Toolbutton', variable=chb7, onvalue='historyY', offvalue='historyN', command=lambda: CheckState(chb7))
chbtn_7.place(x=_x+210, y=_y+222)
chb8 = StringVar()
chbtn_8 = ttk.Checkbutton(root, text='Family', style='warning.Outline.Toolbutton', variable=chb8, onvalue='familyY', offvalue='familyN', command=lambda: CheckState(chb8))
chbtn_8.place(x=_x+5, y=_y+264)
chb9 = StringVar()
chbtn_9 = ttk.Checkbutton(root, text='Horror', style='warning.Outline.Toolbutton', variable=chb9, onvalue='horrorY', offvalue='horrorN', command=lambda: CheckState(chb9))
chbtn_9.place(x=_x+75, y=_y+264)
chb10 = StringVar()
chbtn_10 = ttk.Checkbutton(root, text='Fantasy', style='warning.Outline.Toolbutton', variable=chb10, onvalue='fantasyY', offvalue='fantasyN', command=lambda: CheckState(chb10))
chbtn_10.place(x=_x+145, y=_y+264)
chb11 = StringVar()
chbtn_11 = ttk.Checkbutton(root, text='Mistery', style='warning.Outline.Toolbutton', variable=chb11, onvalue='mysteryY', offvalue='misteryN', command=lambda: CheckState(chb11))
chbtn_11.place(x=_x+225, y=_y+264)
style.configure('success.Outline.TButton', font=('Helvetica',15), padding=2, width=8)
btn_2 = ttk.Button(root, text='Search', style='success.Outline.TButton', command=Button_2)
btn_2.place(x=100, y=320)

tk.Frame(root, height=3, width=280, bg='#437291').place(x=10, y=370)

lab_1 = tk.Label(root, text = 'IMDB Rated', anchor=CENTER, font=('Impact', 13), bg= '#a6a6a6', fg='#fafafa', padx=5, pady=5)#, style='TLabel')
lab_1.place(x=100, y=390)
lab_1 = tk.Label(root, text = 'Above:', anchor=CENTER, font=('Helvetica', 13), bg= '#e3e3e3', fg='#383838', padx=5, pady=5)#, style='TLabel')
lab_1.place(x=5, y=440)
sb_value = tk.DoubleVar()
sb = ttk.Spinbox(root, from_=0.0, to=10.0, width=5, values=(0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10), textvariable=sb_value, wrap = False, style= 'info.TSpinbox')
sb.delete(0,"end")
sb.insert(0,7)
sb.config(state='readonly')
sb.place(x=70, y=440)
style.configure('success.TButton', font=('Helvetica',14), padding=2, width=6)
btn_3 = ttk.Button(root, text='Search', style='success.TButton', command=Button_3)
btn_3.place(x=190, y=440)

tk.Frame(root, height=3, width=280, bg='#437291').place(x=10, y=500)

lab_1 = tk.Label(root, text = 'Similarity Search', anchor=CENTER, font=('Impact', 13), bg= '#a6a6a6', fg='#fafafa', padx=5, pady=5)#, style='TLabel')
lab_1.place(x=77, y=520)
style.configure('danger.Outline.TButton', font=('Helvetica',16), padding=2, width=5)
btn_4 = ttk.Button(root, text='Go', style='danger.Outline.TButton', command=Button_4).place(x=115, y=590)

style.configure('primary.Treeview', font=('helvetica', 13))
style.configure('.', font = ('Helvetica', 20))
tree = ttk.Treeview(root, columns='#1', selectmode='extended', show='headings', height=27, style='primary.Treeview')
tree.column("#1", minwidth=0, width=750, stretch=tk.NO)
tree.heading('#1', text ='Search Results')
tree.place(x=325, y=56)

p ='Click the Button on the left panel for respetive Criterion search'
tree.insert('', END, values=(p,))

sb = ttk.Scrollbar(root,  orient=tk.VERTICAL, command=tree.yview)
#tree.configure(yscroll=scrollbar.set)
tree['yscrollcommand'] = sb.set
sb.place(x=1059, y=105, height=540)

root.mainloop()