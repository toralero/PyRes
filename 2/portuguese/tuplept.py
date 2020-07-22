pessoas_na_foto = ("Olga", "Simão", "Tomás")
print("Na foto estão", pessoas_na_foto)
print("A pessoa mais à esquerda é", pessoas_na_foto[0])

print("O Simão está nesta foto?")
if "Simão" in pessoas_na_foto:
    print("Simão está na foto")

print("Vamos ver se o Simão consegue mudar de nome")
pessoas_na_foto[1] = "Simzão"


