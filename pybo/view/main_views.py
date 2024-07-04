from flask import Blueprint, render_template, url_for
from pybo.models import Question
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    # question_list = Question.query.order_by(Question.create_date.desc())
    # return render_template('question/question_list.html', question_list=question_list)
    return redirect(url_for('question._list'))


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)   # 없는 페이지 요청받으면 404오류페이지(not 빈페이지) 표시
    return render_template('question/question_detail.html', question=question)
