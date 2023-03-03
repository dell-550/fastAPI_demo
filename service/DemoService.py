from sqlalchemy.orm import Session

from model import Demo
from dao import DemoDao


def insert_demo(db: Session, demo_info: DemoDao.DemoBase):
    new_demo = Demo.DemoModel(**demo_info.dict())
    db.add(new_demo)
    db.commit()
    db.refresh(new_demo)
    return new_demo
