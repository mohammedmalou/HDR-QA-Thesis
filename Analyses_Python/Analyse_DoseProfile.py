import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dose_profile_example.csv")  # fichier à ajouter plus tard

plt.plot(data["distance_mm"], data["dose_Gy"])
plt.xlabel("Distance (mm)")
plt.ylabel("Dose (Gy)")
plt.title("Profil de dose - Exemple HDR")
plt.grid(True)
plt.show()
