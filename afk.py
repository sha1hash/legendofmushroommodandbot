import pyautogui
import time
from PIL import ImageGrab

# Fonction pour détecter un carré rouge sur l'écran
def detect_red_square():
    screenshot = ImageGrab.grab()
    width, height = screenshot.size

    # Convertir la capture d'écran en RGB
    screenshot = screenshot.convert("RGB")

    for x in range(width):
        for y in range(height):
            r, g, b = screenshot.getpixel((x, y))
            if r > 200 and g < 50 and b < 50:  # Condition pour détecter la couleur rouge
                return (x, y)
    return None

try:
    while True:
        # Bouger la souris tous les 5 secondes
        pyautogui.moveRel(10, 0, duration=0.25)
        time.sleep(5)

        # Détecter le carré rouge
        red_square_position = detect_red_square()
        if red_square_position:
            # Si un carré rouge est détecté, cliquer sur la coordonnée précise capturée
            precise_coord = (672, 155)  # Remplacez par les coordonnées précises capturées
            pyautogui.click(precise_coord)
            print(f"Carré rouge détecté à {red_square_position}. Clic effectué à {precise_coord}.")

except KeyboardInterrupt:
    print("Script arrêté par l'utilisateur.")
