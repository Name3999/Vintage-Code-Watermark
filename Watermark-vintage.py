#-----------------------------------------------------------------
#---------------------   Watermark-vintage   ---------------------
#--------------------------   Bud Radu   -------------------------
#--------------------   29/05/2026 21:00:07   --------------------
#-----------------------------------------------------------------
import datetime
import random
import pyperclip

print("Introdu numele proiectului iar mai apoi numele tau")

prj = input("Numele proiectului este? : ......")
nume = input("Numele tau este? : ......")
data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
forma = ["=", "-", "*", "_"]
alegere_forma = random.choice(forma)
L = random.choice(list(range(40,70)))

def linie_plina():
    return alegere_forma * L

def linie_cu_text(text):
    text = f"   {text}   "
    return text.center(L, alegere_forma)

for i in range(5):
    if i == 0 or i == 4:
        print(linie_plina())
    elif i == 1:
        print(linie_cu_text(prj))
    elif i == 2:
        print(linie_cu_text(nume))
    elif i == 3:
        print(linie_cu_text(data))

output = (
    linie_plina() + "\n" +
    linie_cu_text(prj) + "\n" +
    linie_cu_text(nume) + "\n" +
    linie_cu_text(data) + "\n" +
    linie_plina()
)

pyperclip.copy(output)
print("\n S-a copiat in clipboard")

input("\n Enter pentru a inchide")
