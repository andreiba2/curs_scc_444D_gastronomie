from flask import Blueprint
from curs_scc_444D_gastronomie.app.lib.biblioteca_gastronomie import ingrediente_bouyourdi, descriere_bouyourdi

bouyourdi_bp = Blueprint('bouyourdi', __name__)

@bouyourdi_bp.route('/gastronomie')
def tema():
    return "Pagina principala pentru tema Gastronomie"

@bouyourdi_bp.route('/gastronomie/bouyourdi')
def element():
    return "Pagina elementului Bouyourdi"

@bouyourdi_bp.route('/gastronomie/bouyourdi/ingrediente')
def ingrediente():
    return ingrediente_bouyourdi()

@bouyourdi_bp.route('/gastronomie/bouyourdi/descriere')
def descriere():
    return descriere_bouyourdi()