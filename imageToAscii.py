from PIL import Image

# Grayscale levels mapped to ASCII characters
ASCII_CHARS = "@%#*+=-;:."

def scale_image(image, new_width):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / original_width
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def convert_grayscale(image):
    # convert to greyscale
    return image.convert("L")

def map_pixels_to_ascii(image, range_width = 25):
    # mapping pixel intensity
    pixels = image.getdata()
    ascii_str = ""
    range_width = 256 // len(ASCII_CHARS)
    
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[min(pixel_value // range_width, len(ASCII_CHARS) - 1)]
    
    return ascii_str

def convert_image_to_ascii(image_path, ascii_out, new_width):
    # convesion to ascii
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}. {e}")
        return

    image = scale_image(image, new_width)
    image = convert_grayscale(image)

    ascii_str = map_pixels_to_ascii(image)
    
    img_width = image.width
    ascii_img = ""
    for i in range(0, len(ascii_str), img_width):
        ascii_img += ascii_str[i : (i + img_width)] + "\n"

    try:
        with open(ascii_out, 'w') as f:
            f.write(ascii_img)
    except Exception as e:
        print(f"Unable to write to file {ascii_out}. {e}")

if __name__ == '__main__':
    convert_image_to_ascii("nathandrake.jpg", "nathandrake.txt", 200)
