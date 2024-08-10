meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "PICK ME" : "ilgi odağı olmak isteyen kişi" ,
            "SLAY" : "göz kamaştıran, etkileyici kişi" , 
            "BUG" : "sistem açığı" ,
            }
            
word = input("Anlamadığınız bir kelime yazın(hepsini büyük harfle yazınız. ):")

if word in meme_dict.keys():
    print(meme_dict[word])
    
else:
    print("kelime bulunmamakatadır. Başka bir kelime dene!")
