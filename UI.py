from random import sample
from math import floor
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter.messagebox as Msb
import urllib.request
import base64

class BlackJack(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.DisableType(False)
        self.itemTale = [2,3,4,5,6,7,8,9,"J","Q","K","A"]
        #print(self.table.item("1"))

    def initUI(self):
        self.parent.title("Calculate BlackJack - By: SaviorXXI")
        URL = "https://i.imgur.com/0b7fFYj.png"
        u = urllib.request.urlopen(URL)
        raw_data = u.read()
        u.close()
        #img = tk.Image(raw_data)
        b64_data = base64.encodestring(raw_data)
        image = tk.PhotoImage(data=b64_data)
        #.parent.iconbitmap(default = image)
        self.parent.resizable(0, 0)
        self.parent.tk.call('wm', 'iconphoto', self.parent._w, image)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
            background="#F3F3F3",
            foreground="black",
            rowheight=25,
            fieldbackground="#F3F3F3"
            )
        style.map('Treeview',background=[('selected', 'green')])
        style.configure('TButton', font =
                    ('calibri', 20, 'bold'),
                            borderwidth = '4')
        style.map('TButton', foreground = [('active', '!disabled', 'green')],
                            background = [('active', 'black')])

        self.frame_1 = Frame(self.parent, relief=RAISED, borderwidth=1)
        #self.frame_1.grid(fill=X, padx=0, pady=0)
        self.frame_1.grid(row=0, column=0, rowspan=6, sticky="nsew")

        self.button_2 = Button(
            self.frame_1, text="2", width=5, height=3, command=self.Send_2)
        self.button_2.grid(row=0, column=0, rowspan=2, padx=5, pady=5)

        self.button_3 = Button(
            self.frame_1, text="3", width=5, height=3, command=self.Send_3)
        self.button_3.grid(row=0, column=1, rowspan=2, padx=5, pady=5)

        self.button_4 = Button(
            self.frame_1, text="4", width=5, height=3, command=self.Send_4)
        self.button_4.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        self.button_5 = Button(
            self.frame_1, text="5", width=5, height=3, command=self.Send_5)
        self.button_5.grid(row=0, column=3, rowspan=2, padx=5, pady=5)

        self.button_6 = Button(
            self.frame_1, text="6", width=5, height=3, command=self.Send_6)
        self.button_6.grid(row=0, column=4, rowspan=2, padx=5, pady=5)

        self.button_7 = Button(
            self.frame_1, text="7", width=5, height=3, command=self.Send_7)
        self.button_7.grid(row=2, column=0, rowspan=2, padx=5, pady=5)

        self.button_8 = Button(
            self.frame_1, text="8", width=5, height=3, command=self.Send_8)
        self.button_8.grid(row=2, column=1, rowspan=2, padx=5, pady=5)

        self.button_9 = Button(
            self.frame_1, text="9", width=5, height=3, command=self.Send_9)
        self.button_9.grid(row=2, column=2, rowspan=2, padx=5, pady=5)

        self.button_10 = Button(
            self.frame_1, text="10", width=5, height=3, command=self.Send_10)
        self.button_10.grid(row=4, column=0, rowspan=2, padx=5, pady=5)

        self.button_J = Button(
            self.frame_1, text="J", width=5, height=3, command=self.Send_J)
        self.button_J.grid(row=4, column=1, rowspan=2, padx=5, pady=5)

        self.button_Q = Button(
            self.frame_1, text="Q", width=5, height=3, command=self.Send_Q)
        self.button_Q.grid(row=4, column=2, rowspan=2, padx=5, pady=5)

        self.button_K = Button(
            self.frame_1, text="K", width=5, height=3, command=self.Send_K)
        self.button_K.grid(row=4, column=3, rowspan=2, padx=5, pady=5)

        self.button_A = Button(
            self.frame_1, text="A", width=5, height=3, command=self.Send_A)
        self.button_A.grid(row=4, column=4, rowspan=2, padx=5, pady=5)

        self.frame_4 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame_4.grid(row=6, column=0, rowspan=2, sticky="nsew")

        self.button_hearts = Button(
            self.frame_4, text="♡", width=5, height=3, command=self.Send_hearts)
        self.button_hearts.grid(row=6, column=0, padx=5, pady=5)

        self.button_diamonds = Button(
            self.frame_4, text="♢", width=5, height=3, command=self.Send_diamonds)
        self.button_diamonds.grid(row=6, column=1, padx=5, pady=5)

        self.button_clubs = Button(
            self.frame_4, text="♣", width=5, height=3, command=self.Send_clubs)
        self.button_clubs.grid(row=6, column=2, padx=5, pady=5)

        self.button_spade = Button(
            self.frame_4, text="♠", width=5, height=3, command=self.Send_spade)
        self.button_spade.grid(row=6, column=3, padx=5, pady=5)

        self.frame_5 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame_5.grid(row=0, column=1, rowspan=8, sticky="nsew")

        self.label_value_countC = Label(
            self.frame_5, text="0", anchor='w', font=("Courier", 25))
        self.label_value_countC.grid(row=0, column=0, padx=5, pady=12)
        self.label_value_countC.config(fg="green")

        self.button_plus = Button(
            self.frame_5, text="Add", width=5, height=3, command=self.AddLast)
        self.button_plus.grid(row=2, column=0, rowspan=2, padx=5, pady=5)

        self.button_delete_one = Button(
            self.frame_5, text="Del", width=5, height=3, command=self.DeleteOneCard)
        self.button_delete_one.grid(row=4, column=0, rowspan=2, padx=5, pady=5)

        self.button_cal = Button(
            self.frame_5, text="ShC", width=5, height=3, command=self.ShuffleCards)
        self.button_cal.grid(row=6, column=0, rowspan=2, padx=5, pady=5)

        self.frame_9 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame_9.grid(row=0, column=2, rowspan=8, sticky="nsew")

        self.label_p1 = Label(
            self.frame_9, text="Player 1:", anchor='w')
        self.label_p1.grid(row=0, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p1 = StringVar(self.parent, value='')
        self.input_p1 = Entry(
            self.frame_9, textvariable=self.value_p1, width=20)
        self.input_p1.grid(row=0, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p2 = Label(
            self.frame_9, text="Player 2:", anchor='w')
        self.label_p2.grid(row=1, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p2 = StringVar(self.parent, value='')
        self.input_p2 = Entry(
            self.frame_9, textvariable=self.value_p2, width=20)
        self.input_p2.grid(row=1, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p3 = Label(
            self.frame_9, text="Player 3:", anchor='w')
        self.label_p3.grid(row=2, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p3 = StringVar(self.parent, value='')
        self.input_p3 = Entry(
            self.frame_9, textvariable=self.value_p3, width=20)
        self.input_p3.grid(row=2, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p4 = Label(
            self.frame_9, text="Player 4:", anchor='w')
        self.label_p4.grid(row=3, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p4 = StringVar(self.parent, value='')
        self.input_p4 = Entry(
            self.frame_9, textvariable=self.value_p4, width=20)
        self.input_p4.grid(row=3, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p5 = Label(
            self.frame_9, text="Player 5:", anchor='w')
        self.label_p5.grid(row=4, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p5 = StringVar(self.parent, value='')
        self.input_p5 = Entry(
            self.frame_9, textvariable=self.value_p5, width=20)
        self.input_p5.grid(row=4, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p6 = Label(
            self.frame_9, text="Player 6:", anchor='w')
        self.label_p6.grid(row=5, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p6 = StringVar(self.parent, value='')
        self.input_p6 = Entry(
            self.frame_9, textvariable=self.value_p6, width=20)
        self.input_p6.grid(row=5, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p7 = Label(
            self.frame_9, text="Player 7:", anchor='w')
        self.label_p7.grid(row=6, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p7 = StringVar(self.parent, value='')
        self.input_p7 = Entry(
            self.frame_9, textvariable=self.value_p7, width=20)
        self.input_p7.grid(row=6, column=1, padx=5, pady=6, sticky="nsew")

        self.label_dl = Label(
            self.frame_9, text="Dealer:", anchor='w')
        self.label_dl.grid(row=7, column=0, padx=5, pady=6, sticky="nsew")
        self.value_dl = StringVar(self.parent, value='')
        self.input_dl = Entry(
            self.frame_9, textvariable=self.value_dl, width=20)
        self.input_dl.grid(row=7, column=1, padx=5, pady=6, sticky="nsew")

        self.frame_8 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame_8.grid(row=0, column=4, columnspan=3, rowspan=7, sticky="nsew")

        self.label_p1_2 = Label(
            self.frame_8, text="1H2:", anchor='w')
        self.label_p1_2.grid(row=0, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p1_2 = StringVar(self.parent, value='')
        self.input_p1_2 = Entry(
            self.frame_8, textvariable=self.value_p1_2, width=20)
        self.input_p1_2.grid(row=0, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p2_2 = Label(
            self.frame_8, text="2H2:", anchor='w')
        self.label_p2_2.grid(row=1, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p2_2 = StringVar(self.parent, value='')
        self.input_p2_2 = Entry(
            self.frame_8, textvariable=self.value_p2_2, width=20)
        self.input_p2_2.grid(row=1, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p3_2 = Label(
            self.frame_8, text="3H2:", anchor='w')
        self.label_p3_2.grid(row=2, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p3_2 = StringVar(self.parent, value='')
        self.input_p3_2 = Entry(
            self.frame_8, textvariable=self.value_p3_2, width=20)
        self.input_p3_2.grid(row=2, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p4_2 = Label(
            self.frame_8, text="4H2:", anchor='w')
        self.label_p4_2.grid(row=3, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p4_2 = StringVar(self.parent, value='')
        self.input_p4_2 = Entry(
            self.frame_8, textvariable=self.value_p4_2, width=20)
        self.input_p4_2.grid(row=3, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p5_2 = Label(
            self.frame_8, text="5H2:", anchor='w')
        self.label_p5_2.grid(row=4, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p5_2 = StringVar(self.parent, value='')
        self.input_p5_2 = Entry(
            self.frame_8, textvariable=self.value_p5_2, width=20)
        self.input_p5_2.grid(row=4, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p6_2 = Label(
            self.frame_8, text="6H2:", anchor='w')
        self.label_p6_2.grid(row=5, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p6_2 = StringVar(self.parent, value='')
        self.input_p6_2 = Entry(
            self.frame_8, textvariable=self.value_p6_2, width=20)
        self.input_p6_2.grid(row=5, column=1, padx=5, pady=6, sticky="nsew")

        self.label_p7_2 = Label(
            self.frame_8, text="7H2:", anchor='w')
        self.label_p7_2.grid(row=6, column=0, padx=5, pady=6, sticky="nsew")
        self.value_p7_2 = StringVar(self.parent, value='')
        self.input_p7_2 = Entry(
            self.frame_8, textvariable=self.value_p7_2, width=20)
        self.input_p7_2.grid(row=6, column=1, padx=5, pady=6, sticky="nsew")

        self.frame_9 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame_9.grid(row=7, column=4, columnspan=3, rowspan=9, sticky="nsew")

        self.tableLast = ttk.Treeview(self.frame_9, height= 16)
        self.tableLast['columns'] = ('lastCard')

        self.tableLast.column("#0", width=0,  stretch=NO)
        self.tableLast.column("lastCard", anchor=CENTER, width=85)

        self.tableLast.heading("#0", text="", anchor=CENTER)
        self.tableLast.heading("lastCard", text="Last Card", anchor=CENTER)

        self.tableLast.grid(row=0, column=0,padx=5, pady=5)

        self.tablePre = ttk.Treeview(self.frame_9, height= 16)
        self.tablePre['columns'] = ('nextCard')

        self.tablePre.column("#0", width=0,  stretch=NO)
        self.tablePre.column("nextCard", anchor=CENTER, width=85)

        self.tablePre.heading("#0", text="", anchor=CENTER)
        self.tablePre.heading("nextCard", text="Next Card", anchor=CENTER)

        self.tablePre.grid(row=0, column=1,padx=5, pady=5)

        self.frame_6 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame_6.grid(row=9, columnspan=4, sticky="nsew")

        self.label_shuffletimes = Label(
            self.frame_6, text="Shuffle Time:", anchor='w')
        self.label_shuffletimes.grid(row=0, column=0, padx=5, pady=6, sticky="nsew")
        self.value_shuffletimes = StringVar(self.parent, value='6')
        self.input_shuffletimes = Entry(
            self.frame_6, textvariable=self.value_shuffletimes, width=17)
        self.input_shuffletimes.grid(row=0, column=1, padx=5, pady=6, sticky="nsew")

        self.label_splitletimes = Label(
            self.frame_6, text="Split Time:", anchor='w')
        self.label_splitletimes.grid(row=0, column=2, padx=5, pady=6, sticky="nsew")
        self.value_splitletimes = StringVar(self.parent, value='6')
        self.input_splitletimes = Entry(
            self.frame_6, textvariable=self.value_splitletimes, width=20)
        self.input_splitletimes.grid(row=0, column=3, padx=5, pady=6, sticky="nsew")

        self.button_rs = Button(
            self.frame_6, text="Reset", width=15, command=self.ResetAll)
        self.button_rs.grid(row=0, column=4, rowspan=2, padx=5, pady=5)

        self.frame_5 = Frame(self.parent, relief=RAISED, borderwidth=1)
        self.frame_5.grid(row=11, column=0, columnspan=3, sticky="nsew")

        self.table = ttk.Treeview(self.frame_5, height= 13)

        self.table['columns'] = (
            'card', 'hearts', 'diamonds', 'clubs', 'spade')

        self.table.column("#0", width=0,  stretch=NO)
        self.table.column("card", anchor=CENTER, width=105)
        self.table.column("hearts", anchor=CENTER, width=105)
        self.table.column("diamonds", anchor=CENTER, width=105)
        self.table.column("clubs", anchor=CENTER, width=105)
        self.table.column("spade", anchor=CENTER, width=105)

        self.table.heading("#0", text="", anchor=CENTER)
        self.table.heading("card", text="Card", anchor=CENTER)
        self.table.heading("hearts", text="♡", anchor=CENTER)
        self.table.heading("diamonds", text="♢", anchor=CENTER)
        self.table.heading("clubs", text="♣", anchor=CENTER)
        self.table.heading("spade", text="♠", anchor=CENTER)

        self.table.insert(parent='', index='end', iid=2, text='',
                          values=('2', 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid=3, text='',
                          values=('3', 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid=4, text='',
                          values=('4', 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid=5, text='',
                          values=('5', 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid=6, text='',
                          values=('6', 8, 8, 8, 8)),
        self.table.insert(parent='', index='end', iid=7, text='',
                          values=('7', 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid=8, text='',
                          values=(8, 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid=9, text='',
                          values=('9', 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid=10, text='',
                          values=('10', 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid="J", text='',
                          values=('J', 8, 8, 8, 8)),
        self.table.insert(parent='', index='end', iid="Q", text='',
                          values=('Q', 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid="K", text='',
                          values=('K', 8, 8, 8, 8))
        self.table.insert(parent='', index='end', iid="A", text='',
                          values=('A', 8, 8, 8, 8))

        self.table.grid(padx=5, pady=5)
    
    def ResetAll(self):
        lenPre = len(self.tablePre.get_children())
        for i in range(lenPre):
            self.tablePre.delete(i+2)
        lenLast = len(self.tableLast.get_children())
        for k in range(lenLast):
            self.tableLast.delete(k+2)
        lenTable = len(self.itemTale)
        for l in range(lenTable):
            self.table.item(self.itemTale[l], value = [self.itemTale[l],8,8,8,8])
        self.label_value_countC.config(fg="green")
        self.label_value_countC["text"] = 0

    def ShuffleCards(self):
        deck = []
        lenDeck = len(self.tableLast.get_children())
        for i in range(lenDeck):
            deck.append(self.tableLast.item(i+2)["values"][0])
        if(lenDeck != 416):
            deck += self.GetCardLeft()
        #print(deck)
        timeShuffle = int(self.input_shuffletimes.get())
        timeSplit = int(self.input_splitletimes.get())
        deck = self.Shuffle(deck,timeShuffle)
        deck = self.Shuffle(deck,timeShuffle)
        deck = self.SplitDeck(deck,timeSplit*2)
        aff = []
        lenDeck = len(deck)
        midleDeck = int(len(deck)/2) 
        for i in range(midleDeck):
            aff.append(deck[i]+deck[i+midleDeck])
        newDeck = []
        for k in range(len(aff)):
            aff[k] = self.Shuffle(aff[k],1)
            aff[k] = self.NormalShuffle(aff[k],timeSplit)
            aff[k] = self.Shuffle(aff[k],1)
            newDeck += aff[k]
        newDeck = newDeck[midleDeck:] + newDeck[:midleDeck]
        lenDeck = len(newDeck)
        lenOldPre = len(self.tablePre.get_children())
        for l in range(lenOldPre):
            try:
                self.tablePre.delete(l+2)
            except:
                print("Pass")
                pass
        lenLast = len(self.tableLast.get_children())
        for n in range(lenLast):
            self.tableLast.delete(n+2)
        for m in range(lenDeck):
            try:
                self.tablePre.insert(parent='', index=2+m, iid=2+m, text='',
                    values=newDeck[m])
            except:
                self.tablePre.item(2+m, values=newDeck[m])
            #print(m)
            #print(newDeck[m])
        lenTable = len(self.itemTale)
        for j in range(lenTable):
            self.table.item(self.itemTale[j], value = [self.itemTale[j],8,8,8,8])
        self.label_value_countC.config(fg="green")
        self.label_value_countC["text"] = 0
        #print(len(self.tablePre.get_children()))


    def NormalShuffle(self, oldDeck,times):
        oldDeck = self.SplitDeck(oldDeck, times)
        lenNewDeck = len(oldDeck)
        newDeck = []
        for i in range(lenNewDeck-1,-1,-1):
            newDeck += oldDeck[i]
        return newDeck

    def SplitDeck(self, oldDeck, times):
        carPerPart = int(len(oldDeck)/times)
        newDeck = []
        newDeck.append(oldDeck[:carPerPart])
        prePos = 0
        lastPos = carPerPart
        for i in range(times-2):
            prePos =  lastPos
            lastPos = lastPos + carPerPart
            newDeck.append(oldDeck[prePos:lastPos])
        newDeck.append(oldDeck[lastPos:])
        return newDeck

    def Shuffle(self, oldDeck, times):
        lenOldDeck = len(oldDeck)
        middleDeck = int(lenOldDeck / 2)
        newDeck = []
        div = int(floor(lenOldDeck / (times * 2)))
        surplus = abs(lenOldDeck - div * (times * 2))
        #print(div)
        i = 0
        while i < middleDeck:
            if(i+div-1 + middleDeck> lenOldDeck - 1):
                for j in range(i + int(surplus/2) - 1,i-1,-1):
                    newDeck.append(oldDeck[j])
                    newDeck.append(oldDeck[j + middleDeck])
            else:
                for j in range(i+div-1,i-1,-1):
                    newDeck.append(oldDeck[j])
                    newDeck.append(oldDeck[j + middleDeck])
            i += div
        return newDeck

    def GetCardLeft(self):
        deckLeft = []
        for line in self.table.get_children():
            cardLeft = self.table.item(line)['values'][1:]
            type = 1
            for value in cardLeft:
                if(value > 0):
                    for i in range(value):
                        deckLeft.append(str(self.table.item(line)['values'][0]) + self.GetTypeChar(type))
                type += 1
        #deckLeft = random.shuffle(deckLeft)
        return self.RandomShuffle(deckLeft)
    
    def RandomShuffle(self, deck):
        return sample(deck, len(deck))
    
    def AddLast(self):
        deck = ""
        deck = self.input_dl.get()+self.input_p7_2.get()+self.input_p7.get()+self.input_p6_2.get()+self.input_p6.get()+self.input_p5_2.get()+self.input_p5.get()+self.input_p4_2.get()+self.input_p4.get()+self.input_p3_2.get()+self.input_p3.get()+self.input_p2_2.get()+self.input_p2.get()+self.input_p1_2.get()+self.input_p1.get()
        deck = deck.split("+")
        deck.remove(deck[len(deck) - 1])
        #print(self.table.get_children())
        #print(len(self.table.get_children()))
        #print(self.tableLast.get_children())
        #print(len(self.tableLast.get_children()))
        #print(deck)
        lenDeck = len(deck)
        lenLastDeck = len(self.tableLast.get_children())
        for i in range(lenDeck):
            self.tableLast.insert(parent='', index=lenLastDeck+2+i, iid=lenLastDeck+2+i, text='',
                        values='')
        lenNewDeck = lenDeck + lenLastDeck
        count = 0
        for j in range(lenLastDeck+1,1,-1):
            #print(j)
            #print(self.tableLast.item(j)["values"])
            self.tableLast.item(lenNewDeck+1 - count, text="", values=self.tableLast.item(j)["values"])
            count += 1
        for k in range(lenDeck):
            self.tableLast.item(k+2,text = "", values=deck[k])
        #print(self.tableLast.item(2))
        count = 2
        if(lenDeck > 0):
            #print("OK")
            for line in self.tablePre.get_children():
                #print(self.tablePre.item(line))
                preValue = self.tablePre.item(line)["values"][0]
                if(preValue in deck):
                    self.tablePre.delete(line)
                    deck.remove(preValue)
                if len(deck) <= 0:
                    break
                count += 1
        self.DeleteAllValue()
        

    def DeleteAllValue(self):
        self.input_dl.delete('0', END)
        self.input_p7_2.delete('0', END)
        self.input_p7.delete('0', END)
        self.input_p6_2.delete('0', END)
        self.input_p6.delete('0', END)
        self.input_p5_2.delete('0', END)
        self.input_p5.delete('0', END)
        self.input_p4_2.delete('0', END)
        self.input_p4.delete('0', END)
        self.input_p3_2.delete('0', END)
        self.input_p3.delete('0', END)
        self.input_p2_2.delete('0', END)
        self.input_p2.delete('0', END)
        self.input_p1_2.delete('0', END)
        self.input_p1.delete('0', END)

    def DeleteOneCard(self):
        focused_widget = self.parent.focus_get()
        try:
            deck = focused_widget.get()
        except:
            Msb.showinfo(title='Remind', message='You must forcus on one player')
            return
        lenDeck = len(deck)
        if(lenDeck >= 2):
            type =deck[lenDeck-2]
            try:
                if(deck[lenDeck-3] == "0"):
                    card = deck[lenDeck-4:lenDeck-2]
                    deck = deck[:lenDeck-4]
                elif(deck[lenDeck-2] != "0"):
                    card = deck[lenDeck-3]
                    deck = deck[:lenDeck-3]
            except:
                pass
            #print(type)
            #print(card)
            cardLeft = []
            for i in range(5):
                if(i == self.GetType(type)):
                    cardLeft.append(self.table.item(card)["values"][i] + 1)
                else:
                    cardLeft.append(self.table.item(card)["values"][i])
            self.table.item(card, text = '', values = cardLeft)
            self.CountCards(card,False)
            focused_widget.delete('0', END)
            focused_widget.insert(END, deck)
            self.DisableType(False)
        else:
            Msb.showinfo(title='Remind', message='You must input at least one card')

    def DisableNum(self):
        self.button_2["state"] = DISABLED
        self.button_3["state"] = DISABLED
        self.button_4["state"] = DISABLED
        self.button_5["state"] = DISABLED
        self.button_6["state"] = DISABLED
        self.button_7["state"] = DISABLED
        self.button_8["state"] = DISABLED
        self.button_9["state"] = DISABLED
        self.button_10["state"] = DISABLED
        self.button_J["state"] = DISABLED
        self.button_Q["state"] = DISABLED
        self.button_K["state"] = DISABLED
        self.button_A["state"] = DISABLED
        self.button_hearts["state"] = NORMAL
        self.button_diamonds["state"] = NORMAL
        self.button_clubs["state"] = NORMAL
        self.button_spade["state"] = NORMAL
        self.button_plus["state"] = DISABLED

    def DisableType(self, status):
        self.button_2["state"] = NORMAL
        self.button_3["state"] = NORMAL
        self.button_4["state"] = NORMAL
        self.button_5["state"] = NORMAL
        self.button_6["state"] = NORMAL
        self.button_7["state"] = NORMAL
        self.button_8["state"] = NORMAL
        self.button_9["state"] = NORMAL
        self.button_10["state"] = NORMAL
        self.button_J["state"] = NORMAL
        self.button_Q["state"] = NORMAL
        self.button_K["state"] = NORMAL
        self.button_A["state"] = NORMAL
        self.button_hearts["state"] = DISABLED
        self.button_diamonds["state"] = DISABLED
        self.button_clubs["state"] = DISABLED
        self.button_spade["state"] = DISABLED
        self.button_plus["state"] = NORMAL
        if(status):
            focused_widget = self.parent.focus_get()
            deck = focused_widget.get()
            lenDeck = len(deck)
            if(deck[lenDeck-2] == "0"):
                card = deck[lenDeck-3:lenDeck-1]
            else:
                card = deck[lenDeck-2:lenDeck-1]
            #print(card)
            self.CountCards(card,True)
            type = deck[lenDeck-1:]
            #print(self.table.item(card)["values"][self.GetType(type)])
            cardLeft = []
            for i in range(5):
                if(i == self.GetType(type)):
                    cardLeft.append(self.table.item(card)["values"][i] - 1)
                else:
                    cardLeft.append(self.table.item(card)["values"][i])
            self.table.item(card, text = '', values = cardLeft)
            focused_widget.insert(END, "+")
            
            #print(self.table.item(card))

    def DisableNumNType(self):
        self.button_2["state"] = DISABLED
        self.button_3["state"] = DISABLED
        self.button_4["state"] = DISABLED
        self.button_5["state"] = DISABLED
        self.button_6["state"] = DISABLED
        self.button_7["state"] = DISABLED
        self.button_8["state"] = DISABLED
        self.button_9["state"] = DISABLED
        self.button_10["state"] = DISABLED
        self.button_J["state"] = DISABLED
        self.button_Q["state"] = DISABLED
        self.button_K["state"] = DISABLED
        self.button_A["state"] = DISABLED
        self.button_hearts["state"] = DISABLED
        self.button_diamonds["state"] = DISABLED
        self.button_clubs["state"] = DISABLED
        self.button_spade["state"] = DISABLED

    def CountCards(self, card, type):
        increasePoint = 0
        try:
            card = int(card)
            if(card >= 2 and card <= 6):
                increasePoint = 1
            elif(card >= 7 and card <= 9):
                increasePoint = 0
            elif(card >= 10):
                increasePoint = -1
        except:
            increasePoint = -1
        if(type == True):
            point = increasePoint + int(self.label_value_countC["text"])
        else:
            point = int(self.label_value_countC["text"]) - increasePoint
        if point >= 0:
            self.label_value_countC.config(fg="green")
        else:
            self.label_value_countC.config(fg="red")
        self.label_value_countC["text"] = point
        
    
    def GetType(self, type):
        if(type == "♡"):
            return 1
        elif(type == "♢"):
            return 2
        elif(type == "♣"):
            return 3
        elif(type == "♠"):
            return 4

    def GetTypeChar(self, type):
        if(type == 1):
            return "♡"
        elif(type == 2):
            return "♢"
        elif(type == 3):
            return "♣"
        elif(type == 4):
            return "♠"


    def CheckForcus(self, value):
        try:
            focused_widget = self.parent.focus_get()
            focused_widget.insert(END, value)
            self.DisableNum()
        except:
            Msb.showinfo(title='Remind', message='You must forcus on one player')

    def Send_2(self):
        self.CheckForcus("2")

    def Send_3(self):
        self.CheckForcus("3")

    def Send_4(self):
        self.CheckForcus("4")

    def Send_5(self):
        self.CheckForcus("5")

    def Send_6(self):
        self.CheckForcus("6")

    def Send_7(self):
        self.CheckForcus("7")
    def Send_8(self):
        self.CheckForcus("8")

    def Send_9(self):
        self.CheckForcus("9")

    def Send_10(self):
        self.CheckForcus("10")

    def Send_J(self):
        self.CheckForcus("J")

    def Send_Q(self):
        self.CheckForcus("Q")

    def Send_K(self):
        self.CheckForcus("K")

    def Send_A(self):
        self.CheckForcus("A")
        
    def Send_hearts(self):
        focused_widget = self.parent.focus_get()
        focused_widget.insert(END, "♡")
        self.DisableType(True)

    def Send_diamonds(self):
        focused_widget = self.parent.focus_get()
        focused_widget.insert(END, "♢")
        self.DisableType(True)

    def Send_clubs(self):
        focused_widget = self.parent.focus_get()
        focused_widget.insert(END, "♣")
        self.DisableType(True)

    def Send_spade(self):
        focused_widget = self.parent.focus_get()
        focused_widget.insert(END, "♠")
        self.DisableType(True)

    def Send_plus(self):
        focused_widget = self.parent.focus_get()
        focused_widget.insert(END, "+")
        #self.DisableType(True)
