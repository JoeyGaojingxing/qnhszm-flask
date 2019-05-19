"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""
from lin.exception import NotFound
from lin.interface import InfoCrud as Base
from sqlalchemy import Column, String, Integer, Text


class Article(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    prize = Column(String(15), nullable=False)
    logo = Column(String(255))
    pic = Column(String(1000))
    name = Column(String(255))
    province = Column(String(63))
    school = Column(String(255))
    intro = Column(String(512))
    introduce = Column(Text)

    @classmethod
    def get_all(cls):
        res = cls.query.all()
        if res is None:
            return NotFound(msg="没有项目")
        return res

    @classmethod
    def get_article(cls, aid):
        res = cls.query.filter_by(id=aid).one()
        if res is None:
            raise NotFound(msg="没有找到比赛")
        return res
