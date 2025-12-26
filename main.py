import requests
import os
import time

# Token yang kamu berikan sudah saya masukkan
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-ind"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

dialogs = [
    ("Aris", "Halo semuanya... selamat datang di episode khusus A-P-B-D An-lok. Hari ini kita bedah riset tentang gimana teknologi dijital nyelametin duit warga Jakarta triliunan rupiah."),
    ("Geo", "Spill de ti, Ris! Gue denger ini soal drama paling legendaris antara Ahok sama De-Pe-Er-De pas zaman itu kan?"),
    ("Aris", "Tepat banget. Kita bakal bahas E-Bad-jeting. Tapi sebelum masuk ke sana, kita harus tahu dulu betapa sus atau mencurigakannya sistem manual zaman dulu."),
    ("Geo", "Duh, kalau denger kata manual di birokrasi, pikiran gue langsung ke arah korupsi, pungli, sama tumpukan kertas yang berdebu."),
    ("Aris", "Gak salah sih. Riset ini nyebutin kalau dulu, proses anggaran itu gelap banget. Masyarakat nggak bisa akses drafnya, dan semuanya serba tertutup."),
    ("Geo", "Bau-bau konspirasi ya? Berarti dulu nggak ada yang tahu duit pajak kita lari ke mana sebelum anggarannya diketok palu?"),
    ("Aris", "Gak ada. Titik paling kritisnya itu pas tahap re-typing atau pengetikan ulang dokumen setelah rapat. Di situ tangan gaib mulai main."),
    ("Geo", "Bentar, pengetikan ulang? Jadi setelah dibilang Deal, dokumennya diketik lagi secara manual? Itu mah celah banget buat ganti angka!"),
    ("Aris", "Ek-sek-li. Makanya muncul istilah Anggaran Siluman. Program yang nggak pernah dibahas di rapat, tiba-tiba muncul pas dokumennya mau dicetak."),
    ("Geo", "Red flag parah sih itu. Terus, pas Ahok masuk, dia langsung ganti ke digital kan?"),
]

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Error API: {response.text}")
        return None
    return response.content

if not os.path.exists("podcast_output"):
    os.makedirs("podcast_output")

print("Memulai proses Chatterbox Style (Hugging Face)...")

for i, (spk, txt) in enumerate(dialogs):
    print(f"Memproses dialog {i+1} ({spk})...")
    audio_bytes = query({"inputs": txt})
    
    if audio_bytes:
        with open(f"podcast_output/{i+1:02d}_{spk}.mp3", "wb") as f:
            f.write(audio_bytes)
        print(f"Berhasil simpan: {i+1:02d}_{spk}.mp3")
    
    # Jeda 2 detik biar nggak kena limit API Hugging Face
    time.sleep(2)

print("Semua audio selesai diproses!")

