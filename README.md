# Ranger

Ranger es una herramienta de escaneo de red que permite a los usuarios identificar hosts activos en un rango de direcciones IP y obtener información sobre ellos. Esta herramienta está diseñada para ser fácil de usar y eficiente, aprovechando la concurrencia para acelerar el proceso de escaneo.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Características

- Escanea un rango de direcciones IP de manera rápida y eficiente.
- Obtiene información sobre cada host, incluyendo su dirección IP y dominio.
- Opcionalmente, puede mostrar la versión del servicio en ejecución en el host.
- Soporta múltiples hilos para un escaneo más rápido.

## Requisitos

- Python 3.x
- Paquetes de Python:
  - `socket`
  - `colorama`
  - `concurrent.futures`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/0xNerv/ranger.git
   cd ranger
