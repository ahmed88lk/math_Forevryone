def generate_manim_code(concept):
    # This function generates Manim code based on the mathematical concept provided.
    # It is a placeholder for the actual implementation that would convert the concept
    # into a Manim script.

    manim_code = f"""
from manimlib import *

class {concept.replace(" ", "")}Scene(Scene):
    def construct(self):
        title = Text("{concept}").scale(2)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
    """
    return manim_code

def run_manim_code(manim_code):
    # This function executes the Manim code provided.
    # It assumes that the Manim command line interface is available in the environment.

    import subprocess
    import os

    # Save the Manim code to a temporary file
    with open("temp_manim_script.py", "w", encoding="utf-8") as f:
        f.write(manim_code)

    # Run the Manim command
    command = ["manim", "-pql", "temp_manim_script.py", "MyScene"]
    subprocess.run(command)

    # Clean up the temporary file
    os.remove("temp_manim_script.py")

def render_manim_video(manim_code):
    """
    Rend une vidéo à partir du code Manim fourni et retourne le chemin vers la vidéo générée.
    
    Args:
        manim_code (str): Le code Manim à exécuter
        
    Returns:
        str: Le chemin vers la vidéo générée ou None en cas d'erreur
    """
    import os
    import tempfile
    import re
    import subprocess
    
    # Extrait le nom de la classe Scene du code
    class_name_match = re.search(r'class\s+(\w+)\s*\(\s*Scene\s*\)', manim_code)
    if not class_name_match:
        print("Erreur: Impossible de trouver une classe Scene dans le code")
        return None
        
    class_name = class_name_match.group(1)
    
    # Crée un fichier temporaire pour le script Manim
    temp_dir = tempfile.gettempdir()
    script_path = os.path.join(temp_dir, "temp_manim_script.py")
    
    try:
        # Écrit le code dans un fichier temporaire
        with open(script_path, "w", encoding="utf-8") as f:
            f.write(manim_code)
        
        # Exécute manimgl pour générer la vidéo
        output_dir = os.path.join(os.getcwd(), "media", "videos")
        os.makedirs(output_dir, exist_ok=True)
        
        # Utilise manimgl au lieu de manim
        command = ["manimgl", script_path, class_name, "-o"]
        
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True
        )
        
        if result.returncode != 0:
            print(f"Erreur lors de l'exécution de Manim: {result.stderr}")
            return None
        
        # Recherche le chemin de la vidéo générée dans la sortie de Manim
        output_path = None
        media_dir = os.path.join(os.getcwd(), "media", "videos", script_path.split(os.path.sep)[-1].replace(".py", ""), class_name)
        
        if os.path.exists(media_dir):
            video_files = [f for f in os.listdir(media_dir) if f.endswith('.mp4')]
            if video_files:
                output_path = os.path.join(media_dir, sorted(video_files)[-1])
        
        return output_path
        
    except Exception as e:
        print(f"Erreur lors du rendu de la vidéo: {e}")
        return None
    finally:
        # Nettoyage
        if os.path.exists(script_path):
            os.remove(script_path)

def create_example_scene_py(filepath="example_scenes.py"):
    """
    Crée un fichier example_scenes.py avec une scène OpeningManimExample minimale pour manimgl.
    """
    code = '''from manimlib import *

class OpeningManimExample(Scene):
    def construct(self):
        text = Text("Hello, ManimGL!").scale(2)
        self.play(Write(text))
        self.wait(2)
    '''
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"Fichier exemple créé : {filepath}")

def generate_and_render_manim_video(concept, save_video=False):
    """
    Génère le code Manim pour un concept, le sauvegarde, lance manimgl pour afficher l'animation localement.
    
    Args:
        concept: Le concept mathématique à visualiser
        save_video: Si True, enregistre aussi la vidéo (avec -w), sinon juste affiche
    """
    import os
    import subprocess
    import tempfile
    from utils.gemini_utils import get_manim_code

    # Générer le code manim avec Gemini
    manim_code = get_manim_code(concept)
    
    # Extraire le nom de la classe Scene
    import re
    class_name_match = re.search(r'class\s+(\w+)\s*\(\s*Scene\s*\)', manim_code)
    if not class_name_match:
        print("Erreur: Impossible de trouver une classe Scene dans le code généré.")
        return None
    class_name = class_name_match.group(1)

    # Sauvegarder le code dans un fichier temporaire
    temp_dir = tempfile.gettempdir()
    script_path = os.path.join(temp_dir, "temp_manim_script.py")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(manim_code)

    # Lancer manimgl pour afficher l'animation (sans -w pour ne pas sauvegarder)
    # En mode standard, manimgl affiche juste l'animation dans une fenêtre
    command = ["manimgl", script_path, class_name]
    if save_video:
        command.append("-w")
    
    print("Exécution :", " ".join(command))
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Erreur lors de l'exécution de manimgl :", result.stderr)
        return None
    
    # En mode d'affichage uniquement, pas besoin de chercher un fichier vidéo
    if not save_video:
        return "Animation affichée"
    
    # Si on sauvegarde, chercher le fichier mp4 généré
    video_path = None
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".mp4") and class_name in file:
                video_path = os.path.join(root, file)
    
    if video_path:
        print("Vidéo générée :", video_path)
    else:
        print("Vidéo non trouvée.")
    
    return video_path