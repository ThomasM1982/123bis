# 123 bis - Calculateur d'Impact Fiscal

Un outil complet pour calculer l'impact fiscal des revenus réputés distribués selon l'article 123 bis du Code général des impôts (CGI) français.

## 📋 Description

Ce projet automatise le calcul de l'impact fiscal des revenus 123 bis CGI sur l'impôt sur le revenu (IR) et les prélèvements sociaux (PS) des personnes physiques. Il prend en compte :

- Les barèmes d'imposition progressifs de 2016 à 2025
- La majoration de 25% éventuelle
- Le Prélèvement Forfaitaire Unique (PFU) ou l'imposition au barème
- La Contribution Exceptionnelle sur les Hauts Revenus (CEHR)
- Le plafonnement du quotient familial (PFQF)
- Les intérêts de retard et majorations

## 🚀 Fonctionnalités

### Calculs automatisés
- **Impôt sur le revenu** : Application du barème progressif avec décote
- **Prélèvements sociaux** : 15,5% (avant 2018) et 17,2% (à partir de 2018)
- **CEHR** : Contribution sur les hauts revenus selon les seuils
- **PFU** : Option d'imposition à taux forfaitaire de 12,8% + 17,2% PS
- **Quotient familial** : Plafonnement des avantages liés aux parts fiscales

### Comparaison "avec/sans 123 bis"
L'outil calcule automatiquement :
- La situation fiscale avec le revenu 123 bis
- La situation fiscale sans le revenu 123 bis
- L'impact différentiel (surcoût fiscal)

### Intérêts et pénalités
- Calcul des intérêts de retard (0,40%/mois avant 2018, 0,20%/mois après)
- Majorations pour défaut de déclaration (10%, 40%, 80%)
- Minorations possibles (30%, 50%) sur les intérêts

## 📊 Structure des données

Le fichier génère un Google Sheets avec les onglets suivants :

### Feuilles de paramétrage
- **`Notes`** : Mode d'emploi et explications détaillées
- **`Baremes_IR`** : Barèmes de l'impôt sur le revenu (2016-2025)
- **`Param_IR`** : Paramètres IR (décote, CEHR, plafond QF)
- **`Variables_a_renseigner`** : Données à saisir par l'utilisateur

### Feuilles de calcul
- **`IR_PersonnePhysique`** : Calculs détaillés IR et PS
- **`Calcul IS`** : Calculs d'impôt sur les sociétés (en développement)
- **`CHECK_FORMULES`** : Tests et vérifications

## 🛠️ Installation et utilisation

### Prérequis
- Google Colab ou environnement Python avec pandas
- Accès à Google Sheets API
- Librairies : `gspread`, `gspread_dataframe`, `google.auth`

### Exécution
1. Ouvrir le notebook dans Google Colab
2. Exécuter les cellules de code
3. S'authentifier avec Google (autorisation demandée)
4. Le Google Sheet est créé automatiquement

### Script Python
Une version scriptée est disponible dans `create_google_sheet.py` pour générer les feuilles et formules Google Sheets sans passer par le notebook.

### Saisie des données
Dans l'onglet `Variables_a_renseigner`, remplir pour chaque année :
- Parts fiscales
- Revenu net imposable déclaré
- Revenu réputé distribué (123 bis CGI)
- Options diverses (majoration 25%, PFU, etc.)

## 📖 Guide d'utilisation

### Paramètres principaux

| Paramètre | Description |
|-----------|-------------|
| **Parts fiscales** | Nombre de parts du foyer fiscal |
| **Revenu 123 bis** | Montant du revenu réputé distribué |
| **Majoration 25%** | Application de la majoration (VRAI/FAUX) |
| **Option PFU** | Choix du prélèvement forfaitaire unique |

### Calculs automatiques

Le système calcule automatiquement :
- La base imposable par part
- L'impôt brut selon le barème
- La décote éventuelle
- La CEHR si applicable
- Les prélèvements sociaux
- Le plafonnement du quotient familial

### Résultats
- **Impact IR net** : Surcoût d'impôt sur le revenu
- **Impact PS** : Surcoût de prélèvements sociaux
- **Total à payer** : Impact total incluant intérêts et majorations

## 🔧 Barèmes intégrés

### Barèmes IR 2024-2025
- **0%** : jusqu'à 11 704 € (2025)
- **11%** : de 11 704 € à 29 843 €
- **30%** : de 29 843 € à 85 332 €
- **41%** : de 85 332 € à 183 539 €
- **45%** : au-delà de 183 539 €

### Prélèvements sociaux
- **15,5%** pour les revenus perçus avant 2018
- **17,2%** pour les revenus perçus à partir de 2018

## ⚖️ Aspects juridiques

### Article 123 bis CGI
- Revenus réputés distribués par les sociétés soumises à l'IS
- Majoration de 25% en cas de non-désignation des bénéficiaires
- Régime mère-fille : seuls 5% des dividendes imposables si conditions remplies

### Jurisprudence et doctrine
Se référer au BOFiP et aux instructions fiscales en vigueur pour les cas particuliers.

## 🚨 Avertissements

- **Vérifier les cas particuliers** : régimes spécifiques, crédits d'impôt étrangers, conventions
- **Validation recommandée** : confronter les résultats avec un conseil fiscal
- **Mise à jour** : vérifier les barèmes et paramètres pour les années récentes

## 🔄 Versions et mises à jour

- **Version actuelle** : Barèmes mis à jour au 14/08/2025
- **Prochaines évolutions** : Finalisation du module IS, ajout de nouveaux cas d'usage

## 📞 Support

Ce projet est destiné à des fins pédagogiques et d'aide au calcul. Pour des situations complexes, consulter un expert-comptable ou avocat fiscaliste.

## 📝 Licence

Projet open source - Utilisation libre avec mention de la source.

---

*Dernière mise à jour : Août 2025*
