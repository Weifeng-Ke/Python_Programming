import tkinter as tk

def main():
    window = tk.Tk()  # Create the main window
    window.title("Server")  # Add a title
    window.geometry("500x500")  # Set window size
    label = tk.Label(window, text="This is a label", font=('Arial',18))  # Add a label
    label.pack(padx=50, pady=100)  # Pack the label into the window
    
    textbox=tk.Text(window,height=3,font=('Arial',16))
    textbox.pack()
    
    botton=tk.Button(window,text="click me", font=('arial',18))
    botton.pack(side='left',padx=2,pady=2)
    
    buttonframe=tk.Frame(window)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)
    
    btn1=tk.Button(buttonframe,text='1', font=('arial',19))
    btn1.grid(row=0, column=0, sticky='news')
    
    
    
    btn2=tk.Button(buttonframe,text='2', font=('arial',19))
    btn2.grid(row=0, column=1, sticky='news')
    
    btn3=tk.Button(buttonframe,text='3', font=('arial',19))
    btn3.grid(row=0, column=2, sticky='news')
    
    btn4=tk.Button(buttonframe,text='4', font=('arial',19))
    btn4.grid(row=1, column=0, sticky='news')
    
    btn5=tk.Button(buttonframe,text='5', font=('arial',19))
    btn5.grid(row=1, column=1, sticky='news')
    
    btn6=tk.Button(buttonframe,text='6', font=('arial',19))
    btn6.grid(row=1, column=2, sticky='news')
    
    btn7=tk.Button(buttonframe,text='7', font=('arial',19))
    btn7.grid(row=2, column=0, sticky='news')

    btn8=tk.Button(buttonframe,text='8', font=('arial',19))
    btn8.grid(row=2, column=1, sticky='news')

    btn9=tk.Button(buttonframe,text='9', font=('arial',19))
    btn9.grid(row=2, column=2, sticky='news')
    
    
    buttonframe.pack(fill='x')
    
    window.mainloop()  # Start the GUI event loop

if __name__ == '__main__':
    main()
