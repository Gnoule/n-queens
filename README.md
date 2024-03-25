# Projet N-Reines avec Ajout de Reines Aléatoires

Ce projet implémente une solution au problème classique des N-Reines en utilisant une approche de backtracking, avec la possibilité d'ajouter un certain nombre de dames de manière aléatoire sur le plateau avant de trouver la solution. Le but est de placer N reines sur un échiquier de manière à ce qu'aucune reine ne puisse attaquer une autre.

## Fonctionnalités

- Génération d'un échiquier de taille variable avec un nombre prédéfini de colonnes.
- Possibilité de placer un nombre spécifié de dames de manière aléatoire sur le plateau initial.
- Algorithme de backtracking pour résoudre le problème des N-Reines.
- Affichage graphique des statistiques d'exécution, y compris le temps moyen d'exécution de la fonction principale.

## Exécution du Code

1. Assurez-vous d'avoir Python installé sur votre système.
2. Téléchargez ou clonez le dépôt.
3. Exécutez le fichier `n_queens.py`.
4. Suivez les instructions pour choisir le nombre de colonnes et le nombre de dames déjà présentes sur le plateau.

## Exemple d'utilisation

```python
python n_queens.py

Choisir le nombre de colonne du tableau: 8
Choisir le nombre de dame déja présente: 3

[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]

True
Solution trouvé :

[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]

