import tkinter as tk
import random

afirmacijas = [
    "Visam ir savs iemesls.",
    "Nekad nav par vēlu mainīt savu dzīvi.",
    "Mazs solis ir labāk nekā nekas.",
    "Tu esi dvēsele ķermenī, nevis ķermenis ar dvēseli",
    "Viss nav jādara perfekti."
]

logs = tk.Tk()
logs.title("Kortizoli")
logs.geometry("400x300")

teksts = tk.Label(logs, text="Nospied pogu, lai sāktu", wraplength=350)
teksts.pack(pady=20)

def radit_afirmaciju():
    teksts.config(text=random.choice(afirmacijas))

def elposana():
    teksts.config(text="Ieelpa... (4 sekundes)")
    logs.after(4000, izelpa)

def izelpa():
    teksts.config(text="Izelpa... (6 sekundes)")

poga_afirmacija = tk.Button(
    logs, text="Pozitīva doma", command=radit_afirmaciju
)
poga_afirmacija.pack(pady=5)

poga_elposana = tk.Button(
    logs, text="Elpošanas vingrinājums", command=elposana
)
poga_elposana.pack(pady=5)

logs.mainloop()
