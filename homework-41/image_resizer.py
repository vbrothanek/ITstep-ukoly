from PIL import Image
from pathlib import Path

class ImageResizer():
    def __init__(self, path):
        self.path = path
        
        if self.is_data_path_file(path):
            self.image = Image.open(path)
        

    def resize_to(self, *sizes):
        if self.is_data_path_file(self.path):
            for size in sizes:
                thumb = self.image.copy()
                thumb.thumbnail((size, size))
                destination_path = self.get_thumb_path(size)
                thumb.save(destination_path)
                print(f'Thumb saved into: {destination_path}')

        else:
            directory_path = Path(self.path)
            file_suffix = ['.jpg', '.jpeg', '.png']

            new_folder = directory_path / 'thumb_photos'
            new_folder.mkdir(exist_ok=True)
            print(f'New folder "thumb_photos" created in {directory_path}')

            dir_destination = new_folder

            for file in directory_path.iterdir():
                
                if '-small-' in file.stem:
                    continue
                
                elif file.suffix in file_suffix:
                    for size in sizes:
                        thumb_name = self.get_thumb_name(size, file.stem, file.suffix)
                        image_file = Image.open(file)
                        thumb = image_file.copy()
                        thumb.thumbnail((size, size))
                        thumb.save(dir_destination / thumb_name)
                        print(f'Thumb saved into: {dir_destination / thumb_name}')
                        
                
                
    def get_thumb_name(self, size, file, suffix):
        return f'{file}-small-{size}{suffix}'   
        

    def get_thumb_path(self, size):
        file = Path(self.path)
        file_name = file.stem
        file_suffix = file.suffix
        new_name = f'{file_name}-small-{size}{file_suffix}'
        destination = file.parent / new_name
        return destination


    def is_data_path_file(self, path) -> bool:
        data = Path(path)
        return data.is_file()
    



if __name__ == '__main__':
    my_image_resizer = ImageResizer(r'/Users/vbrothanek/Pictures/Mist/desktop/')
    my_image_resizer.resize_to(300,100)

