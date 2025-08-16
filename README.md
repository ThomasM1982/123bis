# 123 bis - Calculateur d'Impact Fiscal

Un outil complet pour calculer l'impact fiscal des revenus réputés distribués selon l'article 123 bis du Code général des impôts (CGI) français.

## 📋 Description

Ce projet Python, conçu pour Google Colab, génère automatiquement une feuille de calcul Google Sheets pour simuler l'impact de l'article 123 bis du CGI sur l'impôt sur le revenu (IR) et les prélèvements sociaux (PS). Il intègre également un module pour le calcul de l'impôt sur les sociétés (IS).

L'outil prend en compte :
- Les barèmes d'imposition progressifs de 2016 à 2025.
- La majoration de 25% éventuelle.
- L'option pour le Prélèvement Forfaitaire Unique (PFU).
- La Contribution Exceptionnelle sur les Hauts Revenus (CEHR).
- Le plafonnement du quotient familial.

## 🚀 Fonctionnalités

- **Calcul de l'impôt sur le revenu (IR)** : Simulation détaillée avec et sans les revenus 123 bis.
- **Calcul de l'impôt sur les sociétés (IS)** : Module fonctionnel pour estimer l'IS théorique.
- **Comparaison "avec/sans"** : L'outil calcule automatiquement l'impact différentiel (surcoût fiscal) pour l'IR.
- **Paramètres à jour** : Incorpore les barèmes et seuils fiscaux jusqu'à l'année 2025.

## 📊 Structure des Données

Le script génère une feuille Google Sheets avec les onglets suivants :

### Feuilles de Paramétrage
- **`Baremes_IR`** : Barèmes de l'impôt sur le revenu (2016-2025).
- **`Param_IR`** : Paramètres de l'IR (décote, CEHR, plafond QF).
- **`Param_IS`** : Paramètres de l'IS (plafond du taux réduit).
- **`Variables_a_renseigner`** : **Feuille principale où l'utilisateur doit saisir ses données** pour chaque année (revenus, parts fiscales, options, etc.).

### Feuilles de Calcul
- **`IR_PersonnePhysique`** : Calculs détaillés de l'impact sur l'IR et les PS.
- **`Calcul_IS`** : Calculs détaillés de l'impôt sur les sociétés.

## 🛠️ Installation et Utilisation

### Prérequis
- Un compte Google pour utiliser Google Colab et Google Sheets.
- Les librairies Python nécessaires (`gspread`, `gspread_dataframe`, `pandas`) sont gérées par l'environnement Colab.

### Exécution
1. Ouvrir le notebook `123_bis.ipynb` dans Google Colab.
2. Exécuter la **seule et unique cellule de code**.
3. Suivre les instructions pour s'authentifier auprès de Google, ce qui autorise le script à créer une feuille de calcul dans votre Drive.
4. Une fois l'exécution terminée, un lien vers la nouvelle feuille Google Sheets sera affiché.

### Saisie des Données
1. Ouvrez le lien de la feuille de calcul générée.
2. Allez à l'onglet **`Variables_a_renseigner`**.
3. Remplissez les informations pour les années que vous souhaitez simuler.
4. Les résultats des calculs se mettront à jour automatiquement dans les feuilles `IR_PersonnePhysique` et `Calcul_IS`.

## ⚖️ Avertissements

- Cet outil est une aide au calcul et non un conseil fiscal. Les résultats sont des estimations.
- Pour des situations complexes, il est recommandé de consulter un expert-comptable ou un avocat fiscaliste.
- Assurez-vous que les barèmes sont à jour pour les années fiscales les plus récentes si vous utilisez cet outil au-delà de 2025.

## 📝 Licence

Projet open source. Utilisation libre avec mention de la source.

---
*Dernière mise à jour : 2025*
