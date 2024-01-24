from pathlib import Path
from tkinter.filedialog import askopenfilenames

Selected_images_path : list = [] 

def Select_images() -> list:
    path_images = askopenfilenames(title='Selecione uma imagem')
    if path_images:
        print('Aquivos selecionados:')
        for path_image in path_images:
            Selected_images_path.append(Path(path_image))
        return Selected_images_path
    else:
        print("No file selected")

teste = Select_images()

for x in range(len(teste)):
    print(teste[x])