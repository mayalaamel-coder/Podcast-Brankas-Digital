import edge_tts, asyncio, os

# Trik: Menulis singkatan sesuai bunyinya agar tidak kaku
dialogs = [
    ("Aris", "Halo semuanya, selamat datang di episode khusus A-P-B-D An-lok. Hari ini kita bedah riset tentang gimana teknologi digital nyelametin duit warga Jakarta triliunan rupiah."),
    ("Geo", "Spill de ti, Ris! Gue denger ini soal drama legendaris Ahok sama De-Pe-Er-De pas zaman itu kan?"),
    ("Aris", "Tepat banget. Kita bahas E-Bad-jeting. Tapi, dulu itu sistemnya parah banget, Geo. Banyak tangan gaib yang main."),
    ("Geo", "Bentar, tangan gaib? Maksudnya ada yang tiba-tiba nyelipin anggaran siluman gitu?"),
    ("Aris", "Iya! Contohnya anggaran Yu-Pi-Es senilai empat koma dua miliar per unit. Padahal itu cuma baterai cadangan!"),
    ("Geo", "Gila sih! Empat miliar buat satu Yu-Pi-Es? Itu kelurahan apa pusat data n-a-s-a?"),
    ("Aris", "Makanya Ahok bikin Brankas Digital. Begitu waktu input habis, sistem terkunci otomatis atau lok!"),
    ("Geo", "Jadi kalau sudah di-lok, nggak ada lagi yang bisa ganti angka lewat pintu belakang ya?"),
    ("Aris", "Betul! Dan setiap perubahan ada audit trel-nya. Jejak digital nggak bisa dihapus, Geo."),
    ("Geo", "Wah, teknologi emang jadi hakim yang paling jujur ya buat lawan korupsi."),
]

async def main():
    if not os.path.exists("podcast_output"): os.makedirs("podcast_output")
    for i, (spk, txt) in enumerate(dialogs):
        voice = "id-ID-ArdiNeural" if spk == "Aris" else "id-ID-GadisNeural"
        # Geo dibuat sedikit lebih cepat agar lebih ekspresif
        rate = "+15%" if spk == "Geo" else "+0%"
        await edge_tts.Communicate(txt, voice, rate=rate).save(f"podcast_output/{i+1:02d}_{spk}.mp3")
        print(f"Done: {spk}")

if __name__ == "__main__":
    asyncio.run(main())
  
