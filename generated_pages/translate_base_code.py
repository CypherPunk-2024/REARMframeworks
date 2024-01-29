from googletrans import Translator
import re

def translate_file(input_file, output_file):
    translator = Translator()
    
    # Lecture du fichier d'entrée et traduction de l'ensemble du texte
    with open(input_file, 'r', encoding='utf-8') as f_input:
        original_text = f_input.read()
    
    # Traduction de l'ensemble du texte
    translated_text = translator.translate(original_text, dest='fr').text
    
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

# Utilisation du script
input_file = "/home/shell/Documents/SAM/REARMframeworks/generated_pages/techniques/T0001.md"  # Spécifiez le chemin de votre fichier d'entrée
output_file = "/home/shell/Documents/SAM/REARMframeworks/generated_pages/techniques/T0001.fr.md"  # Spécifiez le chemin du fichier de sortie

translate_file(input_file, output_file)