# INA - MUIINF UPV

Asignatura del segundo año del Máster Universitario en Ingeniería Informática (MUIINF) en la UPV dedicada a la inteligencia ambiental. Este repositorio tiene como fin el desarrollo de los trabajos dedicados a esta(aquellos que requieran de código).

Participantes:
* César Augusto
* Zequan Liu

## Shelly Classic API

Este trabajo pretende crear una API para el dispositivo Shelly Plus que cumpla las siguientes condiciones:

* Controlar el dispositivo Shelly Plus
* Leer otros dispositivos del lab
* Triggerear una acción a algún dispositivo del lab
* Leer alguna API online (Opcional)

Se ha pensad un supuesto en el que el dispositivo conectado a este interruptor debería estar encendido 
sólo si la temperatura interior es inferior a la exterior(open-meteo API) y si las ventanas están cerradas