# Palabrón

Juego de palabras en español para el celular, sin anuncios. Cada quien forma palabras con 7 fichas en un tablero de 15×15 con casillas que multiplican puntos. Puedes jugar contra la computadora o pasar el cel entre 2 a 4 personas.

## Funciones

- **Contra la compu**, con tres niveles: fácil (palabras cortas y jugadas modestas), normal y difícil (siempre juega la jugada de mayor puntaje).
- **En familia**: de 2 a 4 personas en el mismo celular. Entre turnos aparece una pantalla que oculta las fichas del jugador anterior.
- **Diccionario integrado** con ~635,000 palabras en español, incluidas conjugaciones y plurales. Valida cada jugada automáticamente y también sirve para revisar si una palabra existe.
- **Pista**: sugiere la mejor jugada posible con tus fichas.
- **Zoom del tablero**: pellizca el tablero o toca la lupa para agrandarlo. Solo crece el tablero; tu atril y los botones se quedan fijos.
- **Funciona sin internet** una vez instalada (PWA).
- **Guarda la partida** en curso y tus récords en el mismo celular.
- **Diseño minimalista** con un solo color de acento y modo oscuro automático según el tema del celular.

## Diseño

La interfaz usa un solo color y cada tono significa algo:

| Elemento | Cómo se ve |
|---|---|
| Fichas ya jugadas | Tinta oscura (claras en modo oscuro), sin puntos para no saturar el tablero |
| Fichas que estás colocando | Azul de acento |
| Última jugada del rival | Contorno azul |
| Fichas de tu atril | Blancas con borde, con su valor en puntos |
| Casillas 2P / 3P | Tinte azul, más intenso en 3P |
| Casillas 2L / 3L | Grises, se distinguen por el peso de la etiqueta |
| Inicio | Punto azul al centro |

Tipografía: Schibsted Grotesk (Google Fonts), con fuentes del sistema como respaldo.

## Reglas

- La primera palabra pasa por la estrella del centro. Las siguientes se conectan con las que ya están, en una sola fila o columna.
- Todas las palabras que se formen deben existir en el diccionario. Se escriben sin acentos. Sí existe la Ñ y no hay K ni W.
- Casillas: **2L / 3L** multiplican la letra, **2P / 3P** multiplican la palabra. Solo cuentan el turno en que se cubren.
- Usar las 7 fichas en una jugada es un **Pleno**: +50 puntos. Los 2 comodines valen 0.
- La partida termina cuando alguien se queda sin fichas con la bolsa vacía (se lleva los puntos de las fichas que les quedaron a los demás) o cuando todos pasan dos veces seguidas.

## Cómo está hecho

| Pieza | Detalle |
|---|---|
| Interfaz | HTML + CSS + JavaScript sin frameworks ni paso de compilación, en un solo `index.html` |
| Diccionario | Lista comprimida en un DAWG (grafo acíclico dirigido de palabras): 635k palabras en ~530 KB, embebido en base64 |
| Rival | Generador de jugadas tipo Appel–Jacobson sobre el DAWG, con anclas y *cross-checks*. Evalúa miles de jugadas en milisegundos |
| Persistencia | `localStorage` (partida en curso, jugadores y récords) |
| Offline | `sw.js` con estrategia *cache-first* + `manifest.json` |

```
palabron/
├── index.html          # juego completo (motor + interfaz + diccionario)
├── manifest.json       # datos para instalar como app
├── sw.js               # service worker (offline y actualizaciones)
├── icon-192.png
├── icon-512.png
└── tools/
    └── build_dawg.py   # regenera el diccionario comprimido
```

## Créditos

La lista de palabras proviene de [an-array-of-spanish-words](https://github.com/words/an-array-of-spanish-words) (licencia MIT), derivada de la lista de Letterpress. Palabrón es un juego original y no está afiliado a ninguna marca comercial de juegos de mesa.
