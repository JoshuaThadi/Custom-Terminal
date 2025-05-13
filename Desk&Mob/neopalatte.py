from PIL import Image

# Define two rows of colors (approximate shades from Neofetch output)
colors_row1 = [(0, 0, 0), (128, 0, 128), (0, 0, 255), (0, 128, 255), (0, 255, 255), (255, 255, 255)]
colors_row2 = [(64, 64, 64), (192, 64, 192), (96, 96, 255), (128, 128, 255), (160, 192, 255), (224, 224, 224)]
# Image size
width, height = 600, 100  # Full image width and height
block_width = width // len(colors_row1)  # Width of each color block
block_height = height // 2  # Half the height for each row

# Create a blank image
img = Image.new("RGB", (width, height))

# Fill the first row
for i, color in enumerate(colors_row1):
    for x in range(i * block_width, (i + 1) * block_width):
        for y in range(0, block_height):
            img.putpixel((x, y), color)

# Fill the second row
for i, color in enumerate(colors_row2):
    for x in range(i * block_width, (i + 1) * block_width):
        for y in range(block_height, height):
            img.putpixel((x, y), color)

# Show the generated color palette
img.show()

