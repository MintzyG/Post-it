from pathlib import Path
from tkinter.filedialog import askopenfilenames
import tkinter as tk

Selected_images_path : list = [] 
Paths = { 'images':[] }


def select_images() -> dict:
    window = tk.Tk()
    window.wm_attributes('-topmost', True)
    window.withdraw()
    
    path_images = askopenfilenames(parent=window, title='Selecione uma imagem', initialdir='')
    if path_images:
        print('Aquivos selecionados:')
        for path_image in path_images:
            Selected_images_path.append(Path(path_image))
        for x in range(len(Selected_images_path)):
            print(Selected_images_path[x])

        for picture in Selected_images_path:
            Paths['images'].append(str(picture))
        print(Paths['images'])
        return Paths
    else:
        print("No file selected")