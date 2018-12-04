from guizero import App, Picture, PushButton

def do_nothing():
    print("Nothing happened")
    
'''
app = App(title="guizero grid span example", width=460, height=210, layout="grid")
picture1 = Picture(app, image="std1.gif", grid=[0,0])
picture2 = Picture(app, image="std2.gif", grid=[1,0])
picture3 = Picture(app, image="tall1.gif", grid=[2,0,1,2])
picture4 = Picture(app, image="wide1.gif", grid=[0,1,2,1])
app.display()
'''
app = App(title="Keypad example", width=100, height=90, layout="grid")
button1 = PushButton(app, command=do_nothing, text="1", grid=[0,0])
button2 = PushButton(app, command=do_nothing, text="2", grid=[1,0])
button3  = PushButton(app, command=do_nothing, text="3", grid=[2,0])
button4  = PushButton(app, command=do_nothing, text="4", grid=[0,1])
button5  = PushButton(app, command=do_nothing, text="5", grid=[1,1])
button6  = PushButton(app, command=do_nothing, text="6", grid=[2,1])
button7  = PushButton(app, command=do_nothing, text="longer_button", grid=[0,2,3,1])
app.display()

