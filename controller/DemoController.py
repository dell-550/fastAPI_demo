from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from dao import DemoDao
from service import DemoService
from dependency import get_db

demo = APIRouter()


@demo.post('/post', response_model=DemoDao.DemoBase, summary='这是一个demo')
async def insert_demo(demo_info: DemoDao.DemoBase, db: Session = Depends(get_db)):
    return DemoService.insert_demo(db, demo_info=demo_info)
