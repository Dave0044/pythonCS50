def main():
    list_bibl()
    
def  list_bibl():  
    nombre_archivo = "requirements.txt"

    bibliotecas = ["Numpy", "Pandas", "Matplotlib", "Scikit-learn", "TensorFlow", "PyTorch"]

    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Lista de Bibliotecas:\n\n")
        for i in range(len(bibliotecas)):
            archivo.write(f"{i + 1}. {bibliotecas[i]}\n")
        
    print(f"Se ha creado el archivo '{nombre_archivo}' con la lista de bibliotecas.")




if __name__ == "__main__":
    main()
