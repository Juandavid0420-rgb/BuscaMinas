import math
import random
import time

# Tamaño del tablero y número de minas
ROWS = 10
COLUMNS = 10
MINE_COUNT = 10

# Variables globales del estado del juego
BOARD = []        # Representación visual del tablero lineal
MINES = set()     # Conjunto de índices donde hay minas
EXTENDED = set()  # Índices de casillas ya reveladas
MATRIX = [['?'] * COLUMNS for i in range(ROWS)]  # Matriz para los valores visibles

# Colores para la impresión en consola
class Colors(object):
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def colorize(s, color):
    """Devuelve el texto coloreado para impresión en consola."""
    return '{}{}{}'.format(color, s, Colors.ENDC)

def get_index(i, j):
    """Convierte coordenadas 2D a índice lineal."""
    if 0 > i or i >= COLUMNS or 0 > j or j >= ROWS:
        return None
    return i * ROWS + j

def create_board():
    """Crea el tablero e inserta las minas aleatoriamente."""
    squares = ROWS * COLUMNS
    BOARD.clear()
    MINES.clear()

    for _ in range(squares):
        BOARD.append('[ ]')  # Todas las casillas empiezan vacías

    while len(MINES) < MINE_COUNT:
        MINES.add(random.randint(0, squares - 1))  # Se agregan minas aleatorias

def draw_board():
    """Dibuja el tablero con coordenadas en la consola."""
    lines = []
    for j in range(ROWS):
        if j == 0:
            lines.append('   ' + ''.join(' {} '.format(x) for x in range(COLUMNS)))
        line = [' {} '.format(j)]
        for i in range(COLUMNS):
            line.append(BOARD[get_index(i, j)])
        lines.append(''.join(line))
    return '\n'.join(reversed(lines))  # Se imprime de abajo hacia arriba

def adjacent_squares(i, j):
    """Devuelve el número de minas alrededor de una casilla y sus vecinos."""
    num_mines = 0
    squares_to_check = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == dj == 0:
                continue
            coordinates = i + di, j + dj
            proposed_index = get_index(*coordinates)
            if not proposed_index:
                continue
            if proposed_index in MINES:
                num_mines += 1
            squares_to_check.append(coordinates)
    return num_mines, squares_to_check

def update_board(square, selected=True):
    """Actualiza el tablero revelando la casilla `square`."""
    i, j = square
    index = get_index(i, j)
    EXTENDED.add(index)

    if index in MINES:
        if not selected:
            return
        BOARD[index] = colorize(' X ', Colors.RED)
        return True  # Juego perdido

    num_mines, squares = adjacent_squares(i, j)
    MATRIX[i][j] = num_mines

    if num_mines:
        if num_mines == 1:
            text = colorize(num_mines, Colors.BLUE)
        elif num_mines == 2:
            text = colorize(num_mines, Colors.GREEN)
        else:
            text = colorize(num_mines, Colors.RED)
        BOARD[index] = ' {} '.format(text)
        return
    else:
        BOARD[index] = '   '
        for asquare in squares:
            aindex = get_index(*asquare)
            if aindex in EXTENDED:
                continue
            EXTENDED.add(aindex)
            update_board(asquare, False)

def reveal_mines():
    """Revela todas las minas (al perder)."""
    for index in MINES:
        if index in EXTENDED:
            continue
        BOARD[index] = colorize(' X ', Colors.YELLOW)

def has_won():
    """Verifica si se ha ganado el juego."""
    return len(EXTENDED | MINES) == len(BOARD)

def greedy_player():
    """Jugador simple que elige la primera casilla no revelada."""
    options = []
    for i in range(ROWS):
        for j in range(COLUMNS):
            if MATRIX[i][j] == '?':
                options.append((i, j))
    return options[0] if options else (0, 0)

def run_experiment(verbose=False):
    global BOARD, MINES, EXTENDED, MATRIX
    BOARD = []
    MINES = set()
    EXTENDED = set()
    MATRIX = [['?'] * COLUMNS for _ in range(ROWS)]
    
    # Elegir primera jugada aleatoria
    first_i = random.randint(0, ROWS - 1)
    first_j = random.randint(0, COLUMNS - 1)
    first_index = get_index(first_i, first_j)

    # Crear tablero evitando poner mina en la primera jugada
    while True:
        create_board()
        if first_index not in MINES:
            break

    start_time = time.time()

    # Ejecutar la primera jugada segura
    update_board((first_i, first_j))

    while True:
        square = greedy_player()
        mine_hit = update_board(square)
        if mine_hit or has_won():
            break

    end_time = time.time()
    duration = end_time - start_time
    won = 0 if mine_hit else 1

    if verbose:
        print(draw_board())
        print("Resultado:", "GANÓ" if won else "PERDIÓ", f"Tiempo: {duration:.4f}s")

    return duration, won


# ---------------------------------------------------------------
# ⚙️ PUNTO DE ENTRADA
if __name__ == '__main__':
    # 🔹 Primero se ejecuta UNA partida y se muestra el tablero
    print("🧪 Ejecutando una partida ejemplo con tablero visible:\n")
    dur, win = run_experiment(verbose=True)
    print("🔚 Fin de la partida\n")

    # 🔹 Luego se ejecutan los 100 experimentos silenciosos
    N = 100
    tiempos = []
    exitos = 0

    print('🔁 Ejecutando 100 experimentos con el jugador voraz...')

    for i in range(N):
        dur, win = run_experiment()
        tiempos.append(dur)
        exitos += win

    promedio_tiempo = sum(tiempos) / N
    porcentaje_exito = (exitos / N) * 100

    print(f'\n📊 Resultados después de {N} juegos:')
    print(f'🕒 Tiempo promedio por partida: {promedio_tiempo:.4f} segundos')
    print(f'✅ Porcentaje de juegos ganados: {porcentaje_exito:.2f}%')
