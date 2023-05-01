"""
Act 3.2
Francisco Jervis
03/31/2023
A00835131

"""
operators={'+':'suma','=':'asignación',' - ':'resta','*':'multiplicación','/':'división','^':'potencia','(':'paréntesis que abre',')':'paréntesis que cierra','\n':''}
#diccionario con operadores

f=input("Nombre del archivo sin su extensión .txt:\n")

def printtable(t):
    """
    Función que imprime la tabla generada pro la función lexer aritmetico

    Parameters
    ----------
    t : lista con formato de tabla.

    Returns
    -------
    None.

    """
    i=0
    print('Token  ->  Tipo\n---------------')
    while i<len(t)-1:
        print(t[i],'  ->  ',t[i+1])
        i+=2 
        
def lexerAritmetico(nombre_archivo):
    """
    Función que procesa un archivo de texto identificando los diferentes tipos de tokens en el archivo 
    y utiliza una función auxiliar para imprimir una tabla con todos los datos     

    Parametrs:
    ----------
    nombre_archivo : nombre del archivo a procesar.

    Returns
    -------
    None.

    """
    nombre_archivo+='.txt'
    table=[]#lista donde se guardarán los elementos de la tabla
    with open(nombre_archivo) as file:
       for line in file:
           if line=='\n':
               continue
           #variables iniciales
           temp=''#string temporal donde se guardan los tokens
           comt=False#booleano para identificar si se llego a un comentario
           flag1=False#boleano para identificar numeros reales en notación cientifica
           
           c=0#iterador adentro de la linea
           
           while c < len(line):
               if line[c]=='/'and line[c+1]=='/':#identificar comentraios
                   comt=True
               flag3=True#booleano para identificar si existe una resta
               
               if c<len(line)-4 and (line[c]==' ' and line[c+1]=='-' and line[c+2]==' '):
                   c+=2
                   flag3=False
                   
               if (line[c]=='e' or line[c]=='E'):#identificar numeros reales en notación cientifica
                   try:#exception handling para saber si la e pertenece a un numero o a una variable
                       flag1=True
                       float(temp)
                   except ValueError:
                       flag1=False
                       
               if line[c] not in operators and flag3:#si no se identificó un operador se añade el caracter a la string del token
                   temp+=line[c]
                   
               else:#token finalizó
               
                   if temp=='':#token vació
                       table.append(line[c])
                       table.append(operators[line[c]])
                       c+=1 
                       continue
                   
                   temp=temp.strip()
                   
                   try:#separar reales con enteros y reales en notación sientifica con variables dependiendo si existen letras en ellos o no 
                       flag2=True
                       float(temp)
                   except ValueError:
                       flag2=False
                       
                   if flag2:
                       if '.' in temp:
                           table.append(temp)
                           table.append('real')
                           temp=''
                       else:
                           table.append(temp)
                           table.append('entero')
                           temp=''
                   else:
                       if  flag1:
                           table.append(temp)
                           table.append('real')
                           temp=''
                       else:
                           table.append(temp)
                           table.append('variable')
                           temp=''
                           
                           #añadir operadores a la tabla
                           
                   if line[c] != '\n'and flag3 and not comt:        
                       table.append(line[c])
                       table.append(operators[line[c]])
                       
                   if not flag3:#existe una resta
                       table.append(' - ')
                       table.append(operators[' - '])
                       
                   if comt:#existe un comentario
                       table.append(line[c:])
                       table.append('comentario')
                       break
                   
               c+=1    
               
    printtable(table)               
                           
lexerAritmetico(f)         