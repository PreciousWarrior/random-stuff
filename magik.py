from wand import image

path = input("Enter a file path: ")
img = image.Image(filename=path)
text = "1"

if img.animation:
    img = img.convert('png')
img.transform(resize='400x400')

try:
    multiplier = int(text)
except ValueError:
    multiplier = 1
else:
    multiplier = max(min(multiplier, 10), 1)

img.liquid_rescale(width=int(img.width * 0.5),
                   height=int(img.height * 0.5),
                   delta_x=0.5 * multiplier,
                   rigidity=0)
img.liquid_rescale(width=int(img.width * 1.5),
                   height=int(img.height * 1.5),
                   delta_x=2 * multiplier,
                   rigidity=0)

img.save(filename=input("Enter output path: "))
