from pathlib import Path
from tkinter.filedialog import askopenfilenames
import tkinter as tk

Selected_images_path : list = [] 

def select_images() -> list:
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
        return Selected_images_path
    else:
        print("No file selected")