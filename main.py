import os
import cv2
import random
# pip install overpass
from overpass import API
# pip install geopy
from geopy.geocoders import Nominatim

import subprocess
import re

os.system('cls')

# ********************************************************************************************************************************
def obtener_latitud_longitud(direccion):
    geolocalizador = Nominatim(user_agent="mi_app")  # Puedes poner cualquier nombre aquí

    # Realizar la búsqueda de la dirección
    try:
        location = geolocalizador.geocode(direccion)
        latitud = location.latitude
        longitud =  location.longitude
        return [latitud, longitud]
    except: # Hay veces que no conecta bien con la API. En este caso ponemos manualmente las coordenadas
        latitud = 37.16127269226915 
        longitud = -3.593688163141175              


# ********************************************************************************************************************************
def puntos_de_interes(latitud, longitud, radio, tipo_lugar):
    api = API()
    query = f"""
    node(around:{radio}, {latitud}, {longitud})[{tipo_lugar}];
    out;
    """
    response = api.get(query)
    nombres_lugares = []
    if 'features' in response:  
        lugares = response['features']
        nombres_lugares = [lugar['properties']['name'] for lugar in lugares if 'name' in lugar['properties']]
    lugares_sin_duplicados = list(set(nombres_lugares))
    return lugares_sin_duplicados


# ********************************************************************************************************************************
def numero_puntos(latitud, longitud, radio):
    paradas = puntos_de_interes(latitud, longitud, radio, '"highway"="bus_stop"')
    farmacias = puntos_de_interes(latitud, longitud, radio, '"amenity"="pharmacy"')
    centros_medicos = puntos_de_interes(latitud, longitud, radio, '"amenity"~"clinic|hospital"')
    restaurantes = puntos_de_interes(latitud, longitud, radio, '"amenity"="restaurant"')
    supermercados = puntos_de_interes(latitud, longitud, radio, '"shop"="supermarket"')
    centros_educativos = puntos_de_interes(latitud, longitud, radio, '"amenity"~"school|college|university"')
    comercios = puntos_de_interes(latitud, longitud, radio, '"shop"')
    playas = puntos_de_interes(latitud, longitud, radio, '"natural"="beach"')
    bibliotecas = puntos_de_interes(latitud, longitud, radio, '"amenity"="library"')
    centros_deportivos = puntos_de_interes(latitud, longitud, radio, '"leisure"="sports_centre"')
    zonas_verdes = puntos_de_interes(latitud, longitud, radio, '"natural"="tree"')
    gasolineras = puntos_de_interes(latitud, longitud, radio, '"amenity"="fuel"')
    puntos_recarga = puntos_de_interes(latitud, longitud, radio, '"amenity"="charging_station"')

    resultados = {
        "paradas": len(paradas),
        "farmacias": len(farmacias),
        "centros_medicos": len(centros_medicos),
        "restaurantes": len(restaurantes),
        "supermercados": len(supermercados),
        "centros_educativos": len(centros_educativos),
        "comercios": len(comercios),
        "playas": len(playas),
        "bibliotecas": len(bibliotecas),
        "centros_deportivos": len(centros_deportivos),
        "zonas_verdes": len(zonas_verdes),
        "gasolineras": len(gasolineras),
        "puntos_recarga": len(puntos_recarga)
    }

    # Filtrar aquellos con valor 0
    resultados = {key: value for key, value in resultados.items() if value != 0}

    return resultados


# ********************************************************************************************************************************
def objetos_encontrados(ruta_imagen):
    comando = ["yolo", "predict", "model=yolov8n.pt", f"source='{ruta_imagen}'"]
    resultado = subprocess.run(comando, capture_output=True, text=True)                   
    texto_completo = resultado.stdout
    # Filtramos toda la informacion y nos quedamos solo con los objetos detectados
    posicion_x640 = texto_completo.find('x640')
    if posicion_x640 != -1:
        texto_final = texto_completo[posicion_x640 + 4:]  # Agregamos 4 para saltar 'x640'
        posicion_speed = texto_final.find('Speed')
        if posicion_speed != -1:
            datos = texto_final[:posicion_speed].strip().split(', ')
            datos = datos[:-1]  # Eliminar el último elemento
            # Diccionario de traducción
            diccionario_traduccion = {                
                'chairs': 'sillas',
                'chair': 'silla',
                'couch': 'sofá',
                'potted plants': 'plantas',
                'potted plant': 'planta',                
                'dining table': 'mesa de comedor',
                'tv': 'televisor',
                'clocks': 'relojes',
                'clock': 'reloj',
                'vases': 'jarrones',
                'vase': 'jarron',
                'bottles': 'botellas',
                'bowl': 'cuenco',
                'toilet': 'inodoro',
                'sink': 'fregadero',
                'microwave': 'microondas',
                'ovens': 'hornos',
                'refrigerator': 'frigorifico',
                'beds': 'camas',
                'bench': 'banco/asiento'
            }
            # Traducción de la lista de objetos detectados
            datos_traducidos = []
            for item in datos:
                # Verifica si la palabra clave está en el diccionario
                traduccion = next((valor for clave, valor in diccionario_traduccion.items() if clave in item), None)
                if traduccion:
                    datos_traducidos.append(traduccion)
                else:
                    datos_traducidos.append(item)

            return datos_traducidos


# ********************************************************************************************************************************
# Analizar la iluminacion de la vivienda haciendo media con la iluminacion de todas las imagenes
def evaluar_iluminacion_carpeta(ruta_carpeta):
    niveles_iluminacion = []

    for imagen in os.listdir(ruta_carpeta):
        ruta_imagen = os.path.join(ruta_carpeta, imagen)
        imagen = cv2.imread(ruta_imagen)

        if imagen is not None:
            imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            iluminacion = cv2.mean(imagen_gris)[0] / 255 * 100
            niveles_iluminacion.append(iluminacion)
        else:
            print(f"No se pudo cargar la imagen: {ruta_imagen}")

    if niveles_iluminacion:
        media_iluminacion = sum(niveles_iluminacion) / len(niveles_iluminacion)
        return media_iluminacion
    else:
        return None


# ********************************************************************************************************************************
# Función para generar el anuncio basado en los datos del usuario
def generar_anuncio(datos):
    keywords = ["Fantástico", "Maravilloso", "Fenomenal", "Gran oportunidad"]
    keywords_adicionales = []
    # -----------------------------------------------------------------------------------
    # Seleccionar 'Espaciosa' y 'Amplia' si la vivienda tiene más de 100 metros cuadrados
    if datos['metros_cuadrados'] > 100:
        keywords += ["Espaciosa", "Amplia"]
    # -----------------------------------------------------------------------------------
    # Concatenar 'apartamento para' con 'familias' si tiene más de 2 habitaciones, o con 'parejas' si tiene 2 o menos habitaciones
    if datos['num_habitaciones'] > 2:
        keywords_adicionales.append("Apartamento para familias")
    else:
        keywords_adicionales.append("Apartamento para parejas o personas que vivan solas.")
    # -----------------------------------------------------------------------------------
    # Construir la descripción de los metros cuadrados
    if datos['metros_cuadrados'] > 100:
        descripcion_metros_cuadrados = f"espacioso apartamento, con una generosa área de {datos['metros_cuadrados']} metros cuadrados"
    else:
        descripcion_metros_cuadrados = f"pequeño apartamento con un área de {datos['metros_cuadrados']} metros cuadrados"
    # -----------------------------------------------------------------------------------
    # Construir la descripción de terraza y balcón
    descripcion_terraza_balcon = ""
    if datos['num_balcones'] > 0 and datos['num_terrazas'] > 0:
        descripcion_terraza_balcon = "Destacando su terraza y balcón, proporciona áreas al aire libre para disfrutar del ambiente."
    elif datos['num_balcones'] > 0:
        descripcion_terraza_balcon = "Destacando su balcón, proporciona áreas al aire libre para disfrutar del ambiente."
    elif datos['num_terrazas'] > 0:
        descripcion_terraza_balcon = "Destacando su terraza, proporciona áreas al aire libre para disfrutar del ambiente."
    # -----------------------------------------------------------------------------------
    # Construir la descripción de ascensores
    descripcion_ascensores = f"{datos['num_ascensores']} ascensores para tu comodidad y " if datos['num_ascensores'] > 0 else ""
    # -----------------------------------------------------------------------------------
    # Construir la descripción del clima
    descripcion_clima = ""
    if not datos['aire_acondicionado'] and not datos['calefaccion']:
        descripcion_clima = ""
    elif not datos['aire_acondicionado'] and datos['calefaccion']:
        descripcion_clima = "Dispone de calefacción para un ambiente cálido durante todo el invierno"
    elif datos['aire_acondicionado'] and not datos['calefaccion']:
        descripcion_clima = "Dispone de aire acondicionado para mantener un clima fresco todo el verano"
    else:
        descripcion_clima = "Dispone de aire acondicionado y calefacción para disfrutar de un clima ideal durante todo el año"
    # -----------------------------------------------------------------------------------
    # Construir la descripción de reformas y apto para vivir
    descripcion_reformas_apto_vivir = ""
    if not datos['reformar'] and not datos['apto_vivir']:
        descripcion_reformas_apto_vivir = "Aunque no es apto para vivir, con algunas reformas usted dispondrá de una vivienda ideal a un precio muy económico."
    elif datos['reformar'] and not datos['apto_vivir']:
        descripcion_reformas_apto_vivir = "Aunque no es apto para vivir, con algunas reformas usted dispondrá de una vivienda ideal a un precio muy económico."
    elif not datos['reformar'] and datos['apto_vivir']:
        descripcion_reformas_apto_vivir = "está listo para habitar, eliminando la necesidad de reformas."
    else:
        descripcion_reformas_apto_vivir = "aunque necesita algunas reformas, está listo para habitar."
    # -----------------------------------------------------------------------------------
    # Construir la descripción de las instalaciones
    descripcion_instalaciones = ""
    if datos['piscina']:
        descripcion_instalaciones += "piscina, "
    if datos['Tenis']:
        descripcion_instalaciones += "canchas de tenis y "
    if datos['Gimnasio']:
        descripcion_instalaciones += "gimnasio "

    descripcion_instalaciones = descripcion_instalaciones.strip()
    if descripcion_instalaciones:
        descripcion_instalaciones = f"Sumérgete en la comodidad de su {descripcion_instalaciones} para mantener un estilo de vida activo."
    # -----------------------------------------------------------------------------------
    # Construir el anuncio utilizando las características del inmueble y las keywords seleccionadas
    anuncio = f"¡{random.choice(keywords)} {' '.join(keywords_adicionales)}! Este "
    anuncio += f"{descripcion_metros_cuadrados}, "
    anuncio += f"ofrece un ambiente acogedor con {datos['num_habitaciones']} habitaciones, ideal para una vida confortable y versátil.\n"
    anuncio += f"Con {datos['num_salones_comedores']} salones/comedores, una cocina totalmente equipada y {datos['num_baños']} baños, "
    anuncio += f"este hogar satisface las necesidades de tu familia. {descripcion_clima}\n{descripcion_terraza_balcon}\n"
    anuncio += f"Además, {'cuenta con ' if datos['num_ascensores'] > 0 else ''}{descripcion_ascensores}{descripcion_reformas_apto_vivir}\n"
    anuncio += f"{descripcion_instalaciones}\n"
    anuncio += f"¡Esta es tu oportunidad de disfrutar de un hogar {'amplio ' if datos['metros_cuadrados'] > 100 else ''}y versátil para toda la familia!"
    # -----------------------------------------------------------------------------------
    return anuncio


# ********************************************************************************************************************************
def main():    
    # DIRECCION DE LA VIVIENDA
    direccion = 'calle fontiveros, 29, granada'
    radio = 100
    latitud, longitud = obtener_latitud_longitud(direccion)

    # CARACTERISTICAS DE LA VIVIENDA (APORTADAS POR EL USUARIO)
    caracteristicas_del_inmueble = {
        'metros_cuadrados':120,
        'num_habitaciones':1,
        'num_salones_comedores':1,
        'num_cocinas':1,
        'num_baños':2,
        'num_balcones':0,
        'num_terrazas':1,
        'num_ascensores':1,
        'aire_acondicionado':True,
        'calefaccion':True,
        'reformar':False,
        'apto_vivir':True,
        'piscina':True,
        'Tenis':False,
        'Gimnasio':True,
        'Garaje':True
    }
    
    # GENERAR TEXTO DEL ANUNCIO EN BASE A LAS CARACTERISTICAS DE LA VIVIENDA
    anuncio = generar_anuncio(caracteristicas_del_inmueble)
    # Mostrar anuncio
    print("ANUNCIO GENERADO: ")
    print(anuncio)
    print()
    
    # ANALIZAR LOS PUNTOS DE INTERES ALREDEDOR DE LA VIVIENDA
    num_puntos_interes = numero_puntos(latitud, longitud, radio)
    # Mostrar los puntos de interes alrededor del inmueble    
    mensaje = f"En un radio de {radio}m dispone de "
    mensaje += ", ".join([f"{valor} {clave.replace('_', ' ')}" for clave, valor in num_puntos_interes.items()])
    mensaje += "."
    print(mensaje)
    print()

    # ANALIZAR LA ILUMINACION DE TODA LA VIVIENDA HACIENDO MEDIA CON TODAS LAS HABITACIONES    
    ruta_carpeta_imagenes = 'PRACTICA 07. Angel Lozano/imagenes/'
    media_total_iluminacion = evaluar_iluminacion_carpeta(ruta_carpeta_imagenes)
    if media_total_iluminacion is not None:
        print(f"La media de iluminación de toda la vivienda es del: {media_total_iluminacion:.2f}%")
    else:
        print("No se pudieron analizar las imágenes.")

    # OBTENER TODAS LAS IMAGENES DE LA VIVIENDA
    archivos_en_carpeta = os.listdir(ruta_carpeta_imagenes)
    # Filtrar los archivos para obtener solo las imágenes
    imagenes_en_carpeta = [archivo for archivo in archivos_en_carpeta if archivo.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # ANALIZAR EL CONTENIDO DE CADA IMAGEN PARA MOSTRARLO EN EL ANUNCIO
    print()
    print("ANALIZANDO EL CONTENIDO DE LAS IMAGENES")

    for imagen in imagenes_en_carpeta:
        ruta_imagen = os.path.join(ruta_carpeta_imagenes, imagen)
        objetos_detectados = objetos_encontrados(ruta_imagen)
        # Extraer el nombre del archivo sin la extensión para mostrarlo en el mensaje
        nombre_imagen = os.path.splitext(imagen)[0]
        contenido_imagen = f"La habitacion {nombre_imagen} dispone de: {', '.join(objetos_detectados)}"
        print(contenido_imagen)   
    print()


# ********************************************************************************************************************************
if __name__ == "__main__":
    os.system("cls")
    main()