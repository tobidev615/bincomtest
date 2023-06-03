from flask import Blueprint, redirect, url_for, request, render_template
from .models import lga, polling_unit, announced_pu_results, db

views = Blueprint('views', __name__)


@views.route('/')
def home():
    # putable = polling_unit.query.all()
    putable = db.session.execute(db.select(polling_unit)).scalars()
    lgatable = db.session.execute(db.select(lga)).scalars()
    return render_template("home.html", polling_id=putable, lga_id_response=lgatable)


@views.route('/puresults', methods=['GET', 'POST'])
def resultchecker():
    if request.method == 'POST':
        puid = request.form.get('puid')
        print(puid)
        queried_result = db.session.execute(
            db.select(announced_pu_results).filter_by(polling_unit_uniqueid=puid)).scalars()
        # queried_result = announced_pu_results.query.filter_by(polling_unit_uniqueid=puid).all()
        puinfo = db.session.execute(db.select(polling_unit).filter_by(uniqueid=puid)).scalar_one()
        return render_template("results.html", allresults=queried_result, puinfo=puinfo)
    else:
        return '<p>Not Found</p>'
        # puresults = announced_pu_results.query.all()
        # return render_template("results.html", allresults=puresults)


@views.route('/lgaresults', methods=['GET', 'POST'])
def lgaresult():
    if request.method == 'POST':
        lgaid = request.form.get('lgaid')
        print(lgaid)
        lgatable = db.session.execute(db.select(lga).filter_by(uniqueid=lgaid)).scalar_one()
        print(lgatable)
        p_unit = db.session.execute(db.select(polling_unit).filter_by(lga_id=lgaid)).scalars()
        print(p_unit)
        queried_result = db.session.execute(db.select(announced_pu_results)).scalars()
        print(queried_result)

        return render_template("lgaresults.html", p_unit=p_unit, lgatable=lgatable)
    else:
        return '<p> Try Again boy ! </p>'


@views.route('/queryall')
def checkall():
    queried_result = db.session.execute(
        db.select(announced_pu_results)).scalars()
    return render_template("queryall.html", allresults=queried_result)
