# Converter Octet to Pixel color

Ce projet est un script Python qui permet de convertir des fichiers binaires en images pixélisées et de créer une vidéo à partir de ces images. Il existe 16 777 216 combinaisons de couleurs disponibles avec 256 bits différents, ce qui fait des milliards de combinaisons possibles. Un texte ou un programme de crypté avant d'être passé dans le bit converter deviendra presque impossible à décoder si vous n'avez pas la seed des couleurs. Il est possible de créer un décodeur qui regarde les pixels un par un. Je reviendrai peut-être plus tard sur ce projet pour apporter les modifications nécessaires.

Il y a aussi un script permettant de générée les couleurs a partir d'une seed.

![image](https://github.com/maxxwwim/Converter-Octet-to-Pixel-color/assets/109239740/50992874-3ca2-46f0-94ea-2035d7378e40)


## Install
1. Assurez-vous que Python 3 est installé sur votre système.
2. Clonez ce référentiel GitHub ou téléchargez le fichier `byt_to_pixel.py` sur votre machine.

## Update
1. Ouvrez le fichier `byt_to_pixel.py` dans un éditeur de texte.
2. Vous pouvez ajuster les paramètres suivants selon vos besoins :
   - `file_path` : chemin vers le fichier binaire que vous souhaitez convertir.
   - `width` : largeur de l'image en pixels.
   - `height` : hauteur de l'image en pixels.
   - `framesecond` : nombre d'images par seconde pour créer la vidéo.
3. Vous pouvez également modifier le fichier `color_codesA.json` pour définir vos propres codes de couleur. Ou utiliser le script de génération des couleurs pour le faire.

## Usage
1. Placez le fichier binaire que vous souhaitez convertir dans le même répertoire que `byt_to_pixel.py`.
2. Ouvrez une invite de commande ou un terminal et accédez au répertoire contenant "byt_to_pixel.py".
3. Exécutez la commande suivante pour créer des images pixélisées, modifier ces ligne a la fin du programme ou appelé le depuis un autre script :
```
   file_path = "C:\\Users\\thgl\\Documents\\iso\\backbox-8-desktop-amd64.iso"
   width = 1280
   height = 720
   framesecond = 60
   video_creator = BytToPixel(file_path, width, height, framesecond)
   video_creator.create_images()
   video_creator.create_video()
```
4. Les images créées seront enregistrées dans le répertoire `outDir` à l'emplacement actuel.
5. La vidéo se créer automatiquement a la fin de génération des images si il y a + de 2 images, puis supprime les images créer précédament 
   **Remarque :** L'utilisation du format AVI permet une compression importante des couleurs, mais cela peut entraîner une perte substantielle de qualité, ce qui rend la détection des pixels plus difficile, actuellement le script et en mp4, `video.write_videofile(output_file, codec='libx264rgb', fps=self.fps, audio=False, ffmpeg_params=['-crf', '0'])` la vidéo peu prendre une place importante.
6. La vidéo résultante sera enregistrée dans le même répertoire que les images.


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
  
```
pip install tqdm Pillow opencv-python numpy moviepy string itertools
```
## Warning
Ce script a était conçus pour toutes configuration et peu prendre un certain temps a générée les images.

## Upcoming
Un fichier pour décrypter les vidéos au format AVI ou MP4 sera bientôt disponible. Cela restaurera une meilleure qualité pour une détection plus facile des pixels, actuellement j'ai des difficulté a décoder les vidéos, je repprendrai ce projet plus tard.

## Contributions
Les contributions sont les bienvenues ! Si vous trouvez un bug ou souhaitez améliorer ce script, n'hésitez pas à ouvrir un problème ou à soumettre une demande d'extraction.

## License
Ce projet est sous licence Apache-2.0. Veuillez consulter le fichier "LICENCE" pour plus d'informations.

**Author:** [maxxwwim](https://github.com/maxxwwim)
