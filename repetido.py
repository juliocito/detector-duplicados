#1- Debo iterar
#2- Avriri el archivo en modo binario
#3- Comparo los archivos internamente ya que por nombres no es efectivo
#4- Si nombre aparece mas de una vez dejar al menos 1 en la carpeta actual y mover los otros a carpeta llama repetida
#5- Nota que los sietmas operativos modernos ya no permite archivos con el mismo nombre

from pathlib import Path
import hashlib  #Esta libreria permite comparar contenidos
import shutil

def mostrar_banner():
    print("=" * 50)
    print("        DUPLICADOS-JULIOCITO-WARRIOR")
    print("=" * 50)
    print("ENCUENTRA LOS ARCHIVOS DUPLICADOS Y LOS METE DENTRO DE UNA CARPETA LLAMADO 'COPIAS'")
    print()

mostrar_banner()

entrada_user = input("Diga su ruta a examinar archivos repetidos: ")
ruta_user = Path(entrada_user)

archivos = [f for f in ruta_user.iterdir() if f.is_file()] #Te dice si el archivo es un archivo y no carpeta


hash_almacenados ={}

print("\nTrabajando, Por favor espere!!!\n")
for archivo in archivos:
    algoritmo = hashlib.md5() #Crea un tipo de alrgoritmo para escanear archivos binariamente
    with open(archivo, "rb") as f: #Abre el archivo en modo binario
        while True:
            bloque = f.read(4096)  #Lee el archivo y lo carga por bloques
            if not bloque: #Cuando el bloque no tenga nada significa que llego al final del archivo
                break
            algoritmo.update(bloque) #Debido a que va opedazos por pedazo del archivo, alfu=inal se actualiza en un solo lugar
    hash_archivo = algoritmo.hexdigest() #Nuevo Hash para cada archivo

    if hash_archivo not in hash_almacenados: #
        hash_almacenados[hash_archivo] = [archivo]
    else:
        destino = ruta_user / "copias"
        destino.mkdir(exist_ok=True)
        shutil.move(str(archivo), destino / archivo.name)
        hash_almacenados[hash_archivo].append(archivo)


print("\nDuplicados encontrados:\n")


for hash_valor, lista_archivos in hash_almacenados.items():
    if len(lista_archivos) > 1:
        print(f"Grupo duplicado ({len(lista_archivos)} archivos):")
        for archivo in lista_archivos:
            print(archivo.name)
        print()

print("Busque los archivos repetidos en la carpeta creada llamada 'copias'".upper())

input("\nPresione Enter para salir....")

