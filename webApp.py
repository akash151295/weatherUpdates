from tkinter import *

import weatherAPI

root = Tk()

root.title("Weather Buddy !!")

root.geometry("600x600+468+158")
# root.minsize(500, 300)
# root.maxsize(500, 300)

variable1 = StringVar()
city_list = []


def search():
    print(variable1.get())
    City = variable1.get()

    temperature, feelsLike_temperature, humidity, grnd_level, City_NotFound = weatherAPI.getweather(City, "a856f37654e904929fcb858c09499991")

    frame3 = Frame(root, bg="#71706E", borderwidth=5, relief=SUNKEN)
    frame3.pack(side=TOP, fill="y", pady=20)
    messageVar = Message(frame3, text=f'''Hey Buddy {City} weather is {temperature} degree C but it feels like {feelsLike_temperature} degree C.''', borderwidth=5, relief=SUNKEN, background="green", fg="white", font="comicsansms 10 bold")
    messageVar1 = Message(frame3,
                         text=f'''{City} humidity is {humidity} g.m-3. and {City} ground level is {grnd_level} MD.''', borderwidth=5, relief=SUNKEN, background="green", fg="white", font="comicsansms 10 bold")
    messageVar.config()
    messageVar.pack(pady=5, padx=5)
    messageVar1.config()
    messageVar1.pack(pady=5, padx=5)

def run():
    # Bot Label Frame
    frame1 = Frame(root, bg="blue", borderwidth=5, relief=SUNKEN)
    frame1.pack(side=TOP, fill="x")
    l1 = Label(frame1, text="BOT", font="comicsansms 15 bold", fg='orange', bg="blue")
    l1.pack(padx=215)

    # Output events
    frame2 = Frame(root, bg="#71706E", borderwidth=5, relief=SUNKEN)
    frame2.pack(side=TOP, fill="y")
    l2 = Label(frame2, text="City: ", font="comicsansms 15 bold", fg='orange', bg="#71706E")
    l2.pack(pady=20, padx=150)
    e1 = Entry(frame2, width=15, textvariable=variable1, background="green", fg="white", font="comicsansms 10 bold")
    e1.pack(pady=10, padx=0)
    b1 = Button(frame2, text="Get Weather Updates !!", padx=10, background="green", fg="white", font="comicsansms 10 bold", command=search)
    b1.pack(pady=40, padx=0)



    root.mainloop()



# run()

