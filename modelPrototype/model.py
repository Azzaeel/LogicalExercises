#Crear una clase para la encuesta
#Crear una clase para los profesores
#Crear una clase para los estudiantes 

def smallest(n):
    cad = str(n)
    x = list(str(n))
    x = [int(i) for i in x]
    final = []
    mani = x.copy()
    for i in range(len(x)):
        mani.pop(i)
        for j in range(len(x)):
            mani.insert(j, x[i])
            final.append((''.join(map(str, mani.copy())))) 
            mani.pop(j)
        mani.insert(i, x[i])
    orde = sorted(final)
    num = orde[0]
    indice_cambio = None
    for i in range(len(x)):
        if x[i] != num[i]:
            indice_cambio = i
            break

# Obtener el índice original y el nuevo índice del número cambiado
    indice_original = indice_cambio
    indice_nuevo = orde.index(x[indice_cambio])
    print([int(num), indice_original, indice_nuevo])
    
    
smallest(296837)    


