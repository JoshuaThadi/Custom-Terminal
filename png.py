from PIL import Image

# Open the uploaded image
image_path = "/mnt/data/Screenshot 2025-02-09 123645.png"
image = Image.open(image_path)

# Convert image to RGBA mode
image = image.convert("RGBA")

# Get pixel data
pixels = image.getdata()

# Define the background color to remove (dark blue in this case)
# Sample a pixel from the corner (assumed to be background)
background_color = pixels[0]

# Create a new image with transparency
new_pixels = []
for pixel in pixels:
    # If the pixel is the background color, make it transparent
    if pixel == background_color:
        new_pixels.append((255, 255, 255, 0))  # Fully transparent
    else:
        new_pixels.append(pixel)

# Update image data
image.putdata(new_pixels)

# Save the transparent image
output_path = "/mnt/data/neovim_transparent.png"
image.save(output_path, "PNG")

# Return the processed image path
output_path

