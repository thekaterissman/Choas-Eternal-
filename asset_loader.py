import trimesh
import pyglet
import os
from fbxloader import FBXLoader

class AssetLoader:
    def load_model(self, model_path):
        """
        Loads a 3D model using trimesh or fbxloader.
        """
        if not os.path.exists(model_path):
            print(f"Error: Model file not found at {model_path}")
            return None
        try:
            if model_path.lower().endswith('.fbx'):
                fbx = FBXLoader(model_path)
                model = fbx.export_trimesh()
            else:
                model = trimesh.load(model_path)
            print(f"Successfully loaded model: {model_path}")
            return model
        except Exception as e:
            print(f"Error loading model {model_path}: {e}")
            return None

    def load_sound(self, sound_path):
        """
        Loads a sound file using pyglet.
        """
        if not os.path.exists(sound_path):
            print(f"Error: Sound file not found at {sound_path}")
            return None
        try:
            sound = pyglet.media.load(sound_path)
            print(f"Successfully loaded sound: {sound_path}")
            return sound
        except Exception as e:
            print(f"Error loading sound {sound_path}: {e}")
            return None
