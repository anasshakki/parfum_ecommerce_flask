# Mini Blog – Application Web Full-Stack (Node.js/Express)

Ce projet est une application web de blog complète conçue pour la gestion et la publication d'articles. Développé en **Node.js** avec le framework **Express**, il intègre une base de données relationnelle et des fonctionnalités d'authentification sécurisée.

Le but de ce projet était de construire une application full-stack démontrant une architecture Backend claire et la maîtrise de l'authentification web moderne.

---

## ⚙️ Technologies Utilisées

| Catégorie | Outils | Rôle dans le Projet |
| :--- | :--- | :--- |
| **Backend/Serveur** | **Node.js & Express** | Création du serveur, gestion des routes API et logique applicative. |
| **Base de Données** | **SQLite** | Base de données légère, rapide et intégrée pour le stockage des utilisateurs et des articles. |
| **Authentification** | **bcryptjs** | Hachage sécurisé des mots de passe utilisateurs. |
| **Sessions** | **express-session** | Gestion de l'état utilisateur (connexion, déconnexion). |
| **Frontend/Vues** | **EJS (Embedded JavaScript)** | Moteur de templating pour le rendu des pages côté serveur. |

---

## Fonctionnalités Principales

* **Authentification Complète :** Système sécurisé d'inscription, connexion, et déconnexion.
* **Gestion des Articles (CRUD) :** Permet aux utilisateurs connectés de créer, éditer, et supprimer leurs propres articles de blog.
* **Protection des Routes :** Les pages de création/édition d'articles sont protégées et accessibles uniquement aux utilisateurs authentifiés.
* **Interface Utilisateur :** Design épuré, moderne et responsive, avec une confirmation JavaScript côté client avant la suppression d'un article.
* **Persistence de Session :** Utilisation de sessions pour maintenir l'utilisateur connecté de manière sécurisée.

---

## Installation et Lancement

Pour lancer l'application en local :

```bash
# 1. Cloner le dépôt
git clone [https://github.com/anasshakki/MiniBlog-NodeJS.git](https://github.com/anasshakki/MiniBlog-NodeJS.git)
cd MiniBlog-NodeJS

# 2. Installer les dépendances Node.js
npm install

# 3. Lancer l'application
node server.js 

# 4. Ouvrir dans le navigateur
# Le site sera accessible à http://localhost:3000 (ou autre port configuré)
