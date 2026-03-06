import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- 1. Paramètres du circuit (Valeurs du TP) ---
R1 = 1e6    # 1 MOhm
C1 = 10e-9  # 10 nF
R2 = 1e3    # 1 kOhm
C2 = 10e-9  # 10 nF

# Calcul des fréquences de coupure théoriques
fc1 = 1 / (2 * np.pi * R1 * C1) # Env 15.9 Hz
fc2 = 1 / (2 * np.pi * R2 * C2) # Env 15.9 kHz

# --- 2. Définition de la fonction de transfert H(s) ---
# Numérateur : R1*C1*s
# Dénominateur : (R1*C1*R2*C2)s^2 + (R1*C1 + R2*C2)s + 1
num = [R1*C1, 0]
den = [R1*C1*R2*C2, R1*C1 + R2*C2, 1]
sys = signal.TransferFunction(num, den)

# Plage de fréquences pour le tracé (0.1 Hz à 1 MHz)
f = np.logspace(-1, 6, 1000)
w = 2 * np.pi * f
w, mag, phase = signal.bode(sys, w)

# --- 3. Création de la figure ---
plt.figure(figsize=(12, 10))

# --- SOUS-GRAPHIQUE 1 : GAIN ---
plt.subplot(2, 1, 1)
plt.semilogx(f, mag, color='blue', lw=2, label='Courbe réelle (Gain)')

# Tracé des asymptotes du gain
# 1. Pente +20dB/dec jusqu'à fc1
plt.semilogx([0.1, fc1], [-44, 0], 'g--', lw=1.5, label='Asymptotes')
# 2. Plateau à 0dB entre fc1 et fc2
plt.semilogx([fc1, fc2], [0, 0], 'g--', lw=1.5)
# 3. Pente -20dB/dec après fc2
plt.semilogx([fc2, 1e6], [0, -36], 'g--', lw=1.5)

plt.title('Diagramme de Bode - Filtre Passe-Bande (Préparation TP)', fontsize=14)
plt.ylabel('Gain (dB)', fontsize=12)
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()
plt.ylim(-50, 10)

# --- SOUS-GRAPHIQUE 2 : PHASE ---
plt.subplot(2, 1, 2)
plt.semilogx(f, phase, color='red', lw=2, label='Courbe réelle (Phase)')

# Tracé des asymptotes de la phase
# +90° avant fc1, 0° entre les deux, -90° après fc2
plt.semilogx([0.1, fc1/10], [90, 90], 'g--', lw=1.5, label='Asymptotes')
plt.semilogx([fc1*10, fc2/10], [0, 0], 'g--', lw=1.5)
plt.semilogx([fc2*10, 1e6], [-90, -90], 'g--', lw=1.5)

plt.ylabel('Phase (degrés)', fontsize=12)
plt.xlabel('Fréquence (Hz)', fontsize=12)
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.legend()
plt.yticks([-90, -45, 0, 45, 90])

plt.tight_layout()
plt.show()