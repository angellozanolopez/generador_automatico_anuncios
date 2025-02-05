Formación en IA generativa

Creación de un sistema de inteligencia artificial para generar descripciones automáticas en los anuncios de los inmuebles (pisos / viviendas). Por ejemplo, un usuario quiere publicar un anuncio y en base a marcar unos checkbox predefinidos (características), se generará el texto. Más abajo hay más información al respecto. 

Los **objetivos** para este ejercicio son: 

- **Mejorar la calidad de los anuncios**: mediante la generación automática de textos  con  IA,  se  logrará  una  descripción más  detallada de  cada  inmueble, incluyendo  todas  sus  características,  haciendo  cada anuncio  único  y  más atractivo. 

**Fases del ejercicio**  

Se segmentará el ejercicio en 5 fases: 

- **Fase 1:** Crear anuncios con sistema de reglas o mediante computación evolutiva. Se creará el texto de los anuncios en base a que el usuario indique las siguientes características: 
- Información básica del inmueble: 
  - metros cuadrados 
  - número de habitaciones 
  - número de salones o comedores 
  - número de cocinas 
  - número de baños 
  - número de balcones 
  - número de terrazas 
  - número de ascensores 
  - climatización / aire acondicionado / calefacción 
  - altura del inmueble (principal, 1ª, 2ª, ....) 
  - nº planta dentro del inmueble 
  - año de construcción 
  - gastos de comunidad e ibi 
  - estado a reformar, o para entrar a vivir 
  - dotaciones vivienda: piscina, tenis, gimnasio 
  - garaje 
- Keywords: 
- Fantástica 
- Maravillosa 
- Fenomenal 
- Oportunidad 
- Espaciosa 
- Amplia 
- Apartamento para [familias, parejas] 
- Inmueble de más de XXXX metros cuadrados 
- **Fase 2**: Complementar las fases anteriores con información geográfica según localización (latitud/longitud + radio/distancia). Se implementará la API de Google Places u otra de acceso gratuito a decidir directamente por el alumno, para disponer de información actualizada en tiempo real. Se identificarán los siguientes servicios o puntos de interés: 
  - transportes 
  - colegios / universidades 
  - establecimientos comerciales 
  - playa 
  - hospitales 
  - farmacias 
  - bibliotecas 
  - centros deportivos 
  - zonas verdes 
  - gasolineras 
  - puntos de recarga de vehículos eléctricos 
- **Fase 3**: Lectura e interpretación de las fotografías del anuncio con visión artificial (ej. api de Google visión, u otras a decidir por parte del usuario), a nivel de: 
  - cocina: horno, nevera, microondas, lavadora, televisor, mesa, sillas, lavavajillas, ventana 
  - habitaciones: cama, mesitas de noche, armarios, ventana 
  - salón-comedor: chimenea, sofá, televisor, mesa, sillas, ventana 
  - baño: pila, WC, bidé, bañera, plato de ducha, ventana 
  - terraza: mobiliario, plantas 
- **Fase 4**: Complementar con adjetivos obtenidos a través de las imágenes, extensión de la fase 3: 
  - Iluminación (mucha luz natural) 
  - Espacios amplios 
  - .... 
- **Fase 5**: Creación de estilos de texto diferente para cada anuncio 
- En función de los resultados obtenidos para cada anuncio (Fase1+2+3+4), se devolverá el texto según target estimado del anuncio (jerga, tutear o tratar de usted, [completar]) 
- Inmueble espacioso, ideal parejas, [completar] 

Ejecución del ejercicio 

Se mostrarán los resultados a nivel de: 

- textos sugeridos para crear los anuncios 
- información en base a puntos de interés por geolocalización 
- keywords y adjetivos para complementar los anuncios 
- estilo de texto según target del anuncio 

` `¡Ánimos! 

Entregables (en un único WeTransfer): 

1. Código fuente de la solución 
1. Video explicativo del código fuente (máximo 3 minutos) 
1. Video mostrando e interpretando los resultados (máximo 2 minutos) 
