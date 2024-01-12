from flask import Blueprint
from flask_restful import Resource, reqparse, request,Api
from service.photo_service import PhotoService

photo_controller_bp = Blueprint('photo', __name__)
api = Api(photo_controller_bp)

@photo_controller_bp.route('/photo/upload_photo', methods=['POST'])
def uploadPhoto():
    if 'file[]' not in request.files:
        return {
            'status': False,
            'message': 'error'
        },404
    files = request.files.getlist('file[]')
    urls = PhotoService.upload_firebase(files)
    return {
            'status': True,
            'content': urls,
        }, 201