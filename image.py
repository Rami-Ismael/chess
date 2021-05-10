from PIL import Image

image = Image.open("chess-39335.png")

width, height = image.size
#<a href="https://www.freepnglogos.com/pics/chess">Chess from freepnglogos.com</a>

print(width, height)