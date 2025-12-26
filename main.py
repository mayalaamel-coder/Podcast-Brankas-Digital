from gradio_client import Client
import os
import time

# Hubungkan ke server Chatterbox yang luwes
try:
    client = Client("ResembleAI/Chatterbox_TTS_Demo")
except:
    print("Server lagi sibuk, coba lagi nanti.")

dialogs = [
    ("Aris", "Halo semuanya... selamat datang di episode khusus A-P-B-D An-lok."),
    ("Geo", "Spill de ti, Ris! Gue denger ini soal drama legendaris itu kan?"),
]

if not os.path.exists("podcast_output"):
    os.makedirs("podcast_output")

for i, (spk, txt) in enumerate(dialogs):
    print(f"Lagi minta server buat suara {spk}...")
    try:
        # Menembak API Space secara langsung
        result = client.predict(
            text=txt,
            reference_audio=None,
            exaggeration=0.5,
            api_name="/predict"
        )
        # Ambil path file hasil audio
        audio_path = result[0] if isinstance(result, (list, tuple)) else result
        os.rename(audio_path, f"podcast_output/{i+1:02d}_{spk}.mp3")
        print(f"Berhasil simpan audio {spk}")
    except Exception as e:
        print(f"Gagal di dialog {i}: {e}")
    
    time.sleep(2) # Jeda agar tidak dianggap spam
    
