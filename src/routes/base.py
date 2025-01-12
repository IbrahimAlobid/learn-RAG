from fastapi import FastAPI , APIRouter,Depends
import os
from helpers.config import get_settings ,Settings



base_router =APIRouter(
    prefix='/api/v1' ,
    tags=['api_v1']
)

@base_router.get("/")
async def we(app_setting :Settings = Depends(get_settings)):
    
    app_name = app_setting.APP_NAME
    app_version = app_setting.APP_VERSION
    
    
    return {
            "APP_NAME":app_name ,
            "APP_version": app_version
            }