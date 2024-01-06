import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.cal = ""
        self.result = tk.Text(root, height=2, width=16)
        self.result.grid(columnspan=5)
        self.display()

        add_button = tk.Button(root, text="C", width=5, command= self.clear)
        add_button.grid(row=4, column=0, columnspan=2)

    def calculate(self, string):
        self.cal += str(string)
        try:
            if string in {'*', '/', '+', '-'}:
                result = self.cal
            else:
                result = str(eval(self.cal))                
            self.result.delete(1.0, tk.END)
            self.result.insert(1.0, result)
        except Exception as e:
            self.result.delete(1.0, tk.END)
            self.result.insert(1.0, "Error")

    def clear(self):
        self.cal = ""
        self.result.delete(1.0, tk.END)
        
    def display(self):
        item = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '0','/']
        for i in range(14):
            add_button = tk.Button(root, text=str(item[i]), command=lambda x=item[i]: self.calculate(x))
            if i>11:
                add_button.grid(row=(i) // 4 + 1, column=(i+2) % 4)
            else:
                add_button.grid(row=(i) // 4 + 1, column=(i) % 4)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
