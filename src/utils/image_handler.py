from pathlib import Path
from flask import current_app
from uuid import uuid4

class ImageHandler:
    __image_path = "static/images/vacations"
    __no_image_path = "static/images/no_photo.jpg"
    
    # Save image:
    @staticmethod
    def save_image(image):
        if not image.filename: return None
        suffix = Path(image.filename).suffix
        image_name = str(uuid4()) + suffix
        image_path = Path(current_app.root_path) / ImageHandler.__image_path / image_name
        image.save(image_path)
        return image_name

    # Update image:
    @staticmethod
    def update_image(old_image_name, image):
        if not image.filename: return old_image_name
        image_name = ImageHandler.save_image(image)
        ImageHandler.delete_image(old_image_name)
        return image_name


    # Delete existing image: 
    @staticmethod
    def delete_image(image_name): 
        if not image_name: return None
        image_path = Path(current_app.root_path) / ImageHandler.__image_path / image_name
        image_path.unlink(missing_ok = True)


    # Return image absolute path from image name: 
    @staticmethod
    def get_image_path(image_name):
        image_path = Path(current_app.root_path) / ImageHandler.__image_path / image_name
        if not image_path.exists(): 
            image_path = Path(current_app.root_path) / ImageHandler.__no_image_path
        return image_path