import os
import time
from googletrans import Translator
import re

def translate_file(input_file, output_file):
    translator = Translator()
    
    try:
        # Lecture du fichier d'entrée et traduction de l'ensemble du texte
        with open(input_file, 'r', encoding='utf-8') as f_input:
            original_text = f_input.read()
        
        # Découpage du texte en morceaux plus petits tout en préservant les lignes complètes
        chunk_size = 1000  # Taille maximale d'un morceau de texte
        chunks = []
        current_chunk = ''
        for line in original_text.split('\n'):
            if len(current_chunk) + len(line) + 1 <= chunk_size:  # +1 pour le caractère de saut de ligne
                current_chunk += line + '\n'
            else:
                if current_chunk.strip():  # Ajouter uniquement les morceaux non vides
                    chunks.append(current_chunk)
                current_chunk = line + '\n'
        if current_chunk.strip():  # Ajouter le dernier morceau s'il n'est pas vide
            chunks.append(current_chunk)
        
        # Traduction de chaque morceau de texte
        translated_chunks = []
        for chunk in chunks:
            translated_chunk = translator.translate(chunk, dest='fr').text
            translated_chunks.append(translated_chunk)
        
        # Reconstitution du texte traduit
        translated_text = ''.join(translated_chunks)
        
        # Recherche et récupération des liens originaux
        original_links = re.findall(r'\]\s*\(\s*.*?\)', original_text)
        
        # Recherche et récupération des liens traduits
        translated_links = re.findall(r'\]\s*\(\s*.*?\)', translated_text)
        
        # Remplacement des liens traduits par les liens originaux dans le texte traduit
        for original_link, translated_link in zip(original_links, translated_links):
            translated_text = translated_text.replace(translated_link, original_link)
        
        # Suppression des espaces entre les double étoiles
        translated_text = re.sub(r'\*\*\s*([^*]+?)\s*\*\*', r'**\1**', translated_text)
        
        # Écriture du texte traduit dans le fichier de sortie
        with open(output_file, 'w', encoding='utf-8') as f_output:
            f_output.write(translated_text)
    except Exception as e:
        print(f"Une erreur est survenue lors de la traduction du fichier {input_file}: {e}")
        # Écriture du fichier d'échec
        failure_output_file = output_file.replace(".fr.md", ".echec.md")
        with open(failure_output_file, 'w', encoding='utf-8') as f_failure:
            f_failure.write(f"Une erreur est survenue lors de la traduction du fichier {input_file}: {e}")

# Utilisation du script pour traduire tous les fichiers dans le dossier spécifié
input_folder = "/home/shell/Documents/SAM/REARMframeworks/generated_pages/techniques/"
output_folder = "/home/shell/Documents/SAM/REARMframeworks/generated_pages/techniques/"

# Parcours de tous les fichiers dans le dossier d'entrée
for filename in os.listdir(input_folder):
    if filename.endswith(".md"):  # Sélectionner uniquement les fichiers avec l'extension .md
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename.replace(".md", ".fr.md"))
        translate_file(input_file_path, output_file_path)
        time.sleep(2)  # Attendre 2 secondes entre chaque fichier