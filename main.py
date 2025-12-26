import requests
import os
import time

API_TOKEN = "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"
# Pakai model yang lebih stabil untuk bahasa Indonesia
API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-ind"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

dialogs = [
    ("Aris", "Halo... selamat datang di episode khusus A-P-B-D An-lok. Hari ini kita bedah riset tentang teknologi dijital."),
    ("Geo", "Spill de ti, Ris! Gue denger ini soal drama legendaris Ahok sama De-Pe-Er-De kan?"),
]

def query(payload):
    # Kita tambah pengulangan kalau modelnya masih loading
    for _ in range(3): 
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return response.content
        elif "estimated_time" in response.text:
            print("Model sedang loading, nunggu sebentar...")
            time.sleep(20) # Tunggu 20 detik
        else:
            print(f"Error: {response.text}")
    return None

if not os.path.exists("podcast_output"):
    os.makedirs("podcast_output")

for i, (spk, txt) in enumerate(dialogs):
    print(f"Lagi bikin suara {spk}...")
    audio_bytes = query({"inputs": txt})
    if audio_bytes:
        with open(f"podcast_output/{i+1:02d}_{spk}.mp3", "wb") as f:
            f.write(audio_bytes)
        print(f"Berhasil simpan audio {i+1}")

# Pastikan folder tidak kosong sebelum selesai
print(f"Isi folder sekarang: {os.listdir('podcast_output')}")

