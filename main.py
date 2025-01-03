from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def we() -> dict[str , str]:
    return {"Message" : "Hello World"}