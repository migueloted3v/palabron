# Guía personal: instalar, publicar y actualizar Palabrón

## 1. Subirlo a GitHub (una sola vez)

1. En github.com, crea un repositorio **público** llamado `palabron` sin README, porque ya traes uno.
2. En tu compu, dentro de la carpeta `palabron`:
   ```bash
   git init
   git add .
   git commit -m "Palabrón v1"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/palabron.git
   git push -u origin main
   ```
   Si no quieres usar la terminal, en la página del repo usa **Add file → Upload files** y arrastra todos los archivos, incluida la carpeta `tools`.
3. Activa GitHub Pages: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**.
4. Espera 1–2 minutos. Tu juego queda en `https://TU_USUARIO.github.io/palabron/`.

## 2. Instalarlo en el cel

- **Android (Chrome):** abre la URL, toca ⋮ y luego **Instalar app** o **Agregar a pantalla principal**.
- **iPhone (Safari):** abre la URL, toca **Compartir** y luego **Agregar a inicio**. Tiene que ser desde Safari.

Ábrelo una vez con internet para que se guarde todo. De ahí en adelante funciona sin conexión.

## 3. Publicar cambios

1. Edita `index.html`.
2. **Sube la versión en `sw.js`**, por ejemplo `palabron-v1` → `palabron-v2`. Si no lo haces, los celulares siguen mostrando la versión vieja guardada en caché.
3. Sube los cambios:
   ```bash
   git add .
   git commit -m "Descripción del cambio"
   git push
   ```
4. En el cel, abre la app con internet y luego ciérrala y vuélvela a abrir. La segunda apertura ya trae la versión nueva.

### Cambiar el color de acento

Todos los colores están al inicio del `<style>` de `index.html`, en `:root`. Para otro acento, cambia `--accent` y los tres tintes `--t14`, `--t22` y `--t30` (el mismo color en `rgba` con opacidad .14, .22 y .30). Hay un bloque para modo claro y dos para modo oscuro (el automático y el forzado); cambia los tres. Luego publica como arriba.

## 4. Si algo no se actualiza

- Confirma que subiste el número en `sw.js`.
- Android: Ajustes → Apps → Chrome → Almacenamiento → borrar datos del sitio. En iPhone: Ajustes → Safari → Avanzado → Datos de sitios web → borrar el de github.io.
- Ojo: borrar los datos del sitio también borra la partida guardada y los récords.

## 5. Cambiar el diccionario (opcional)

El diccionario va embebido en `index.html` dentro de `<script type="text/plain" id="dawg">`. Para regenerarlo con otra lista de palabras (un JSON con un arreglo de palabras en minúsculas, sin acentos):

```bash
python3 tools/build_dawg.py mi_lista.json
```

Se genera `dawg.b64`. Reemplaza con su contenido el texto dentro de esa etiqueta y publica como en el paso 3.

## 6. Qué cambió por versión

- **v1:** juego completo con compu en 3 niveles, modo familia, diccionario y pista.
- **v2:** diseño minimalista y modo oscuro. En `sw.js` va `palabron-v2`; la próxima vez que publiques cambios usa `palabron-v3`.

## 7. Ideas para siguientes versiones

- Arrastrar fichas además de tocarlas.
- Estadísticas por jugador (promedio por partida, mejor palabra de cada hija).
- Lista de palabras "familiares" para que la compu fácil solo juegue palabras conocidas.
