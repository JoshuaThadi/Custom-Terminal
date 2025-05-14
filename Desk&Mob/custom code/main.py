from PIL import Image

# Define a smaller set of ASCII characters for a more compact result
ASCII_CHARS = ['$', '#', '%', '?', '*', '+', ';', ':', ',', '.']

# Function to resize the image to a fixed width and height
def resize_image(image, new_width=50, new_height=25):  # Fixed width and height
    return image.resize((new_width, new_height))

# Function to convert the image to grayscale
def grayscale_image(image):
    return image.convert("L")

# Function to map pixel values to ASCII characters
def pixel_to_ascii(pixel_value):
    return ASCII_CHARS[pixel_value // 32]  # Adjust granularity for smaller output

# Function to convert the image to ASCII art
def image_to_ascii(image_path, new_width=50, new_height=25):  # Fixed width and height
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width, new_height)
    image = grayscale_image(image)

    ascii_str = ""
    for y in range(image.height):
        for x in range(image.width):
            pixel_value = image.getpixel((x, y))
            ascii_str += pixel_to_ascii(pixel_value)
        ascii_str += '\n'
    
    return ascii_str

# Path to your image
image_path = "F:\AsciiImageGen\PowerShell_5.0_icon.png"
ascii_image = image_to_ascii(image_path, new_width=50, new_height=25)  # Fixed size
print(ascii_image)
