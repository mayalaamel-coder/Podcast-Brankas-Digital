import edge_tts
import asyncio
import os

dialogs = [
    ("Aris", "Halo semuanya... selamat datang di episode khusus A-P-B-D An-lok. Hari ini kita bedah riset tentang gimana teknologi dijital nyelametin duit warga Jakarta triliunan rupiah."),
    ("Geo", "Spill de ti, Ris! Gue denger ini soal drama paling legendaris antara Ahok sama De-Pe-Er-De pas zaman itu kan?"),
    ("Aris", "Tepat banget. Kita bakal bahas E-Bad-jeting. Tapi sebelum masuk ke sana, kita harus tahu dulu betapa sus atau mencurigakannya sistem manual zaman dulu."),
    ("Geo", "Duh, kalau denger kata manual di birokrasi, pikiran gue langsung ke arah korupsi, pungli, sama tumpukan kertas yang berdebu."),
]

async def main():
    if not os.path.exists("podcast_output"):
        os.makedirs("podcast_output")
    
    for i, (spk, txt) in enumerate(dialogs):
        # Ardi untuk Aris (Pria), Gadis untuk Geo (Wanita)
        voice = "id-ID-ArdiNeural" if spk == "Aris" else "id-ID-GadisNeural"
        
        # TRIK BIAR GAK ROBOT:
        # Aris dibuat lebih lambat dan berat
        # Geo dibuat lebih cepat dan nada tinggi
        rate = "+0%" if spk == "Aris" else "+15%"
        pitch = "-3Hz" if spk == "Aris" else "+5Hz"
        
        communicate = edge_tts.Communicate(txt, voice, rate=rate, pitch=pitch)
        await communicate.save(f"podcast_output/{i+1:02d}_{spk}.mp3")
        print(f"Berhasil simpan: {spk}")

if __name__ == "__main__":
    asyncio.run(main())
    
