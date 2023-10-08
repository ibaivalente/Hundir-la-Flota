import barcos_funciones as fun
import barcos_variables as var

fun.init_tablero_mio(fill=' ')

fun.init_tablero_maquina(fill=' ')

fun.init_tablero_visible(fill='?')

fun.generar_todos_los_barcos_mios()

fun.generar_todos_los_barcos_maquina()

fun.disparar(var.tablero_mio,var.tablero_maquina,var.tablero_visible)