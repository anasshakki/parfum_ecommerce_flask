# Fichier : app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Le catalogue des parfums
parfums = [
    {'id': 1, 'nom': 'Rose Éternelle', 'prix': 79.99, 'image': 'parfum1.jpg'},
    {'id': 2, 'nom': 'Bois Mystique', 'prix': 89.50, 'image': 'parfum2.jpg'},
    {'id': 3, 'nom': 'Agrumes Frais', 'prix': 59.90, 'image': 'parfum3.jpg'},
]

# Le panier (liste simple)
panier = []

@app.context_processor
def inject_panier_count():
    return dict(panier_count=len(panier))

@app.route('/')
def index():
    return render_template('index.html', parfums=parfums)

@app.route('/ajouter_au_panier/<int:parfum_id>', methods=['POST'])
def ajouter_au_panier(parfum_id):
    parfum_selectionne = next((p for p in parfums if p['id'] == parfum_id), None)
    if parfum_selectionne:
        panier.append(parfum_selectionne)
    
    return redirect(url_for('index'))

@app.route('/panier')
def voir_panier():
    prix_total = sum(p['prix'] for p in panier)
    return render_template('panier.html', panier=panier, total=prix_total)

@app.route('/payer')
def payer():
    """Affiche la page de paiement simplifiée."""
    if not panier:
        return redirect(url_for('index')) # Redirige si le panier est vide

    prix_total = sum(p['prix'] for p in panier)
    return render_template('checkout.html', total=prix_total) # Renvoyer un nouveau template !

if __name__ == '__main__':
    app.run(debug=True)