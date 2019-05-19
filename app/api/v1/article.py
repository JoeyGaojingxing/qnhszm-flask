from flask import jsonify
# from lin import route_meta, group_required, login_required
# from lin.exception import Success
from lin.redprint import Redprint

from app.models.article import Article

article_api = Redprint('article')


@article_api.route('/', methods=['GET'])
def get_all():
    res = Article.get_all()
    return jsonify(res)


@article_api.route('/<aid>', methods=['GET'])
def get_article(aid):
    res = Article.get_article(aid)
    return jsonify(res)
