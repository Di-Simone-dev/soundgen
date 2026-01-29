# 🔊 UI Sound Generator

Generatore di suoni per interfacce utente (typing sounds, button clicks, hover effects, notifiche) creato con Python.

## 📋 Descrizione

Questo progetto permette di creare suoni sintetici di alta qualità per interfacce utente, simili a quelli utilizzati in applicazioni moderne come OperaGX. I suoni sono generati proceduralmente utilizzando sintesi audio, permettendo completa personalizzazione di durata, tonalità e caratteristiche sonore.

## 🎵 Tipi di Suoni Disponibili

- **Typing Sound** (20ms) - Click breve e piacevole per feedback di digitazione
- **Button Click** (50-150ms) - Suono percussivo per click su pulsanti
- **Button Hover** (30ms) - Effetto sottile per hover del mouse
- **Notification** (300ms) - Suono a due toni per notifiche

## 🚀 Installazione

### Requisiti

- Python 3.6+
- NumPy
- SciPy

### Installazione dipendenze

```bash
pip install numpy scipy
```

## 💻 Utilizzo

### Utilizzo Base

Esegui lo script per generare tutti i suoni di esempio:

```bash
python generate_ui_sounds.py
```

Questo creerà automaticamente:
- `typing_sound.wav` (20ms)
- `button_click_short.wav` (50ms)
- `button_click_long.wav` (150ms)
- `hover_sound.wav` (30ms)
- `notification.wav` (300ms)

### Utilizzo Avanzato

Importa la funzione nel tuo codice Python:

```python
from generate_ui_sounds import generate_ui_sound

# Genera un typing sound personalizzato
generate_ui_sound('typing', duration_ms=25, output_file='my_typing.wav')

# Genera un button click lungo
generate_ui_sound('button_click', duration_ms=150, output_file='my_button.wav')

# Genera un hover effect
generate_ui_sound('button_hover', duration_ms=30, output_file='my_hover.wav')

# Genera una notifica
generate_ui_sound('notification', duration_ms=300, output_file='my_notification.wav')
```

## 🎛️ Parametri

### `generate_ui_sound(sound_type, duration_ms, output_file)`

- **sound_type** (str): Tipo di suono da generare
  - `'typing'` - Sound di digitazione
  - `'button_click'` - Click su pulsante
  - `'button_hover'` - Effetto hover
  - `'notification'` - Suono di notifica

- **duration_ms** (int): Durata del suono in millisecondi
  - Typing: 15-30ms consigliati
  - Button Click: 50-150ms consigliati
  - Hover: 20-40ms consigliati
  - Notification: 200-400ms consigliati

- **output_file** (str): Nome del file WAV di output

## 🔧 Personalizzazione

Puoi modificare le caratteristiche sonore modificando i parametri all'interno della funzione:

```python
# Esempio: modificare il typing sound
click = np.exp(-t * 200) * np.sin(2 * np.pi * 800 * t)  # Click iniziale
tone = np.exp(-t * 150) * np.sin(2 * np.pi * 1200 * t)  # Tono principale
```

**Parametri modificabili:**
- **Frequenze** (`2 * np.pi * 800`): Cambia il pitch del suono (Hz)
- **Decay rate** (`-t * 200`): Cambia la velocità di attenuazione
- **Mix** (`click * 0.4 + tone * 0.5`): Cambia il bilanciamento tra componenti

## 📊 Specifiche Tecniche

- **Sample Rate**: 44100 Hz
- **Bit Depth**: 16-bit PCM
- **Canali**: Mono
- **Formato**: WAV (RIFF)
- **Fade-out**: 5ms per evitare click audio

## 📁 Struttura del Progetto

```
.
├── generate_ui_sounds.py    # Script principale
├── generate_typing_sound.py # Script semplificato per typing sound
├── typing_sound.wav         # Esempio typing sound (20ms)
└── README.md               # Questo file
```

## 🎯 Esempi d'Uso

### Integrazione in un'App Web

```javascript
// Riproduci il typing sound ad ogni keystroke
const typingSound = new Audio('typing_sound.wav');

document.addEventListener('keypress', () => {
  typingSound.currentTime = 0;
  typingSound.play();
});
```

### Integrazione in Python/Tkinter

```python
from tkinter import *
import pygame

pygame.mixer.init()
click_sound = pygame.mixer.Sound('button_click.wav')

root = Tk()
btn = Button(root, text="Click me!", command=lambda: click_sound.play())
btn.pack()
root.mainloop()
```

## 🤝 Contribuire

Sentiti libero di:
- Aggiungere nuovi tipi di suoni
- Migliorare gli algoritmi di sintesi
- Ottimizzare le performance
- Correggere bug

## 📝 Licenza

Questo progetto è rilasciato sotto licenza MIT - sentiti libero di usarlo come preferisci.

## 🙏 Crediti

Creato con Python, NumPy e SciPy.
Ispirato dai suoni UI di OperaGX e altre applicazioni moderne.

## 📞 Supporto

Per domande o problemi, apri una issue su GitHub.

---

**Buon sound design! 🎵**
