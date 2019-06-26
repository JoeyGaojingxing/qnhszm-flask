from flask import jsonify
# from lin import route_meta, group_required, login_required
# from lin.exception import Success
from lin.redprint import Redprint
from lin.util import paginate

from app.models.article import Article

article_api = Redprint('article')


@article_api.route('/', methods=['GET'])
def get_all():
    start, count = paginate()
    res = Article.get_all(start, count)
    for val in res:
        try:
            val.logo = "https://qnhszm.obs.cn-north-1.myhuaweicloud.com/images/" + val.logo.split('/')[-1]
            val.img1 = "https://qnhszm.obs.cn-north-1.myhuaweicloud.com/images/" + val.img1.split('/')[-1]
            val.img2 = "https://qnhszm.obs.cn-north-1.myhuaweicloud.com/images/" + val.img2.split('/')[-1]
            val.img3 = "https://qnhszm.obs.cn-north-1.myhuaweicloud.com/images/" + val.img3.split('/')[-1]
            val.img4 = "https://qnhszm.obs.cn-north-1.myhuaweicloud.com/images/" + val.img4.split('/')[-1]
            val.img5 = "https://qnhszm.obs.cn-north-1.myhuaweicloud.com/images/" + val.img5.split('/')[-1]
        except:
            continue
    return jsonify(res)


@article_api.route('/<aid>', methods=['GET'])
def get_article(aid):
    res = Article.get_article(aid)
    return jsonify(res)
