import txtprocessor as txtP
import sys

if len(sys.argv) > 1:
    fentrada = sys.argv[1]
else:
    fentrada = input("nombre completo del fichero: ")

try:
    fentrada = open(fentrada, "r")
    fstats = open("stats.txt", "w+")
    fcorrec = open("correccion.txt", "w+")

    texto = fentrada.read()
    # Corregir texto
    textoCorregido = txtP.textCorrection(texto)
 
    # Estadísticas del texto
    totales, listas = txtP.estadisticas(textoCorregido)

    # Escribir ficheros y salida
    fcorrec.write(textoCorregido)

    print("Texto original:\n>>>{}<<<\n-----------".format(texto))
    print("Texto corregido:\n>>>{}<<<".format(textoCorregido))

    for key, value in totales.items():
        linea = "Total de {}: {}".format(key, value)
        print(linea)
        fstats.write(linea+"\n")

    fentrada.close()
    fstats.close()
    fcorrec.close()
except Exception as e:
    print("Se ha producido un error con los ficheros: ", e)