from gradio_client import Client
import os
import time

# Hubungkan ke server Chatterbox yang luwes
client = Client("ResembleAI/Chatterbox_TTS_Demo")

dialogs = [
    ("Aris", "Halo semuanya... selamat datang di episode khusus A-P-B-D An-lok."),
    ("Geo", "Spill de ti, Ris! Gue denger ini soal drama legendaris itu kan?"),
]

# BUAT FOLDER DULU
output_folder = "podcast_output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i, (spk, txt) in enumerate(dialogs):
    print(f"Sedang memproses {spk}...")
    
    # Minta audio ke server
    result = client.predict(
        text=txt,
        reference_audio=None,
        exaggeration=0.5,
        api_name="/predict"
    )
    
    # Ambil lokasi file sementara dari server
    temp_audio_path = result[0] if isinstance(result, (list, tuple)) else result
    
    # PINDAHKAN KE FOLDER KITA
    final_path = os.path.join(output_folder, f"{i+1:02d}_{spk}.mp3")
    os.rename(temp_audio_path, final_path)
    
    # CEK APAKAH FILE SUDAH ADA (PENJAGA GAWANG)
    if os.path.exists(final_path):
        print(f"✅ BERHASIL: File {final_path} sudah tercipta!")
    else:
        print(f"❌ GAGAL: File {final_path} tidak ditemukan!")

# CETAK ISI FOLDER TERAKHIR UNTUK MEMASTIKAN GITHUB MELIHATNYA
print(f"Isi folder akhir: {os.listdir(output_folder)}")

