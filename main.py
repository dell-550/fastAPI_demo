from fastapi import FastAPI
from controller.DemoController import demo
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(docs_url='/api/docs')
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount(path='/static', app=StaticFiles(directory='./static'), name='static')
app.include_router(demo, prefix='/api/demo', tags=['Demo'])

if __name__ == '__main__':
   uvicorn.run(app, port=8088)

