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
