from tkinter import *

root = Tk()
root.title("heart")
root.geometry("600x600")

question1_radioButton = StringVar(value = "0")
Question1 = Label(root, text = "is your breath slowing down")
Question1.pack()
question1_r1 = Radiobutton(root, text = "yeah! for sure.", variable = question1_radioButton, value = "yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text = "bruh wot. no", variable = question1_radioButton, value = "no")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")
Question2 = Label(root, text = "are your toes getting smaller")
Question2.pack()
question2_r1 = Radiobutton(root, text = "YES!! i was waiting for someone to mention about that!", variable = question2_radioButton, value = "yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text = "umm.. what?", variable = question2_radioButton, value = "no")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")
Question3 = Label(root, text = "are u confused or lost ur memory")
Question3.pack()
question3_r1 = Radiobutton(root, text = "wat??? wat is this question saying??? (yes i have those symptoms)", variable = question3_radioButton, value = "yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text = "UM. OF COURSE NOT", variable = question3_radioButton, value = "no")
question3_r2.pack()

question4_radioButton = StringVar(value = "0")
Question4 = Label(root, text = "are you coughing ew ew stuff")
Question4.pack()
question4_r1 = Radiobutton(root, text = "yes! its disgusting. please help", variable = question4_radioButton, value = "yes")
question4_r1.pack()
question4_r2 = Radiobutton(root, text = "🤢🤮eughhh... you made me throw up reading that sentence even though i dont have that symptom 🤮🤢", variable = question4_radioButton, value = "no")
question4_r2.pack()

def heart_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+20
        print(score)

    if score <= 20:
        messagebox.showinfo("YAY", "you absolutely should not see a doctor because you are not sick.... (why the heck are you taking this quiz if you said no every single time)")

    elif score > 20 and score <= 40:
        messagebox.showinfo("uh oh..", "you MAYBE have to see the doctor (idk)")
    else: 
        messagebox.showinfo("OH NO", "YOUR BODY", "IT MIGHT HAVE TO SEE THE DOCTOR")

btn = Button(root, text = "click me once you have completed all the question (u better not have put no to all of them)", command = heart_score)
btn.pack()

root.mainloop()