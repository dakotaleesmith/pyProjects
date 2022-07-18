import pyautogui
import pytesseract
from PIL import Image

def get_text(image):
    return pytesseract.image_to_string(image, config="--psm 6")

X = 813
Y = 746
WIDTH = 35
HEIGHT = 25

### Function code for future refactoring:
# def get_num(filename) -> int:
#   """Gets total stat roll number from character creation screen."""
#   filepath = f"{filename}.png""
## Can the 4 constants below be assigned in a single line?
#   X = 813
#   Y = 746
#   WIDTH = 35
#   HEIGHT = 25
#   screenshot = pyautogui.screenshot(filepath, region=(X, Y, WIDTH, HEIGHT))
#   img = Image.open(filepath)
## Line below refactored because the get_text function isn't necessary
#   text = pytesseract.image_to_string(img, config="--psm 6").rstrip("\n")
#   num = int(text)

screenshot = pyautogui.screenshot("stat.png", region=(X, Y, WIDTH, HEIGHT))
img = Image.open("stat.png")
text = get_text(img).rstrip("\n")
num = int(text)

clicks = 0

while num < 95:
    pyautogui.click(x=886, y=806)
    screenshot = pyautogui.screenshot("stat.png", region=(X, Y, WIDTH, HEIGHT))
    img = Image.open("stat.png")
    text = get_text(img).rstrip("\n")
    num = int(text)
    clicks += 1

print(f"Number of clicks: {clicks}")

### Insert code here that deletes the final screenshot
### Or refactor so the file is stored in memory rather than in the directory