# 🧠 Buscaminas con Jugadores Automáticos: Voraz y Fuerza Bruta

Este proyecto implementa una versión del clásico juego **Buscaminas (Minesweeper)** en Python, acompañado por **dos jugadores automáticos** que intentan resolver el tablero de formas muy distintas:

- 🤖 **Jugador Voraz (Greedy):** elige la primera casilla desconocida.
- 🧠 **Jugador de Fuerza Bruta (Brute Force):** analiza todas las combinaciones posibles para seleccionar jugadas 100% seguras.

---

## 🎯 Objetivo

Evaluar y comparar el desempeño de dos estrategias automatizadas para resolver Buscaminas:

- Número de partidas ganadas vs. perdidas.
- Tiempo de ejecución por partida.
- Impacto de la estrategia en entornos inciertos.

---

## 📌 Características

- Tablero configurable (`ROWS` x `COLUMNS`)
- Generación aleatoria de minas (sin repetir posiciones)
- Garantía de que la **primera jugada nunca es una mina**
- Interfaz de consola intuitiva y visual
- Estadísticas automáticas tras 100 partidas:
  - ✅ Tasa de victoria
  - 🕒 Tiempo promedio
  - ⏱️ Tiempo total
  - 📁 Exportación automática de resultados en **archivos CSV** con dos variantes:
  - `resultados_buscaminas_*.csv` → con porcentaje de victorias (ej. `34.00%`)
  - `resultados_buscaminas_*(fraccion).csv` → con conteo (ej. `34/100`)


---

## 🧠 Estrategias Implementadas

### 1️⃣ Jugador Voraz (Greedy)
Selecciona la **primera casilla no revelada** del tablero sin realizar ningún análisis adicional.

- ✅ Muy rápido
- ⚠️ Alto riesgo de fallar
- 🧠 Sin inferencia

### 2️⃣ Jugador de Fuerza Bruta
Detecta la frontera de casillas alrededor de números visibles y **simula todas las combinaciones posibles** de minas. Elige una casilla que sea **segura en todas las combinaciones válidas**.

- ✅ Muy seguro si hay información suficiente
- ⏳ Lento por su complejidad (`O(2^n)` combinaciones)
- 🧠 Inteligencia combinatoria

---

## ⚙️ Estructura del Código

- `create_board()` – Inicializa el tablero y las minas
- `draw_board()` – Visualiza el tablero actual
- `adjacent_squares(i, j)` – Retorna minas y vecinos de una casilla
- `update_board(square)` – Revela una casilla y expande si está vacía
- `greedy_player()` – Retorna la primera casilla desconocida
- `brute_force_player()` – Analiza todas las combinaciones posibles y retorna una jugada segura
- `run_custom_experiment()` – Ejecuta una partida automática
- `main()` – Pregunta por el jugador, ejecuta 100 partidas y genera estadísticas

---

## 📈 Resultados de ejemplo

```text
🤖 Jugador: Fuerza Bruta

📊 Resultados después de 100 juegos:
🕒 Tiempo promedio por partida: 1.2389 segundos
✅ Porcentaje de juegos ganados: 92.00%
⏱️ Tiempo total para los 100 juegos: 0:02:03.895742
📁 CSV guardado: resultados_buscaminas_bruteforce.csv
📁 CSV resumen fracción: resultados_buscaminas_bruteforce(fraccion).csv

🤖 Jugador: Voraz (Greedy)

📊 Resultados después de 100 juegos:
🕒 Tiempo promedio por partida: 0.0018 segundos
✅ Porcentaje de juegos ganados: 34.00%
⏱️ Tiempo total para los 100 juegos: 0:00:00.210846
📁 CSV guardado: resultados_buscaminas_greedy.csv
📁 CSV resumen fracción: resultados_buscaminas_greedy(fraccion).csv

> ⚠️ Nota: Las tasas de éxito pueden variar por la aleatoriedad y la información disponible en el tablero.
```
---

## 🛠️ Requisitos

* Python 3.7 o superior

---

## 🚀 Cómo Ejecutar

```bash
python3 buscaminas.py
```

Al iniciar el programa, elige:

* `1` para el jugador heurístico (greedy)
* `2` para el jugador de fuerza bruta

---

## 📚 Posibles Mejoras

* Implementar un **jugador probabilístico** o basado en inferencia lógica
* Agregar una **interfaz gráfica** (ej. con `tkinter`)
* Guardar estadísticas en `.csv` para análisis posterior
* Permitir que el usuario juegue manualmente contra el AI

---

## 👨‍💻 Autores

Este proyecto fue desarrollado como parte de un taller académico sobre agentes automatizados y simulación de decisiones.

* Alejandro Pinzón – [@alejandro09pf](https://github.com/alejandro09pf)
* Juan David Sánchez – [@juandavid0420-rgb](https://github.com/juandavid0420-rgb)

