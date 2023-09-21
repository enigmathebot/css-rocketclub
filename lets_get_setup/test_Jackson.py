# calc
import operator
import tkinter as tk

def calc(input):
  eq = [*input]
  for i in eq:
    if i in [*"+-*/%^"]:
      op = i
      opindex = eq.index(i)
  num1 = int("".join(eq[:opindex]))
  num2 = int("".join(eq[opindex+1:]))
  ops = {"+":operator.add,"-":operator.sub,"*": operator.mul,"/":operator.truediv,"%":operator.mod,"^":pow}
  return "="+str(ops[op](num1, num2))

root = tk.Tk()
root.title("Calculator")

textbox = tk.Text(root, height = 1, width = 30)
textbox.pack()

def calc2():
  textbox.insert(tk.END, calc(textbox.get("1.0", "end-1c")))

button = tk.Button(root, text="Calculate", command=calc2)
button.pack()


root.mainloop()