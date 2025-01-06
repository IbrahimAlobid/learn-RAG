from pydantic import BaseModel
from typing import Optional
from langchain_community.document_loaders import PyPDFLoader


class ProcessRequest(BaseModel):
    file_id : str
    chunk_size :Optional[int]=100
    overlap_size :Optional[int]=20
    do_reset :Optional[int]=0
    