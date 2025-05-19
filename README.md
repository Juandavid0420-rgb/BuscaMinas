# 🧠 Buscaminas con Jugador Voraz (Greedy Minesweeper AI)

Este proyecto implementa una versión del clásico juego **Buscaminas (Minesweeper)** en Python, acompañado por un jugador automatizado **voraz** (greedy), que toma decisiones de forma simple para seleccionar su siguiente jugada.

## 🎯 Objetivo

Evaluar el desempeño de un jugador voraz resolviendo el juego del Buscaminas, midiendo:
- El número de partidas ganadas/perdidas.
- El tiempo de ejecución por partida.
- El comportamiento del algoritmo en múltiples ejecuciones.

## 📌 Características

- Tablero de dimensiones configurables (`ROWS` x `COLUMNS`)
- Generación aleatoria de minas sin repetir posiciones.
- Interfaz de consola que muestra el tablero actualizado tras cada jugada.
- Jugador voraz que selecciona siempre la primera casilla desconocida.
- Garantía de que la **primera jugada no es una mina**.
- Cálculo de estadísticas tras 100 partidas: tasa de victoria y tiempo promedio.

## 🧠 Estrategia del Jugador Voraz

El jugador **no utiliza lógica probabilística ni inferencia**, simplemente selecciona la **primera casilla no revelada** del tablero en cada turno. Esto permite analizar cómo se comporta un enfoque simple ante un entorno incierto como el Buscaminas.

## ⚙️ Estructura del Código

- `create_board()` – Genera el tablero oculto y coloca minas.
- `draw_board()` – Muestra el estado actual del tablero visible.
- `get_index(i, j)` – Mapea coordenadas `(i, j)` a un índice lineal.
- `get_ij(index)` – Mapea índice lineal a coordenadas `(i, j)`.
- `get_neighbors(index)` – Devuelve los índices vecinos válidos.
- `count_adjacent_mines(index)` – Cuenta minas adyacentes a una celda.
- `reveal(index)` – Revela la casilla y propaga si es vacía.
- `update_board(index)` – Procesa la jugada del jugador.
- `has_won()` – Verifica si el jugador ganó.
- `greedy_player()` – Implementa la lógica del jugador voraz.
- `run_experiment()` – Ejecuta una partida completa.
- `main()` – Ejecuta 100 partidas, mide tiempos y muestra estadísticas.

## 📈 Estadísticas del Juego

Al ejecutar el script, se generan 100 partidas automáticas y se imprime un resumen como el siguiente:

Total de partidas: 100
Ganadas: 38
Perdidas: 62
Tiempo promedio por partida: 0.0018 segundos


> Nota: Debido a la naturaleza aleatoria y la simpleza del jugador, las tasas de victoria pueden ser bajas.

## 🛠️ Requisitos

- Python 3.7 o superior

## 🚀 Cómo Ejecutar

```bash
python3 buscaminas.py
```

## 📚 Posibles Mejoras
Implementar un jugador más inteligente que use lógica deductiva.

Agregar una interfaz gráfica (por ejemplo, con tkinter).

Guardar estadísticas en un archivo .csv para análisis externo.

Permitir que el usuario juegue manualmente.

## 👨‍💻 Autor
Este proyecto fue desarrollado como parte de una práctica para estudiar agentes voraces y simulación de juegos.
