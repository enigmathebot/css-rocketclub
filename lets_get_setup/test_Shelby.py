#calculator!!
import operator

#program structure - input (string of numbers/symbols)
#splice and convert
#insert into algorithm
while True:
    try:
        calc_input=input("Enter numbers")
        arithmetic_Symbols = {'x': *, '+':+, '-': -, '/': /, '^': **}
        DIGITS = set('0123456789')
        OPERATIONS = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
            '^': operator.pow,
        }

        def is_digit(var):
          return var in DIGITS

        def get_number(varstr):
            s=""
            for c in carstr:
                if not is_digit(c):
                    break
                s+=c
            return(int(s), len(s))  
        
        def perform_operation(string,num1,num2 ):
            op=OPERATIONS.get(string, NONE)
            if op is not None:
                return op(num1, num2)
            else:
                return None #How to handle this?
            
        def eval_math_expr(expr):
            negate=False
            while True:
                try:
                    if expr[0]=='-' #negative numbers
                    negate=True
                    expr=expr[1:]
        #search calc input (string) for arithmetic symbols 
        def search(values, searchFor):
            for i in values:
                for v in values[i]:
                    if searchFor in v: 
                        return i
            return None
        "if symbol is present than add it to the new string in right order"

        "returns arithmetic symbol"
        search(calc_input, 'x')
        search(calc_input, '+')
        search(calc_input, '-')
        search(calc_input, '/')
        search(calc_input, '^')
    
        def calculate (multiply, add, subract, divide, exponent):
            addition = calc_input.split("+", -1) 
            return answer
        
      
        calculate()

        break
    except ValueError:
        print("That was not a valid input. Try again...")
    


