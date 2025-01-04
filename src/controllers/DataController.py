from .BaseController import BaseController
from fastapi import UploadFile


class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576
        
    
    def validate_uploaded_file(self , file: UploadFile):
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False ,'file type not suppurt'
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False,"file size exeeded"
        
        return True ,'success'
    