import os
import numpy as np
import matplotlib.image as mpimg


def get_data(equilibre=False):
    #----------info---------------
    #Recup les photos dans chaque répertoire
    #
    #Input:
    #   equilibre= false ==> Prend toute les images dans le repertoire
    #   equilibre= True ==> Prend le mombre minimums de photo dans le répertoire
    #                       et prend le meme nombre d'image dans chaque répertoire
    #                   On a un jeu de donnée equilibre
    #
    #
    #Output:
    #list of array d'image
    #
    #
    #Mise a jour: 25/08/2021
    #----------end info---------------
    #list
    label=[]
    images_list=[]
    dataset_image=[]
    #dico
    dico_photo={}
    # Path
    path_v0='..'
    path_v1='raw_data'
    path_v2='photos_class'

    # Join various path components 
    image_path=os.path.join(path_v0,path_v1,path_v2)
    # list of directory
    list_directory_names = [d for d in os.listdir(image_path) if d.find('.')==-1]
    if equilibre==False:
        for name in list_directory_names:
            #creer le chemin global de chaque repertorie
            image_path_tmp=os.path.join(image_path,name)
            #recupére toute les noms des images dans le repertoire
            images_list_tmp = os.listdir(image_path_tmp)
            dico_photo[name]=images_list_tmp
            for image in images_list_tmp:
                #creer le chemin global de chaque images et le met dans une liste
                text_tmp=image_path_tmp+"/"+image
                images_list.append(text_tmp)
            #Creer une liste avec chaque label de chaque image   
            label_tmp=[name for i in range(len(images_list_tmp))]
            label.extend(label_tmp)
    else:
        for name in list_directory_names:
            #creer le chemin global de chaque repertorie
            image_path_tmp=os.path.join(image_path,name)
            #recupére toute les noms des images dans le repertoire
            images_list_tmp = os.listdir(image_path_tmp)
            dico_photo[name]=images_list_tmp
        #Recup le répertoire avec le moins de photo
        tmp_mini=999999
        for k, v in dico_photo.items():
            test=len(v)
            if tmp_mini>test:
                    tmp_mini=test
                    tmp_mini_key=k
            print(k,":", len(v))
        #recup les photos randomisé
        for k, v in dico_photo.items():
            path_tmp=os.path.join(image_path,k)
            #Ramdom les photo avec le nombre de photo du répertoire ou il y a le moins de photo
            list_a_extraire=np.random.choice(dico_photo[k], tmp_mini)
            for image in list_a_extraire:
                #creer le chemin global de chaque images et le met dans une liste
                text_tmp=path_tmp+"/"+image
                images_list.append(text_tmp)
            #Creer une liste avec chaque label de chaque image   
            label_tmp=[k for i in range(len(list_a_extraire))]
            label.extend(label_tmp)     
    #Recupère les images et les met dans un dataset
    for image in images_list:
        #Lit l'image sous forme d'array
        img = mpimg.imread(image)
        dataset_image.append(np.array(img))  
    return dataset_image, label, dico_photo
    
if __name__=='__main__':
     dataset_image, label, dico=get_data(equilibre=True)
     print(dico)