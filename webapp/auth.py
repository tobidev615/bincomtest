from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import agentname, polling_unit, announced_pu_results, party, db

auth = Blueprint('auth', __name__)


@auth.route('/newresults', methods=['GET', 'POST'])
def create_new():
    if request.method == 'POST':
        # ID is auto increment so not required to add to fields
        # Date entered would also be automatic from the Date you generated data

        PollingUnitUniqueid = request.form.get('puid')
        PartyAbbreviation = request.form.get('partyab')
        PartyScore = request.form.get('partyscore')
        EnteredByUser = request.form.get('agentname')
        UserIpAddress = request.form.get('geotag')

        new_results = announced_pu_results(polling_unit_uniqueid=PollingUnitUniqueid, party_abbreviation=PartyAbbreviation, party_score=PartyScore, entered_by_user=EnteredByUser, user_ip_address=UserIpAddress)
        db.session.add(new_results)
        db.session.commit()
        flash('Account Created!', category='success')
        return redirect(url_for('auth.create_new'))
        # return redirect('/newresult')
        # The above would work the same
        # But we would always have to change it here
        # Instead of changing once at auth.py
    else:
        ag_table = db.session.execute(db.select(agentname)).scalars()
        pu_table = db.session.execute(db.select(polling_unit)).scalars()
        pa_table = db.session.execute(db.select(party)).scalars()
        return render_template("newresult.html", pu_table=pu_table, pa_table=pa_table, ag_table=ag_table)


@auth.route('/signout')
def logout():
    return "<p>Logout Text</p>"


@auth.route('/sign-up')
def signup():
    return "<p>SingUp Text</p>"
