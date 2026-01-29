import numpy as np
from scipy.io import wavfile

def generate_ui_sound(sound_type='typing', duration_ms=20, output_file='ui_sound.wav'):
    """
    Genera diversi tipi di suoni per UI
    
    Parametri:
    - sound_type: 'typing', 'button_click', 'button_hover', 'notification'
    - duration_ms: durata in millisecondi
    - output_file: nome del file di output
    """
    
    sample_rate = 44100
    duration = duration_ms / 1000.0
    t = np.linspace(0, duration, int(sample_rate * duration))
    
    if sound_type == 'typing':
        # Typing sound: click breve + tono medio
        click = np.exp(-t * 200) * np.sin(2 * np.pi * 800 * t)
        tone = np.exp(-t * 150) * np.sin(2 * np.pi * 1200 * t)
        harmonic = 0.3 * np.exp(-t * 180) * np.sin(2 * np.pi * 2400 * t)
        sound = click * 0.4 + tone * 0.5 + harmonic * 0.1
        
    elif sound_type == 'button_click':
        # Button click: più percussivo, decay più lento
        click = np.exp(-t * 80) * np.sin(2 * np.pi * 600 * t)
        bass = np.exp(-t * 60) * np.sin(2 * np.pi * 300 * t)
        mid = 0.5 * np.exp(-t * 100) * np.sin(2 * np.pi * 1000 * t)
        sound = click * 0.5 + bass * 0.3 + mid * 0.2
        
    elif sound_type == 'button_hover':
        # Hover: suono sottile e breve
        tone = np.exp(-t * 250) * np.sin(2 * np.pi * 1500 * t)
        high = 0.3 * np.exp(-t * 300) * np.sin(2 * np.pi * 2500 * t)
        sound = tone * 0.7 + high * 0.3
        
    elif sound_type == 'notification':
        # Notification: due toni (ding-dong)
        if duration_ms < 100:
            duration_ms = 300
            duration = duration_ms / 1000.0
            t = np.linspace(0, duration, int(sample_rate * duration))
        
        # Primo tono
        tone1 = np.exp(-t * 15) * np.sin(2 * np.pi * 800 * t) * (t < duration/2)
        # Secondo tono (leggermente più basso)
        tone2 = np.exp(-(t - duration/2) * 15) * np.sin(2 * np.pi * 600 * (t - duration/2)) * (t >= duration/2)
        sound = tone1 + tone2
        
    else:
        raise ValueError(f"Tipo di suono '{sound_type}' non riconosciuto")
    
    # Normalizzazione
    sound = sound / np.max(np.abs(sound))
    
    # Fade-out per evitare click
    fade_samples = min(int(0.005 * sample_rate), len(sound) // 4)
    fade = np.ones_like(sound)
    fade[-fade_samples:] = np.linspace(1, 0, fade_samples)
    sound = sound * fade
    
    # Conversione a 16-bit PCM
    sound_int = np.int16(sound * 32767 * 0.8)
    
    # Salvataggio
    wavfile.write(output_file, sample_rate, sound_int)
    
    print(f"✓ Creato: {output_file}")
    print(f"  Tipo: {sound_type}")
    print(f"  Durata: {duration_ms}ms")
    print(f"  Sample rate: {sample_rate}Hz")


# Esempi di utilizzo:
if __name__ == "__main__":
    
    # Typing sound (20ms)
    generate_ui_sound('typing', duration_ms=20, output_file='typing_sound.wav')
    
    # Button click breve (50ms)
    generate_ui_sound('button_click', duration_ms=50, output_file='button_click_short.wav')
    
    # Button click lungo (150ms) - simile ai tuoi file
    generate_ui_sound('button_click', duration_ms=150, output_file='button_click_long.wav')
    
    # Hover effect (30ms)
    generate_ui_sound('button_hover', duration_ms=30, output_file='hover_sound.wav')
    
    # Notification (300ms)
    generate_ui_sound('notification', duration_ms=300, output_file='notification.wav')
    
    print("\n✅ Tutti i suoni sono stati generati!")