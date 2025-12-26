from gradio_client import Client
import os

# Menghubungkan ke Space yang kamu temukan
client = Client("ResembleAI/Chatterbox_TTS_Demo")

dialogs = [
    ("Aris", "Halo... selamat datang di episode khusus A-P-B-D An-lok. Hari ini kita bedah riset tentang teknologi dijital."),
    ("Geo", "Spill de ti, Ris! Gue denger ini soal drama legendaris Ahok sama De-Pe-Er-De kan?"),
]

if not os.path.exists("podcast_output"):
    os.makedirs("podcast_output")

for i, (spk, txt) in enumerate(dialogs):
    print(f"Lagi minta server Chatterbox buat suara {spk}...")
    
    # Memanggil fungsi predict dari Space Chatterbox
    # Parameter: (teks, audio_referensi, exaggeration, cfg, seed, temp, vad_trim)
    result = client.predict(
        text=txt,
        reference_audio=None, # Kita pakai suara default dulu
        exaggeration=0.5,     # Biar ekspresif (0.5 - 0.7 bagus)
        cfg=0.5,              # Kontrol kecepatan
        seed=0,               # Random seed
        temp=1.0,             # Keberagaman suara
        ref_vad_trim=0.5,
        api_name="/predict"
    )
    
    # Chatterbox biasanya kasih output dalam list/tuple, ambil path filenya
    audio_path = result[0] if isinstance(result, (list, tuple)) else result
    
    # Pindahkan hasil dari folder temporary ke folder kita
    os.rename(audio_path, f"podcast_output/{i+1:02d}_{spk}.mp3")
    print(f"Berhasil simpan: {spk}")
    
