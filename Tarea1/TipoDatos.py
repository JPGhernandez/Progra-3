def dato(valor):
   
    try:
        
        int(valor)
        return "entero"
    except ValueError:
        pass
    
    try:
        float(valor)
        return "flotante"
    except ValueError:
        pass
    
    if valor.lower() in ['true', 'false']:
        return "booleano"
    
    return "cadena"

def main():
  
    valor = input("Ingrese un valor: ")

    tipo_dato = dato(valor)
    print(f"La variable ingresada es de tipo:  {tipo_dato}.")

if __name__ == "__main__":
    main()


