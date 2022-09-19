"""Symbolic Link For Different Directory Dataset"""

import os
from glob import glob
from tqdm import tqdm

def get_glob_files(dataset_type:str, file_type:str):
    """
    dataset_type: [train, test, val]
    file_type: [images, annotations]
    """
    path = f'data/dataset/single/*/{dataset_type}/{file_type}/*'
    path_city = f'data/dataset/single/city/*/*/{dataset_type}/{file_type}/*'
    
    files = sorted(glob(os.path.join(path)))
    files_city = sorted(glob(os.path.join(path_city)))
    total = files + files_city

    print(f'Total {dataset_type} {file_type}:',len(total))
    
    return total

def symlink(glob_files, target_path):
    # change folder to labels from annotations
    if glob_files[0].split('/')[-2] == 'annotations':
        names = os.path.join(glob_files[0].split('/')[-3], 'labels')
    else:
        names = '/'.join(glob_files[0].split('/')[-3:-1])
    target_path_new = os.path.join(target_path, names)
    if not os.path.isdir(target_path_new):
        os.makedirs(target_path_new)
        
    for i, file in tqdm(enumerate(glob_files), desc=names, total=len(glob_files)):
        target = os.path.join(target_path, names, file.split('/')[-1])
        os.system(f"ln -s {file} {target}")

def main():
    """Main Function"""
    train_images = get_glob_files('train', 'images')
    val_images = get_glob_files('val', 'images')
    train_annos = get_glob_files('train', 'annotations')
    val_annos = get_glob_files('val', 'annotations')

    for glob in [train_images, val_images, train_annos, val_annos]:
        symlink(glob, 'data/dataset/')

if __name__ == '__main__':

    main()