import tkinter as tk
main_window = tk.Tk()
main_window.geometry("600x400")
main_window.title('Markhor Society')
button = tk.Button(main_window, text='Stop', width=25, command=main_window.destroy)
button.pack()
main_window.mainloop()
