from . import db
from datetime import datetime


class agentname(db.Model):
    name_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(255), nullable=False)
    pollingunit_uniqueid = db.Column(db.Integer, nullable=False)


class announced_lga_results(db.Model):
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lga_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)


class announced_pu_results(db.Model):
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    polling_unit_uniqueid = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False,default='127.0.0.1')


class announced_state_results(db.Model):
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)


class announced_ward_results(db.Model):
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ward_name = db.Column(db.String(50), nullable=False)
    party_abbreviation = db.Column(db.String(4), nullable=False)
    party_score = db.Column(db.Integer, nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)


class lga(db.Model):
    uniqueid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lga_id = db.Column(db.Integer, nullable=False)
    lga_name = db.Column(db.String(50), nullable=False)
    state_id = db.Column(db.Integer, nullable=False)
    lga_description = db.Column(db.String(), nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)


class party(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    partyid = db.Column(db.String(11), nullable=False)
    partyname = db.Column(db.String(11), nullable=False)


class polling_unit(db.Model):
    uniqueid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    polling_unit_id = db.Column(db.Integer, nullable=False)
    ward_id = db.Column(db.Integer, nullable=False)
    lga_id = db.Column(db.Integer, nullable=False)
    uniquewardid = db.Column(db.Integer, nullable=False)
    polling_unit_number = db.Column(db.String(50), nullable=False)
    polling_unit_name = db.Column(db.String(50), nullable=False)
    polling_unit_description = db.Column(db.String(), nullable=False)
    lat = db.Column(db.String(255), nullable=True)
    long = db.Column(db.String(255), nullable=True)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)


class states(db.Model):
    state_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_name = db.Column(db.String(50), nullable=False)


class ward(db.Model):
    uniqueid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ward_id = db.Column(db.Integer, nullable=False)
    ward_name = db.Column(db.String(50), nullable=False)
    lga_id = db.Column(db.Integer, nullable=False)
    ward_description = db.Column(db.String(), nullable=False)
    entered_by_user = db.Column(db.String(50), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_ip_address = db.Column(db.String(50), nullable=False)
