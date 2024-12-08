meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/sinirlenmek",
}

word = input("Anlamını Bilmediğiniz İnglizce Bir kelime yazın (büyük harflerle): ")

if word in meme_dict:
    print(word + ": " + meme_dict[word])  # Anlamını göster
else:
    print("Malesef yok.")  # Kelime yoksa mesaj ver
