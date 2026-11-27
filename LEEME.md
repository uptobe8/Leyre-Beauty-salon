# Royal Beauty Studio V2

Abre index.html en un servidor web o utiliza el HTML autónomo. No necesita servicios externos.

Tres personajes de los GLB aportados: Rapunzel (rapunzel.glb), Elsa (primera de dos poses presentes en el GLB) y Anna. Retratos renderizados desde las geometrías y texturas originales. Vista 3D giratoria en WebGL2 (pose estática). La segunda variante Rapunzel rig no se utiliza porque su exportación presenta ojos blancos. No hay príncipes en esta tanda.

Tres servicios: color/cepillado/brillo/adornos de pelo; colorete/labios/sombra/purpurina; manicura de diez uñas con esmalte, francesa, estrellas y corazones. Las operaciones de belleza se aplican al retrato renderizado; manicura con ilustración SVG provisional. No son físicas ni deformación del cabello ni maquillaje 3D de textura UV. Salón provisional diseñado con CSS; pendiente de los modelos de mobiliario y herramientas.

Estrellas por servicio, deshacer, guardado local, sonido generado, diseño adaptable.

Atribuciones originales en assets. Los derechos de los personajes y diseños pertenecen a sus titulares; verificar los permisos de publicación y explotación. Rapunzel clásica: licencia no localizada en sus archivos.

## V2 — renovación visual
Portada independiente, selector visual de princesas, acceso directo a cada servicio, retorno y continuación, conservación de la clave de guardado V1. Presentación palaciega en violeta y dorado; ajuste de postura estática de Rapunzel, manos simétricas y posición de maquillaje corregida. No se añaden nuevos modelos externos. Los retratos interactivos y el salón siguen siendo provisionales hasta recibir los escenarios y accesorios.
Pruebas Chromium: portada móvil, selector, peluquería, maquillaje, diez uñas, recompensas, persistencia y cambio de princesa; sin errores JS observados. La vista 3D mantiene su implementación original y no se ha probado de nuevo en esta entrega.

## V3
Torre, secador y tijeras: imágenes renderizadas a partir de sus GLB originales, integradas en portada, ventana y herramientas. 14 peinados renderizados a partir del pack glTF y ajustados a Rapunzel y Anna. Elsa no admite sustitución por ahora porque su cabello está unido a la malla del cuerpo. Los nuevos peinados se aplican sobre retratos 2D, no sobre la vista giratoria 3D (que muestra el modelo original). Las tijeras abren el selector de peinados; el secador activa brillo y efecto visual. Se mantienen todas las opciones de V2 y el formato de guardado. Los archivos repetidos en otros formatos no se incluyen. Licencia de torre no adjunta; revisar antes de publicar.

## V4
Blancanieves añadida con retrato, máscara de pelo y geometría original. Maquillaje adaptado a su rostro. Peinado Beatrice añadido al catálogo (15 peinados alternativos para Rapunzel y Anna). Elsa y Blancanieves conservan su pelo original, con tinte y decoración 2D. Segundo escenario seleccionable: salón Shimokitazawa, vista interior renderizada de la fotogrametría aportada, con techo eliminado. Se mantiene el palacio original. No es un escenario 3D navegable. La fotogrametría presenta discontinuidades y zonas sin detalle. Los secadores/tijeras repetidos se conservan de V3. Licencias de Blancanieves y salón no adjuntas. No se verifica WebGL en esta actualización.
Pruebas Chromium V4: cuatro personajes, 15 peinados alternativos, selección y guardado del salón, maquillaje de Blancanieves, secador, tinte, manicura y recompensas; sin errores JS.

## V5
Tocador victoriano como tercer salón seleccionable, render del modelo original. Manicura sustituye la ilustración anterior por manos renderizadas del GLB, con tono de piel adaptado y diez regiones SVG ajustadas a las uñas; conserva esmalte, francesa, corazones, estrellas, deshacer y recompensas. El archivo Nail Polish Bottle contiene geometría plana de un icono, no una botella volumétrica; su render se usa como icono de herramienta. Licencias originales incluidas. Secador y pelo rizado y pack de peinados repetidos se mantienen sin duplicarlos. No se introducen personajes nuevos ni cambios en el guardado.

Pruebas V5 ejecutadas en Chromium: selección de tres salones, diez uñas, esmalte, corazones, francesa, deshacer, peluquería, maquillaje, recompensas y guardado; sin errores JS. Vista 3D no reevaluada.

## V6
Nuevo cuarto escenario: tocador moderno Furniture No-23, con espejo, cajón, asiento y caja de maquillaje, renderizado desde las 14 mallas del GLB. Conversión de color a sRGB para la vista previa. Haircut 3D Model es un icono de cara y tijeras, no un cabello; se integra como imagen en el catálogo de cortes. Licencias Sketchfab Standard originales incluidas. No se introducen personajes ni peinados adicionales. Se mantiene guardado, herramientas y todas las modalidades.

## V7 — revisión funcional
- Acciones progresivas sobre zonas de pelo, ojos, labios y mejillas. Champú, aclarado, secado, corte, tinte, brillo y flores. Limado, retirada de esmalte y conservación de decoración. Se requiere completar el porcentaje de tratamiento antes de obtener estrellas; premio único por princesa y servicio. El selector cancela correctamente y continuar está desactivado en partida nueva.
- Renderizador software Canvas 2D que dibuja las mallas triangulares texturizadas en perspectiva ortográfica, sin depender de WebGL. Permite girar los personajes y manos y aplicar tratamientos sobre sus zonas. Quince peinados disponibles para las cuatro princesas; Elsa y Blancanieves se adaptaron mediante separación aproximada de triángulos del pelo.
- Las tres escenas importadas tienen visor 3D giratorio, independiente del fondo durante los tratamientos. Palacio ilustrado sin malla. Los personajes tienen una reacción corporal corta, no animaciones esqueléticas/faciales completas. Recorte y peinado simplificados, no simulación física de mechones. Las manos son geometría real con regiones de uñas proyectadas; limado y adornos son efectos superficiales.
- No se añaden príncipes sin modelos aportados. Pruebas Chromium local, no verificación Safari físico ni publicación GitHub. La versión autónoma es grande; preferir ZIP para alojar. Se mantienen los créditos de las versiones previas.

## V8
Portada con cuatro modos, personalización y música. Día de relajación: secuencia peluquería, maquillaje y manicura. Todas las zonas de tratamiento muestran las mallas 3D por defecto, sin botón de cambio a 2D. Escenarios dibujados en Canvas mediante mallas 3D: salón Shimokitazawa desde una cámara interior, tocador victoriano, tocador moderno y torre de Rapunzel (exterior). Se mantienen los visores giratorios. Personajes y escenarios se renderizan en capas separadas, no hay un mundo 3D unificado ni simulación física del cabello. El salón fotogramétrico tiene imperfecciones del original. No se ha localizado otro castillo entre los archivos montados. Tres composiciones originales de música instrumental creadas para esta aplicación, no canciones Disney. Las descargas de Incompetech están bloqueadas en el entorno; se recomiendan como alternativas Fairytale Waltz (CC BY 4.0) y las obras del catálogo de Kevin MacLeod con su licencia individual.

## V9 — Rosa
- Portada rosa luminosa, selector de cuatro princesas, botones y paletas de tratamientos de alto contraste; se mantienen cuatro modos, música, guardado y recompensas.
- Nuevo salón 3D rosa construido con geometría y materiales procedurales (mármol, paredes, ventanas, estanterías, botellas y banco), reutilizando el tocador moderno original de Furniture No-23. Es una escena 3D estilizada, no un salón fotográfico. El salón escaneado, torre de Rapunzel y ambos tocadores anteriores siguen seleccionables. La cámara del nuevo salón se puede girar en el visor. Se conserva el renderizado de personajes/escenarios por capas separadas.
- En primera carga de V9, el escenario por defecto anterior Shimokitazawa migra a salón rosa (otros escenarios y todos los progresos se conservan). El selector desde Personalizar vuelve a Inicio al confirmar.
- HTML autónomo incluye scripts e imágenes. Música: las tres melodías instrumentales originales de V8. Sin despliegue ni prueba en Safari físico.

## V10
Selector unificado de cuatro princesas, cinco escenarios y diez canciones. Selección dorada y rosa; giro directo mediante arrastre en la previsualización y fuera de las zonas de tratamiento en el salón. Las zonas de tratamiento conservan los gestos. Nuevo renderizador WebGL con resolución nativa de pantalla hasta 3840 × 2160 y alternativa CPU mejorada. WebGL no está disponible en Chromium de pruebas: no se han verificado la fluidez GPU ni 4K real; los recursos originales tienen resolución limitada. Siete MP3 aportados, recodificados completos a 96 kbps; licencias de publicación no verificadas.

PASS Four modes
PASS Four princesses, five venues, ten songs
PASS Selection clearly marked
PASS Princess selection persists
PASS Tower selected
PASS Uploaded music selected
PASS Direct preview rotation
PASS Service opens directly in 3D
PASS No rotate buttons visible
PASS Direct rotation in salon
GPU available: False
PASS No JavaScript errors
PASS Mobile selector no horizontal overflow
PASS Relajación comienza en peluquería 3D
PASS Pelo progresa mediante interacción 3D
PASS Relajación avanza a maquillaje
PASS Maquillaje 3D completo
PASS Manicura siempre 3D
PASS Diez uñas tratadas en 3D
PASS Día completo, nueve estrellas
PASS Sin errores JS

## V11
Escenarios nuevos: Beauty Salon del archivo Blender 4.01 (405.496 triángulos de origen, 20 grupos de material; color UV de 8 imágenes empaquetadas, reducidas a máximo 2048 px; cámara original, planos recortados para el navegador). Se importan mallas base, no modificadores Blender ni iluminación Cycles, materiales PBR aproximados. Sweet Home Hair Salon convertido desde el XML y las mallas OBJ internas (muebles low poly del original). Se conserva todo el catálogo anterior. La mano articulada texturizada de Elena FF se usa duplicada y reflejada en una pareja; pose estática y 10 áreas de manicura reajustadas. Los GLB de mano sin textura son duplicados/variantes no usados; no se incorporan formatos redundantes. Licencia de Blender y SH3D no confirmada en sus archivos, revisar antes de publicación. No se garantiza fotorrealismo ni 4K efectivo.
