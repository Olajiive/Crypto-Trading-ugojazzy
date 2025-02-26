from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')



@dashboard.route('/dashboard')
def dashboard_home():
    return render_template('dashboard/index.html')


@dashboard.route('/base')
def base():
    return render_template('dashboard/base.html')


@dashboard.route('/transfers')
def transfers():
    return render_template('dashboard/exchange.html')

@dashboard.route('/wallets')
def wallet():
    return render_template('dashboard/wallet.html')

@dashboard.route('/profile')
def profile():
    return render_template('dashboard/profile-settings.html')

