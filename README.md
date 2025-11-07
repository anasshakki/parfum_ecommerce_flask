# Site E-commerce de Parfums

Ce projet est la démonstration d'une **application web full-stack minimaliste** conçue pour simuler l'expérience utilisateur d'une boutique en ligne de produits de luxe. Développé avec le micro-framework Python **Flask**, ce site met l'accent sur la clarté de l'architecture et la fonctionnalité d'achat essentielle.

---

## Caractéristiques et Fonctionnalités

* **Catalogue Dynamique :** Affiche un catalogue de produits défini directement dans la logique Python.
* **Gestion du Panier :** Implémentation d'une logique de session (via une variable Python) pour suivre les articles sélectionnés et calculer le prix total de la commande.
* **Simulation de Paiement :** Intégration d'une page de "passage à la caisse" pour simuler la collecte des informations de livraison et de paiement.
* **Design Professionnel :** Utilisation d'un thème sombre (gris anthracite/noir) et de CSS personnalisé pour créer une ambiance de luxe et de sobriété.

---

## Architecture Technique

| Catégorie | Outils | Rôle dans le Projet |
| :--- | :--- | :--- |
| **Backend/Logique** | **Python 3** | Langage principal de l'application. |
| **Framework** | **Flask** | Micro-framework utilisé pour la gestion des routes et des requêtes HTTP. |
| **Frontend/Vues** | **HTML5/Jinja2** | Structure des pages et rendu dynamique des données dans les templates. |
| **Stylisme** | **CSS3** | Mise en forme moderne et responsive, et application du thème sombre. |

### Structure Modulaire

Le projet suit une structure Flask modulaire propre :
* `app.py` : Point d'entrée de l'application.
* `routes.py` : Définit toutes les URL et contient les données du catalogue.
* `templates/` : Contient toutes les vues HTML (base, index, panier, checkout).
* `static/` : Contient les fichiers CSS et les images.

---

## Installation et Lancement Local

Pour exécuter cette application en local :

```bash
# 1. Cloner le dépôt (si vous utilisez Git)
git clone [https://github.com/anasshakki/parfum_ecommerce_flask.git](https://github.com/anasshakki/parfum_ecommerce_flask.git)
cd parfum_ecommerce_flask

# 2. Installer les dépendances (Flask)
pip install Flask

# 3. Lancer l'application Flask
python app.py

# 4. Accéder au site
# Ouvrez votre navigateur à l'adresse [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
