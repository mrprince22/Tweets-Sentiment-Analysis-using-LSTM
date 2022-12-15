import Predict
import tkinter
from tkinter import messagebox
result = ""
bg = "#2A2A2A"
font = ("Cairo",25)
green = "#00FF00"
red = "#FF0000"
degrees = {"positive": green, "negative": red}
def get_text():
    global main_root
    global result
    sentence = text.get("1.0","end-1c")
    if len(sentence) == 0:
        pass
    result = Predict.predict(sentence)
    sentiment.configure(text = result, fg=degrees[result], font = ("Cairo", 21))

root = tkinter.Tk()
root.resizable(False, False)
root.title("Sentiment Detection")
root.geometry("350x450")
root.config(background=bg)
label = tkinter.Label(root, text="Enter A Sentence", font=font, bg=bg, fg = "#FFFFFF")
label.grid()
label.place(relx=0.5, rely=0.08, anchor='center')
text = tkinter.Text(root, width=30, height = 1.5, font = ("Montserrat", 15))
text.grid()
text.place(relx=0.5, rely = 0.2, anchor = 'center')
press = tkinter.Button(root, command=get_text, width=20, height=1, highlightbackground = bg, text="Get Sentiment") 
press.grid()
press.place(relx=0.5, rely = 0.3, anchor='center')
sentiment = tkinter.Label(root, text="", bg = bg)
sentiment.grid()
sentiment.place(relx=0.5, rely=0.4, anchor="center")
root.mainloop()