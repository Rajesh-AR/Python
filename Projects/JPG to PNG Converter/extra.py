
img = Image.open('./pokedex/pikachu.jpg')
img1 = Image.open('./pokedex/astro.jpg')
print(img1.size)
filtered_img = img.convert('L')
filtered_img.save('grey.png', 'png')
img1.thumbnail((400,400))
img1.save('tumb1.png', 'png')
print(img1.size)
filtered_img.show()
print(img)
print(filtered_img)