
def arithmetic_arranger(lista, val = False):
    
    if len(lista) > 4:
        return "Error: Too many problems."
    
    line1 = line2 = line3 = line4 = ""
    
    for cadena in lista:
        
        operando1, operador, operando2 = cadena.split()
        
        if not operando1.isdigit() or not operando2.isdigit():
            return "Error: Numbers must only contain digits."
        
        res = str(eval(cadena))
        
        if operador not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        max_len = max(len(operando1), len(operando2))
        min_len = min(len(operando1), len(operando2))
        
        if max_len > 4 or min_len > 4:
            return "Error: Numbers cannot be more than four digits."
        
        
        line1 += f"  {operando1:>{max_len}}    "
        line2 += f"{operador} {operando2:>{max_len}}    "
        line3 += f"-" * (max_len + 2) + f"    "
        line4 += f" {res:>{max_len + 1}}    "
        
    lineas = [line1, line2, line3, line4]
    for i in range(len(lineas)):
        lineas[i] = lineas[i].rstrip()
        
    if val == True:
            
        operacion = f"{lineas[0]}\n{lineas[1]}\n{lineas[2]}\n{lineas[3]}"
            
    else:
        operacion = f"{lineas[0]}\n{lineas[1]}\n{lineas[2]}"

    return operacion
    

print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49', '45 + 43', '123 + 49']))