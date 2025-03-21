# **Formación en IA Generativa: Generación Automática de Descripciones para Inmuebles**

El objetivo de esta formación es desarrollar un sistema de inteligencia artificial capaz de generar automáticamente descripciones detalladas para anuncios de inmuebles.  
Un usuario podrá seleccionar características predefinidas mediante checkboxes, y el sistema generará un texto basado en esos datos.  

### **Beneficios del sistema**
✅ **Mejorar la calidad de los anuncios:**  
Mediante IA, se generarán descripciones únicas y atractivas que reflejen con precisión las características del inmueble.  

## **Fase 1: Creación de anuncios con sistema de reglas o computación evolutiva**
El sistema generará un texto basado en la información proporcionada por el usuario:  

### 🔹 **Información básica del inmueble**
- 📏 Metros cuadrados  
- 🛏️ Número de habitaciones  
- 🛋️ Número de salones o comedores  
- 🍽️ Número de cocinas  
- 🚿 Número de baños  
- 🌅 Número de balcones  
- ☀️ Número de terrazas  
- 🏗️ Número de ascensores  
- ❄️ Climatización (aire acondicionado / calefacción)  
- 🏢 Altura del inmueble (principal, 1ª, 2ª...)  
- 🔢 Nº planta dentro del inmueble  
- 🏗️ Año de construcción  
- 💰 Gastos de comunidad e IBI  
- 🛠️ Estado (a reformar o listo para vivir)  
- 🏊‍♂️ Dotaciones adicionales (piscina, tenis, gimnasio)  
- 🚗 Garaje  

### 🔹 **Palabras clave en la descripción**
- ✨ Fantástica  
- 🏡 Maravillosa  
- 🌟 Oportunidad  
- 📌 Espaciosa  
- 🏠 Amplia  
- 🏢 Fenomenal  
- 👨‍👩‍👧‍👦 Apartamento para [familias, parejas]  
- 📏 Inmueble de más de XXXX metros cuadrados  

---

## **Fase 2: Incorporación de información geográfica**
Se implementará una API (Google Places u otra gratuita) para extraer datos de la zona según la localización del inmueble (latitud/longitud + radio).  

### 🔹 **Puntos de interés a identificar**
- 🚇 Transporte público  
- 🎓 Colegios y universidades  
- 🏬 Establecimientos comerciales  
- 🏖️ Playas y zonas verdes  
- 🏥 Hospitales y farmacias  
- 📚 Bibliotecas y centros deportivos  
- ⛽ Gasolineras y puntos de recarga de vehículos eléctricos  

---

## **Fase 3: Análisis de imágenes mediante visión artificial**
Se utilizará una API de visión artificial (Google Vision u otra) para detectar objetos en las fotos del inmueble.  

### 🔹 **Elementos detectables por estancia**
- **Cocina:** horno, nevera, microondas, lavadora, televisor, mesa, sillas, lavavajillas, ventana  
- **Habitaciones:** cama, mesitas de noche, armarios, ventana  
- **Salón-comedor:** chimenea, sofá, televisor, mesa, sillas, ventana  
- **Baño:** pila, WC, bidé, bañera, plato de ducha, ventana  
- **Terraza:** mobiliario, plantas  

---

## **Fase 4: Generación de descripciones mejoradas**
A partir de los datos extraídos de las imágenes, se enriquecerán las descripciones con adjetivos adicionales.  

### 🔹 **Adjetivos añadidos según análisis de imágenes**
- ☀️ Mucha luz natural  
- 📏 Espacios amplios  
- 🏡 Diseño moderno y acogedor  

---

## **Fase 5: Personalización del estilo de los anuncios**
Se generarán descripciones adaptadas según el público objetivo del anuncio.  

### 🔹 **Tipos de personalización del texto**
- 👔 **Formal o informal:** según el tipo de comprador  
- 👨‍👩‍👦 **Dirigido a familias, parejas o inversores**  
- 🏡 **Uso de jergas específicas del mercado**  

---

## **Ejecución del ejercicio**
📌 **Resultados esperados:**  
✅ Textos sugeridos para los anuncios  
✅ Información relevante de la zona basada en geolocalización  
✅ Keywords y adjetivos para mejorar los anuncios  
✅ Estilos de texto según el público objetivo  

---

## **📂 Entregables**
Se entregarán los siguientes elementos en un único WeTransfer:  

1️⃣ **Código fuente de la solución**  
2️⃣ **Video explicativo del código fuente (máximo 3 minutos)**  
3️⃣ **Video mostrando e interpretando los resultados (máximo 2 minutos)**  

---

## **🎥 SOLUCIÓN**
### 📌 Video y Demostración  
🔹 **Código fuente:** [![Ver en YouTube](https://img.shields.io/badge/🎥%20Código-red?logo=youtube&logoColor=white)](https://youtu.be/O_mOVcr4vlY?si=TXGakYguqF3IaBrZ)  
🔹 **Demostración:** [![Ver en YouTube](https://img.shields.io/badge/🎥%20Demostración-red?logo=youtube&logoColor=white)](https://youtu.be/82R7os-4LtY?si=zIIzCWVkMNWTGiWi)  
📌 *Haz clic con el botón derecho en el botón y selecciona "Abrir enlace en una nueva pestaña" para no salir del repositorio.*  
