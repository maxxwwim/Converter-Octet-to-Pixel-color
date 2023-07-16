# Converter Octet to Pixel color

This project is a Python script that allows you to convert binary files into pixelated images and create a video from these images. There are 16,777,216 color combinations available with 256 bit differing, making billions of possible combinations. A text or encrypting program before being passed the converter bit will become almost impossible to decode if you don't have the basic colors. It is possible to create a decoder that looks at pixels one by one. I may come back later on this project to make the necessary modifications.



## Installation
1. Make sure you have Python 3 installed on your system.
2. Clone this GitHub repository or download the `byt_to_pixel.py` file to your machine.

## Modification
1. Open the `byt_to_pixel.py` file in a text editor.
2. You can adjust the following parameters according to your needs:
   - `file_path`: Path to the binary file you want to convert.
   - `width`: Image width in pixels.
   - `height`: Image height in pixels.
   - `framesecond`: Number of images per second to create the video.
3. You can also modify the `color_codesA.json` file to define your own color codes. Make sure to follow the format.

## Usage
1. Place the binary file you want to convert in the same directory as `byt_to_pixel.py`.
2. Open a command prompt or terminal and navigate to the directory containing `byt_to_pixel.py`.
3. Run the following command to create pixelated images:
   ```
   python byt_to_pixel.py
   ```
4. The created images will be saved in the `outDir` directory in the current location.
5. To create a video from the images in AVI format (for more efficient color compression):
   ```
   python byt_to_pixel.py --create-video --output-format avi
   ```
   **Note:** The use of AVI format allows for significant color compression, but it may result in a substantial loss of quality, making pixel detection more challenging.
6. The resulting video will be saved in the same directory as the images.

**Note:** Ensure you have the following dependencies installed:
- `json`
- `os`
- `random`
- `string`
- `sys`
- `math`
- `concurrent.futures`
- `itertools.islice`
- `tqdm`
- `PIL`
- `cv2`
- `numpy`
- `moviepy`

## Warning
This script is designed for small binary files. Converting large files may take time and consume significant memory.

## Upcoming
A file for decrypting AVI format videos will be available soon. This will restore higher quality for easier pixel detection.

## Contributions
Contributions are welcome! If you find a bug or want to improve this script, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. Please see the `LICENSE` file for more information.

**Author:** [maxxwwim](https://github.com/maxxwwim)
