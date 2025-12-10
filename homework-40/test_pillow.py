from PIL import Image
from pathlib import Path


def resize_image(path, save_to, size=(320, 320)):
    image = Image.open(path)
    image.thumbnail(size)
    image.save(save_to)


def get_thumb_path(path):
    file = Path(path)
    file_name = file.stem
    file_suffix = file.suffix
    new_name = f'{file_name}-small{file_suffix}'
    destination = file.parent / new_name
    return destination


def is_data_path_file(path) -> bool:
    data = Path(path)
    return data.is_file() 


def main(path, size):
    # If input path is file 
    if is_data_path_file(path):
        file_destination = get_thumb_path(path)
        resize_image(path, file_destination, size)
        print(f'Thumb saved into: {file_destination}')

    #If input path is directory
    else:
        directory = Path(path)
        file_suffix = ['.jpg', '.jpeg', '.png']

        new_folder = directory / 'thumb_photos'
        new_folder.mkdir(exist_ok=True)
        dir_destination = new_folder

        for file in directory.iterdir():
            #Skip files that already have -small in the name
            if '-small' in file.stem:
                continue

            thumb_name = f'{file.stem}-small{file.suffix}'
            destination = dir_destination / thumb_name

            #If file suffix (.jpg, .png, etc) is in file_suffix list
            if file.suffix in file_suffix:
                resize_image(file, destination, size)
                print(f'Thumb saved into: {destination}')


                

if __name__ == '__main__':
    path_file = r'/Users/vbrothanek/Pictures/Mist/desktop/9.png'
    path_dir = r'/Users/vbrothanek/Pictures/Mist/desktop/'
    size_file = (700, 700)
    size_dir = (200, 200)

    main(path_file, size_file)
    main(path_dir, size_dir)
