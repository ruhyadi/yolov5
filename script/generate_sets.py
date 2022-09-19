"""Generate images sets for training"""

import os
from glob import glob

def generate_sets(images_path: str, output_path: str):
    dump_txt = open(output_path, "w")
    files = sorted(glob(os.path.join(images_path, "*.jpg")))
    files = [os.path.join(".", file.split("dataset/")[-1]) for file in files]
    [dump_txt.write(file + "\n") for file in files]
    dump_txt.close()
    print("[INFO] Generated", output_path)

if __name__ == "__main__":
    generate_sets("data/dataset/train/images", "data/dataset/train.txt")
    generate_sets("data/dataset/val/images", "data/dataset/val.txt")