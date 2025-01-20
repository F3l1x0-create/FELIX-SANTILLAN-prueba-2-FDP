
precios={
    "auto : $", 2000 ,
    "camioneta : $", 3000 ,
    "camion : $", 4000,
    "motocicleta: $", 890

}


fondo_inicial= 40000
fondo= fondo_inicial
descuento_acumulados =0

def calcular_descuento (correo):
    reglas_descuento ={
        'A': 1.5, 'E':1.0, 'I': 0.7, 'O':1.2, 'U':0.5,
        'X': 2.0, 'Y': 2.1
    
}
    descuento=0
    for char in correo.upper():
        if char in reglas_descuento:
            descuento+= reglas_descuento[char]
            return descuento
        
def maquina_estacionamiento():
    global fondo , descuento_acumulados

while True: 
        print("***maquina de estacionamientos***")
        print("tipo de vehiculos y precios")
        for tipo , precios in precios.items():
            print(f"- {tipo}:. ${precios}")

        correo= input(" ingrese su correo electronico :")
        if len(correo) < 8 or len(correo) > 30 :
            print("correo invalido, debe tener de 8 a 30 caracteres")
            continue



        print("seleccione el tipo de vehiculo :")
        tipos= list(precios.keys())
        for i, tipo in enumerate(tipos):
            print(f"{i+ 1 }. {tipo}")
            opcion= int(input("opcion :"))
            if opcion < 1 or opcion > len(tipos):
                print("opcion invalida")
                continue


        descuento= calcular_descuento(correo)
        total_descuento= precios* (descuento / 100)
        precio_final= precios - total_descuento
        if precio_final < 0 :
            precio_final=0
        if descuento_acumulados > 0 :
            print("aplicando descuento adicional")
        precio_final -= descuento_acumulados
    
        if precio_final <= 0:
            print("estacionamiento gratuito")
        else:
            print(f" el precio final con descuentos: ${precio_final: .2f} ")
            print(f"descuentos acumulados :{descuento_acumulados:.2f}")

        repetir=input("desea hacer la operacion denuevo (si/no):")
        if repetir.lower () != "si":
            print("**resumen final**")
            print(f"total recaudado: ${fondo}")
            print(f"fondos disponibles: ${fondo}")
            print(f"descuentos otorgados: {descuento_acumulados:.2f}")
            print("gracias por usar la maquina de estacionamiento ")
            break

if __name__ == "__main__":
    maquina_estacionamiento=()
