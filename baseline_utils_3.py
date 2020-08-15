import random
import pandas as pd
import numpy as np
import os


def create_bow(file_path):
    """
    Transformation du document en sac de mots (BOW)
    Entrée:
        `file_path` chemin complet et nom de fichier
    Sortie
        dictionnaire `bow` du type {mot:fréquence}
    """
    bow = {}
    with open(file_path, encoding='utf8') as f:

        # #################
        # Code à compléter

        pass

        # #################

    return bow


def find_victim_sex(bow):
    """
    Détermine le sexe de la victime en fonction d'un un dictionnaire
    Entrée: dictionnaire sac de mots `bow` du type {mot:fréquence}
    Sortie: chaîne 'homme' ou 'femme'
    """
    sex = ''

    # #################
    # Code à compléter

    pass

    # Cas limites
    # Comparaison des fréquences des mots clés 'il' et 'elle'
    # Choix aléatoire lorsque les deux quantités sont égales

    # #################

    return sex


def predict(x, txt_files_folder):
    """
    Entrées:
        x dataframe avec pour colonnes ID, filename
        txt_files_folder chemin complet pour l'accès aux fichiers textes
    Sortie:
        y_hat : y estimé sous la forme dataframe avec pour colonnes ID, sexe
    """
    y_hat_list = []

    for index, row in x.iterrows():
        ID = row['ID']
        file_name = row['filename']
        file_path = os.path.join(txt_files_folder, file_name)

        bow = create_bow(file_path)
        sex = find_victim_sex(bow)

        # Ajout d'une ligne à y estimé
        y_hat_list.append([ID, sex])

    # Dataframe des prédictions
    y_hat = pd.DataFrame(y_hat_list, columns=['ID', 'sexe'])
    return y_hat


def accuracy_sex(y, y_hat):
    """
    Entrées:
        y     : y véritable sous la forme dataframe avec pour colonnes ID, sexe
        y_hat : y estimé sous la forme dataframe avec pour colonnes ID, sexe
    Sortie:
        précision
    """
    accuracy = 0

    # #################
    # Code à compléter

    pass

    # #################
    return accuracy
