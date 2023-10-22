Para cambiar los threads utilizados solo hace falta cambiar el valor definido en la línea 3. Para conseguir los resultados con los diferentes tipos de calendarizadores, lo único que se debe hacer es modificar el pragma en la línea 45, donde cambiaremos el valor de *schedule* por uno de los siguientes:
- runtime
- static
- dynamic
- dynamic,2
- dynamic,4
- guided
- guided,2
- guided,4