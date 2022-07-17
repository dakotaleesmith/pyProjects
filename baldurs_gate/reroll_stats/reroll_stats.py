import pyautogui
import pytesseract
from PIL import Image

def get_text(image):
    return pytesseract.image_to_string(image, config="--psm 6")

X = 813
Y = 746
WIDTH = 35
HEIGHT = 25

screenshot = pyautogui.screenshot("stat.png", region=(X, Y, WIDTH, HEIGHT))
img = Image.open("stat.png")
text = get_text(img).rstrip("\n")
num = int(text)

clicks = 0

while num < 92:
    pyautogui.click(x=886, y=806)
    screenshot = pyautogui.screenshot("stat.png", region=(X, Y, WIDTH, HEIGHT))
    img = Image.open("stat.png")
    text = get_text(img).rstrip("\n")
    num = int(text)
    clicks += 1
    