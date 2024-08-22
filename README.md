This Python script converts images into ASCII art using the PIL (Python Imaging Library) module. The script can be run directly from the command line, allowing you to specify the source image, destination file, and output width, or it can default to converting a predefined image.

Requirements:
Python 3.x, PIL (Pillow) library

To install the required library, run: "pip install pillow"

How It Works:

Image Scaling: The image is resized to a specified width while maintaining its aspect ratio, ensuring that the ASCII art output retains the correct proportions.

Grayscale Conversion: The image is converted to grayscale, which reduces the color depth to shades of gray. This simplifies the process of mapping pixel values to ASCII characters.

Pixel Mapping: Each pixel's intensity (from 0 to 255) is mapped to a corresponding ASCII character based on predefined levels of brightness. Darker pixels are represented by denser characters (e.g., @), while lighter pixels are represented by less dense characters (e.g., .).

ASCII Image Creation: The ASCII characters are arranged into lines matching the width of the scaled image, forming a complete text representation of the image.

Usage:

Command-Line Usage: 
You can run the script from the command line by providing the source image path, destination file path, and the desired width for the ASCII art.

Command: "python ascii_art.py <source_image_path> <destination_file_path> <size_s>"

<source_image_path>: Path to the input image file.

<destination_file_path>: Path to the output text file where the ASCII art will be saved.

<size_s>: The desired width of the ASCII art in characters.

Example
To convert an image named example.jpg to an ASCII art image with a width of 100 characters and save it as example.txt, you would run:
 "python ascii_art.py example.jpg example.txt 100"

Default Behavior:

If the script is run without proper command-line arguments, it will attempt to convert a default image located at ./images/nathandrake.jpg and save the ASCII art to ./images/nathandrake.txt with a width of 200 characters.

Error Handling:

The script includes basic error handling to manage issues such as:

Missing or incorrect command-line arguments.
Problems opening the specified image file.
Issues writing to the destination file.
If an error occurs, appropriate messages will be displayed to help you diagnose the problem.

Customization:

ASCII Character Set: You can customize the ASCII_CHARS list in the script to use different characters for the art. The default characters are @%#*+=-;:., where @ represents the darkest shade and . represents the lightest.

Range Width:
The range_width determines how pixel intensities are mapped to the ASCII characters. It is automatically calculated based on the number of characters in ASCII_CHARS.

License:
This script is open-source and can be freely used and modified. Contributions and suggestions for improvements are welcome.
