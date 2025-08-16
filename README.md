# 123 bis - Calculateur d'Impact Fiscal (Version Corrigée et Améliorée)

Un outil complet et fonctionnel pour simuler l'impact fiscal des revenus réputés distribués selon l'article 123 bis du Code général des impôts (CGI) français.

## 📋 Description

Ce projet Python, conçu pour Google Colab, génère automatiquement une feuille de calcul Google Sheets qui modélise la logique complète de l'article 123 bis. Il permet de :

1.  **Analyser une société étrangère** pour déterminer si elle relève d'un régime fiscal privilégié.
2.  **Calculer l'impact** de ses revenus sur l'impôt sur le revenu (IR) et les prélèvements sociaux (PS) d'une personne physique en France.

L'outil est maintenant structuré de manière logique, avec une séparation claire entre les données d'entrée et les calculs.

## 🚀 Fonctionnalités Clés

- **Calcul de l'Impôt sur les Sociétés (IS) théorique** : Estime l'impôt qu'aurait payé la société étrangère en France pour déterminer si le régime est privilégié.
- **Calcul de l'Impôt sur le Revenu (IR)** : Simule l'impôt "sans" et "avec" l'intégration des revenus 123 bis, en se basant sur le résultat du calcul de l'IS.
- **Logique Connectée** : La feuille de calcul de l'IR est automatiquement liée à la feuille de calcul de l'IS, n'appliquant l'imposition que si le régime est effectivement jugé privilégié.
- **Paramètres à Jour** : Incorpore les barèmes et seuils fiscaux pertinents jusqu'à l'année 2025.

## 📊 Structure des Données

Le script génère une feuille Google Sheets avec une structure claire et logique :

### Feuilles d'Entrée (INPUT)
- **`INPUT_Personne_Physique`** : Saisissez ici les informations fiscales de la personne physique (revenus déclarés, parts fiscales, etc.).
- **`INPUT_Societe_Etrangere`** : Saisissez ici les données de la société étrangère (bénéfice, chiffre d'affaires, impôt payé, etc.).

### Feuilles de Paramètres (lecture seule)
- **`Baremes_IR`** : Barèmes de l'impôt sur le revenu (2016-2025).
- **`Param_IR`** : Paramètres de l'IR (décote, CEHR, etc.).
- **`Param_IS`** : Paramètres de l'IS (plafond du taux réduit).

### Feuilles de Calcul (automatisé)
- **`Calcul_IS`** : Détermine si le régime fiscal est privilégié en comparant l'impôt payé à l'IS théorique français.
- **`IR_PersonnePhysique`** : Calcule l'impact final sur l'impôt sur le revenu, en utilisant le résultat de la feuille `Calcul_IS`.

## 🛠️ Installation et Utilisation

### Prérequis
- Un compte Google pour utiliser Google Colab et Google Sheets.

### Exécution
1.  Ouvrir le notebook `123_bis.ipynb` dans Google Colab.
2.  Exécuter la **seule et unique cellule de code**.
3.  Suivre les instructions pour vous authentifier auprès de Google. Cela autorise le script à créer une feuille de calcul dans votre Google Drive.
4.  Une fois l'exécution terminée, un lien vers la nouvelle feuille Google Sheets (`Calculateur Fiscal 123bis (Final)`) sera affiché.

### Simulation
1.  Ouvrez la feuille de calcul via le lien fourni.
2.  Allez dans les onglets `INPUT_Personne_Physique` et `INPUT_Societe_Etrangere` pour y saisir vos propres données.
3.  Les résultats se mettront à jour automatiquement dans les feuilles `Calcul_IS` et `IR_PersonnePhysique`.

## ⚖️ Avertissements

- Cet outil est une aide au calcul et non un conseil fiscal. Les résultats sont des estimations.
- Pour des situations complexes, il est fortement recommandé de consulter un expert-comptable ou un avocat fiscaliste.

## 📝 Licence

Projet open source. Utilisation libre avec mention de la source.

---
*Dernière mise à jour du script : 2025*
