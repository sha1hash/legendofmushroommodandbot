import pyautogui
import time

print("Placez la souris à l'endroit souhaité pour capturer les coordonnées. Appuyez sur Ctrl+C pour arrêter.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Coordonnées actuelles de la souris: ({x}, {y})", end="\r")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nScript arrêté par l'utilisateur.")
