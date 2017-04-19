import socket
import Tkinter
from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

client_socket = socket.socket()
client_socket.connect(('192.168.1.22', 1111))

Info = ""


def hide_me(event):
    event.widget.pack_forget()

def UserInfo(Data):
    global Info 
    Info = Info + Data
    return Info
    print Info
    print "UserInfo()"

def Register():
    RegisteringWindow = Tk()
    canvas = Canvas(RegisteringWindow, width = 3000, height = 1000)
    w = Label(RegisteringWindow, text = "Enter your name : ")
    w.pack()
    NameBox = Text(RegisteringWindow, height=10, width=30)
    NameBox.pack()
    w2 = Label(RegisteringWindow, text = "Enter your password : ")
    w2.pack()
    PassBox = Text(RegisteringWindow, height=10, width=30)
    PassBox.pack()
    def Saving():
        username = NameBox.get(1.0, END)
        password = PassBox.get(1.0, END)
        Data = username + password
        RegisteringWindow.destroy()
        a.bind('<Button-1>', hide_me)
        Info = UserInfo(Data)
        client_socket.send(username) #to line 17 in server
        text = client_socket.recv(1024)# from line 22 in client
        print text + " is the text"
        if text == "Ok":
            Websites()
        else:
            m = Label(RegisteringWindow, text = "Please choose another name")
            m.pack()
            print "Not a good name"
    Save = Tkinter.Button(RegisteringWindow, text="Save", command = Saving)
    Save.pack()
    
    


def Websites():
    WebsitesWindow = Tk()
    canvas = Canvas(WebsitesWindow, width = 3000, height = 1000)   
    def GmailWindow():
        Gmail2 = Tk()
        canvas = Canvas(Gmail2, width = 3000, height = 1000)
        gulabel = Label(Gmail2, text = "Please enter your E-mail : ")
        gulabel.pack()
        guser = Text(Gmail2, height=10, width=30)
        guser.pack()
        gplabel = Label(Gmail2, text = "Please enter your password : ")
        gplabel.pack()
        gpass = Text(Gmail2, height=10, width=30)
        gpass.pack()
        
        def Finishg():
            GmailData = "Gmail\n" + guser.get(1.0, END) + gpass.get(1.0, END)
            Info = UserInfo(GmailData)
            Gmail2.destroy()
            
        Saveg = Tkinter.Button(Gmail2, text="Save", command = Finishg)
        Saveg.pack()
            
    def WallaWindow():
        Walla2 = Tk()
        canvas = Canvas(Walla2, width = 3000, height = 1000)    
        canvas = Canvas(Walla2, width = 3000, height = 1000)
        wulabel = Label(Walla2, text = "Please enter your E-mail : ")
        wulabel.pack()
        wuser = Text(Walla2, height=10, width=30)
        wuser.pack()
        wplabel = Label(Walla2, text = "Please enter your password : ")
        wplabel.pack()
        wpass = Text(Walla2, height=10, width=30)
        wpass.pack()
        
        def Finishw():
            WallaData = "Walla\n" + wuser.get(1.0, END) + wpass.get(1.0, END)
            Info = UserInfo(WallaData)
            Walla2.destroy()
        Savew = Tkinter.Button(Walla2, text="Save", command = Finishw)
        Savew.pack()
        
    def Finish():
        print "Info = " + Info
        client_socket.send(Info) # to line 35 in server
        WebsitesWindow.destroy()
    
    GmailButton = Tkinter.Button(WebsitesWindow, text="Add Gmail Data", command = GmailWindow)
    GmailButton.pack()
    WallaButton = Tkinter.Button(WebsitesWindow, text="Add Walla Data", command = WallaWindow)
    WallaButton.pack()
    Save = Tkinter.Button(WebsitesWindow, text="Save Data", command = Finish)
    Save.pack()
    
                            
def SignIn():
    pass

chromedriver = ('C:\\Users\User\Desktop\chromedriver.exe')
driver = webdriver.Chrome(chromedriver)
k = 'https://www.google.co.il/?gfe_rd=cr&ei=peS2WM3sO5PN8geGl6rgDA&gws_rd=ssl'
driver.get(k)
FirstWindow = Tk()
canvas = Canvas(FirstWindow, width = 3000, height = 1000)
a = Tkinter.Button(FirstWindow, text="Register", command = Register)
a.pack()
b = Tkinter.Button(FirstWindow, text="Sign In", command = SignIn)
b.pack()

mainloop()


client_socket.close()



