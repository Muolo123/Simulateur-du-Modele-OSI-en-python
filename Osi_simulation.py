import tkinter as tk

# ======================
# VARIABLES
# ======================
etapes = []
index = 0
animation_active = False

# ======================
# ENCAPSULATION REALISTE
# ======================
def preparer_encapsulation(message):
    global etapes

    # Application
    application = message

    # Presentation (encodage simple)
    presentation = message.upper()

    # Session
    session = f"SESSION[{presentation}]"

    # Transport (segmentation)
    segments = [presentation[i:i+2] for i in range(0, len(presentation), 2)]

    # Réseau (paquet)
    paquet = {
        "IP_source": "192.168.1.10",
        "IP_dest": "192.168.1.20",
        "data": segments
    }

    # Liaison de données (trame)
    trame = {
        "MAC_source": "AA:BB:CC:DD",
        "MAC_dest": "11:22:33:44",
        "payload": paquet
    }

    # Physique (bits)
    bits = ' '.join(format(ord(c), '08b') for c in presentation)

    etapes = [
        f"Application (HTTP)\nMessage : {application}",
        f"Presentation (TLS)\nEncodage : {presentation}",
        f"Session (NetBIOS)\nSession : {session}",
        f"Transport (TCP)\nSegments : {segments}",
        f"Reseau (IP)\nPaquet : {paquet}",
        f"Liaison de données (Ethernet)\nTrame : {trame}",
        f"Physique (Signal)\nBits : {bits}"
    ]


# ======================
# DECAPSULATION REALISTE
# ======================
def preparer_decapsulation(message):
    global etapes

    # Reconstruction des structures
    presentation = message.upper()

    segments = [presentation[i:i+2] for i in range(0, len(presentation), 2)]

    paquet = {
        "IP_source": "192.168.1.10",
        "IP_dest": "192.168.1.20",
        "data": segments
    }

    trame = {
        "MAC_source": "AA:BB:CC:DD",
        "MAC_dest": "11:22:33:44",
        "payload": paquet
    }

    bits = ' '.join(format(ord(c), '08b') for c in presentation)

    etapes = [
        f"Physique (Signal)\nBits reçus : {bits}",
        f"Liaison de données (Ethernet)\nExtraction trame : {trame}",
        f"Reseau (IP)\nExtraction paquet : {paquet}",
        f"Transport (TCP)\nRéassemblage : {''.join(segments)}",
        f"Session (NetBIOS)\nFermeture session",
        f"Presentation (TLS)\nDécodage : {message.lower()}",
        f"Application (HTTP)\nMessage final : {message}"
    ]


# ======================
# ANIMATION
# ======================
def lancer_animation():
    global index, animation_active

    if index < len(etapes) and animation_active:
        sortie.config(text=etapes[index])
        index += 1
        fenetre.after(1200, lancer_animation)
    else:
        sortie.config(text="✔ Simulation terminée")
        animation_active = False


# ======================
# BOUTONS
# ======================
def demarrer_encap():
    global index, animation_active
    message = entree.get()

    if message == "":
        sortie.config(text="⚠ Veuillez entrer un message")
        return

    preparer_encapsulation(message)
    index = 0
    animation_active = True
    lancer_animation()


def demarrer_decap():
    global index, animation_active
    message = entree.get()

    if message == "":
        sortie.config(text="⚠ Veuillez entrer un message")
        return

    preparer_decapsulation(message)
    index = 0
    animation_active = True
    lancer_animation()


# ======================
# INTERFACE
# ======================
fenetre = tk.Tk()
fenetre.title("Simulation OSI Pro")
fenetre.geometry("650x500")
fenetre.configure(bg="#1e1e1e")

titre = tk.Label(
    fenetre,
    text="SIMULATION MODÈLE OSI (AVANCÉE)",
    font=("Arial", 16, "bold"),
    fg="cyan",
    bg="#1e1e1e"
)
titre.pack(pady=10)

tk.Label(
    fenetre,
    text="Entrez un message :",
    fg="white",
    bg="#1e1e1e"
).pack()

entree = tk.Entry(fenetre, width=40, font=("Arial", 12))
entree.pack(pady=5)

tk.Button(
    fenetre,
    text="▶ Encapsulation",
    command=demarrer_encap,
    bg="green",
    fg="white"
).pack(pady=5)

tk.Button(
    fenetre,
    text="◀ Décapsulation",
    command=demarrer_decap,
    bg="orange",
    fg="black"
).pack(pady=5)

sortie = tk.Label(
    fenetre,
    text="",
    wraplength=600,
    justify="left",
    font=("Arial", 12),
    fg="white",
    bg="#2b2b2b",
    width=70,
    height=12
)

sortie.pack(pady=20)

fenetre.mainloop()