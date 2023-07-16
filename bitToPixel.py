import json
import os
import random
import string
import sys
import math
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from itertools import islice
from tqdm import tqdm
from PIL import Image
import cv2
import numpy as np
from moviepy.editor import ImageSequenceClip
class BytToPixel:
    def __init__(self, file_path, width, height, framesecond=25):
        self.file_path = file_path
        self.width = width
        self.height = height
        self.fps = framesecond
        self.current_directory = os.getcwd()
        self.output_directory = f"{self.current_directory}/outDir/{''.join(random.choices(string.ascii_lowercase + string.digits, k=8))}"
        os.makedirs(self.output_directory, exist_ok=True)
        self.color_codes = self.load_color_codes_from_json(f'{self.current_directory}/color_codesA.json')
    def load_color_codes_from_json(self, filename):
        print("Loading color codes from JSON file...")
        try:
            with open(filename, 'r') as file:
                color_codes = json.load(file)
            print("Color codes loaded successfully.")
            return color_codes
        except (IOError, json.JSONDecodeError) as e:
            print("Error loading color codes from JSON file:", str(e))
            return {}
    def create_images(self):
        print("Creation of images from file bytes...")
        file_size = os.path.getsize(self.file_path)
        with open(self.file_path, 'rb') as file:
            byte_data = file.read()
        image_size = self.width * self.height
        num_images = math.ceil(file_size / image_size)
        if num_images == 0:
            print("The file is too small to create a single image.")
            return
        byte_count = 0
        with tqdm(total=num_images, desc="Creating Images", unit="image") as pbar:
            for i in range(num_images):
                output_file = f"{self.output_directory}/image_{i+1}.png"
                image = Image.new('RGB', (self.width, self.height))
                pixel_data = []
                for y in range(self.height):
                    for x in range(self.width):
                        byte_index = i * image_size + (y * self.width + x)
                        if byte_index < len(byte_data):
                            byte = byte_data[int(byte_index)]
                            byte_str = bin(byte)[2:].zfill(8)
                            color = self.color_codes.get(byte_str)
                            if color is not None:
                                rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
                                pixel_data.append(rgb)
                            else:
                                pixel_data.append((0, 0, 0))
                        else:
                            pixel_data.append((0, 0, 0))
                image.putdata(pixel_data)
                image.save(output_file)
                byte_count += len(pixel_data)
                pbar.set_postfix({"Bytes Processed": byte_count})
                pbar.update(1)
                print(f"Image {i+1} created. Bytes processed: {byte_count}/{len(byte_data)}. Byte index: {byte_index}")
        print(f"{num_images} images created successfully.")
    def create_video(self):
        print("Create video from images...")
        image_files = [f for f in os.listdir(self.output_directory) if f.endswith(".png")]
        image_files.sort()
        image_clips = []
        for image_file in image_files:
            image_path = os.path.join(self.output_directory, image_file)
            image = Image.open(image_path)
            image = image.convert('RGB')
            image_array = np.array(image)
            image_clips.append(image_array)
        output_file = os.path.join(self.output_directory, 'video.mp4')
        video = ImageSequenceClip(image_clips, fps=self.fps)
        # Utilisez le codec libx264rgb pour une compression sans perte de qualité des pixels
        # Réglez le paramètre de compression CRF à une valeur élevée ou 0 pour un encodage sans perte
        video.write_videofile(output_file, codec='libx264rgb', fps=self.fps, audio=False, ffmpeg_params=['-crf', '0'])
        for image_file in image_files:
            image_path = os.path.join(self.output_directory, image_file)
            os.remove(image_path)
        print("Video created successfully.")
file_path = "C:\\Users\\thgl\\Documents\\iso\\backbox-8-desktop-amd64.iso"
width = 1280
height = 720
framesecond = 60
video_creator = BytToPixel(file_path, width, height, framesecond)
video_creator.create_images()
video_creator.create_video()
