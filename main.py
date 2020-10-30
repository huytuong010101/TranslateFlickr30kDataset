from googletrans import Translator
import os
translator = Translator()

with open("./captions.txt", "r", encoding="utf8") as f:
    rows = f.read().splitlines()

index = 0
rows = rows[index:]

for row in rows:
    img, cap = row.split()[0], row.split()[1:]
    cap = " ".join(cap)
    result = translator.translate(cap, dest='vi', src="en").text

    lang = translator.detect(result).lang

    if lang == "vi":
        with open("./results.txt", "a", encoding="utf8") as f:
            f.write(img + " " + result + "\n")
        print("N.o:", index, "Success")
    else:
        with open("./bug.txt", "a", encoding="utf8") as f:
            f.write(img + " " + result + "\n")
        print("N.o:", index, "Fail")

    index += 1
    if index % 100 == 0:
        os.system('cls')
