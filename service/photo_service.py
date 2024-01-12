from firebase_admin import storage
from typing import List
import mimetypes
class PhotoService():
    def __init__(self):
        pass
    
    def upload_firebase(files):
        photos = []
        for file in files:
            bucket = storage.bucket()
            blob = bucket.blob(file.filename)
            mime_type, _ = mimetypes.guess_type(file.filename)
            # blob_name = f"{typePost}/{file.filename}"
            # blob = bucket.blob(blob_name)
            # Subir el archivo a Firebase Storage con el tipo MIME detectado
            blob.upload_from_file(file, content_type=mime_type)
            

            # Obtener la URL pública del archivo
            blob.make_public()
            url = blob.public_url
            photos.append(url)

        return photos

