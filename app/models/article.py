"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""
from lin.exception import NotFound
from lin.interface import InfoCrud as Base
from sqlalchemy import Column, String, Integer, Text, BigInteger


class Article(Base):
    id = Column(BigInteger, primary_key=True, autoincrement=True, default=None)
    index = Column(BigInteger, default=None)
    prize = Column(Text)
    logo = Column(Text)
    img1 = Column(Text)
    img2 = Column(Text)
    img3 = Column(Text)
    img4 = Column(Text)
    img5 = Column(Text)
    title = Column(Text)
    province = Column(Text)
    college = Column(Text)
    brief_intro = Column(Text)
    intro = Column(Text)

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
