from vilib import Vilib
from vilib import Face
import pickle

from os import getlogin

username = getlogin()


def main():
    
    pic_path=f'/home/{username}/trainer/Jackie_Chan'
    model_path=f"/home/{username}/trainer/encodings.pickle"
    Face.training("Jackie", pic_path,model_path)

    datas = []
    with open(model_path,'rb') as f:
        while True:
            try:
                datas.append(pickle.load(f))              
            except EOFError:
                break

    print(datas)
        
if __name__ == "__main__":
    main()