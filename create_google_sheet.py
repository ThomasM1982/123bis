# Script unifié pour créer un Google Sheet natif avec toutes les feuilles et formules.

# Exécute ceci dans Colab. Il te demandera d'authentifier.



from google.colab import auth

import gspread

from gspread_dataframe import set_with_dataframe

import google.auth

import pandas as pd

import numpy as np # Import numpy



# Authentification

auth.authenticate_user()

credentials, project = google.auth.default()

gc = gspread.authorize(credentials)



# Création d'un nouveau Google Sheet

sheet_title = 'Tax_123_bis_CGI_ameliore_Unified_Formulas' # Using a new title for clarity

sh = gc.create(sheet_title)



# Function to get column letter from index (0-based)

def col_index_to_letter(col_index):

    letter = ''

    while col_index >= 0:

        letter = chr(col_index % 26 + ord('A')) + letter

        col_index = col_index // 26 - 1

    return letter



# Function to write a dataframe to a sheet and handle formulas

def write_df_to_gsheet_with_formulas(df, sheet_name, formula_columns=[]):

    # Check if DataFrame is empty

    if df.empty:

        print(f"DataFrame for sheet '{sheet_name}' is empty. Skipping.")

        return



    # Check if sheet already exists, if so, clear it before writing

    try:

        worksheet = sh.worksheet(sheet_name)

        worksheet.clear()

    except gspread.WorksheetNotFound:

        # Create worksheet with appropriate dimensions

        worksheet = sh.add_worksheet(title=sheet_name, rows=df.shape[0] + 1, cols=df.shape[1])



    # Write the dataframe data (including formula strings as text initially)

    set_with_dataframe(worksheet, df, include_index=False)



    # Update formula columns explicitly to be interpreted as formulas

    if formula_columns and not df.empty:

        # Get the column indices for formula columns

        formula_col_indices = [df.columns.get_loc(col) for col in formula_columns if col in df.columns]



        if formula_col_indices:

            # Prepare a list of lists with formula strings for updating

            # No need to get .values here, the data is already in df[formula_columns]

            formula_data = df[formula_columns].values.tolist()



            # Determine the range to update (e.g., 'A2:C11' for columns A, B, C and rows 2-11)

            start_row = 2 # Data starts from row 2 after header

            end_row = start_row + len(df) -1

            # Get the column letters for the formula columns by applying min/max to the indices list

            # Corrected: Use np.min and np.max on the list of indices

            start_col_letter = col_index_to_letter(np.min(formula_col_indices))

            end_col_letter = col_index_to_letter(np.max(formula_col_indices))



            range_to_update = f'{start_col_letter}{start_row}:{end_col_letter}{end_row}'



            # Update the cells with formulas, explicitly telling Sheets to interpret them

            worksheet.update(range_to_update, formula_data, value_input_option='USER_ENTERED')

            print(f"Updated formulas in sheet '{sheet_name}' for range '{range_to_update}'.")





# --- Create and Write Sheets ---



# Sheet: Notes

notes_data = {

    'Paramètre / Note': [

        'Mode d\'emploi', 'Régime mère-fille (MF)', 'Plafond 15 %', 'Tranche 75 000 € (2017)',

        'Tranche 500 000 € (2018-2020)', 'Taux 2019', 'Taux 2020 (≥ 250 M€ de CA)',

        'Taux 2021 (≥ 250 M€ de CA)', 'Taux 2022+', 'Contribution sociale 3,3 %',

        'Contributions exceptionnelles', 'Avertissement'

    ],

    'Détails': [

        'Saisir par année : Bénéfice avant ajustements, dividendes, CA, statut PME (si applicable), impôt étranger. Cochez VRAI/FAUX pour les options. Le fichier calcule l\'IS théorique et la condition des 60 %.',

        'Si MF=VRAI et conditions de l\'art.145 CGI remplies, seuls 5 % des dividendes sont imposables (E = B - C + 5 % de C).',

        '38 120 € jusqu’aux exercices ouverts en 2021 inclus ; 42 500 € à compter de 2022.',

        '2017 : pour les PME, la fraction de bénéfice après 15 % est imposée à 28 % dans la limite de 75 000 €, puis au taux normal (33 1/3 %).',

        '2018–2020 : 28 % jusqu\'à 500 000 € de bénéfice (après éventuel 15 %).',

        '2019 : 28 % jusqu\'à 500 k€, 31 % au-delà.',

        '2020 : CA < 250 M€ → 28 % sur tout ; CA ≥ 250 M€ → 28 % jusqu\'à 500 k€, 31 % au-delà.',

        '2021 : taux normal 26,5 % ; CA ≥ 250 M€ → 27,5 %.',

        'À compter de 2022 : taux normal unique 25 %.',

        'Appliquée si CA > 7,63 M€ et IS (L+N) > 763 k€ ; taux 3,3 % sur l\'excédent.',

        '2016 : surtaxe 10,7 % si CA ≥ 250 M€ ; 2017–2018 : contributions 15 % (CA > 1 Md€) et 30 % (CA ≥ 3 Md€) sur la fenêtre légale.',

        'Vérifier les cas particuliers (régimes spécifiques, crédits d\'impôt étrangers, conventions).'

    ]

}

df_notes = pd.DataFrame(notes_data)

write_df_to_gsheet_with_formulas(df_notes, 'Notes')



# Sheet: Baremes_IR (avec 2025 mis à jour au 14/08/2025, basé sur impots.gouv.fr - ajustés pour inflation ~1.8%)

baremes_data = {

    'Année': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],

    'Seuil1': [9710, 9807, 9964, 10064, 10084, 10225, 10777, 11294, 11497, 11704],

    'Taux1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    'Seuil2': [26818, 27086, 27519, 27794, 25710, 26070, 27478, 28797, 29315, 29843],

    'Taux2': [0.14, 0.14, 0.14, 0.14, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11],

    'Seuil3': [71898, 72617, 73779, 74517, 73516, 74545, 78570, 82341, 83823, 85332],

    'Taux3': [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],

    'Seuil4': [152260, 153783, 156244, 157806, 158122, 160336, 168994, 177106, 180294, 183539],

    'Taux4': [0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41, 0.41],

    'Seuil5': [1000000000] * 10,

    'Taux5': [0.45] * 10

}

df_baremes = pd.DataFrame(baremes_data)

write_df_to_gsheet_with_formulas(df_baremes, 'Baremes_IR')



# Sheet: Notes_IR (texte complet)

notes_ir_data = {

    'Paramètre / Note': ['Automatisation du barème', 'Source 2024 (seuils/taux)', 'Années 2016–2023', 'Quotient familial', 'Décote / CEHR', 'Personnalisation', 'Plafond du quotient familial', 'Paramétrage du PFQF', 'Réductions / Crédits', 'Majoration de 25 % (art. 158, 7-2° et 200 A, 1-A-1° CGI)', 'Option PFU (à compter de 2018)', 'Prélèvements sociaux sur revenus 123 bis', 'Taux historiques des prélèvements sociaux', 'Intérêts de retard – règles de calcul', 'Majoration (10% / 40% / 80%)', 'Correction assiette prélèvements sociaux', 'Réorganisation des colonnes par blocs logiques', 'Bloc Revenu', 'Bloc IR', 'Bloc Prélèvements sociaux', 'Bloc PFQF', 'Bloc Intérêts de retard', 'Bloc Majorations', 'Régularisation spontanée – droit à l\'erreur'],

    'Détails': [

        'Le calcul utilise la table \'Baremes_IR\' (5 tranches). L\'impôt est calculé par part puis multiplié par le nombre de parts.',

        '2024 est prérempli selon Service-Public (revenus 2024 imposés en 2025). Renseignez les autres années si nécessaire.',

        'Par prudence, les seuils/taux 2016–2023 ne sont pas pré-renseignés ici. Vous pouvez les coller depuis des sources officielles (BOFiP/Service-Public).',

        'Le revenu imposable total est divisé par les parts (colonne E) avant application du barème.',

        'La décote, réductions/crédits et CEHR ne sont pas intégrés par défaut. On peut les ajouter à la demande.',

        'Vous pouvez compléter la table \'Baremes_IR\' pour chaque année ; le calcul se mettra à jour automatiquement.',

        'Le modèle calcule l\'avantage lié aux parts au regard d\'une base (1 part célib., 2 parts marié) et applique le plafonnement via un montant par demi-part.',

        'Renseignez, dans Param_IR, \'QF_cap_par_demi_part (€)\' pour chaque année. Le plafond total = cap × nombre de demi-parts au-delà de la base.',

        'Saisissez vos réductions non restituables et crédits imputables/restituables : ils s\'imputent après décote, CEHR et PFQF.',

        'Conformément au 2° du 7 de l\'article 158 du CGI et au 1° du A du 1 de l\'article 200 A du CGI, ainsi qu\'aux II-B §120 et III §160 du BOI-RPPM-RCM-20-10-20-10, les revenus réputés distribués entrant dans ce champ sont majorés de 25 % pour le calcul de l\'assiette imposable. Case activable dans l\'onglet IR_PersonnePhysique.',

        'Si \'PFU\' est sélectionné (par défaut dès 2018), le revenu 123 bis (majoré le cas échéant) est exclu de la base du barème et imposé séparément à 12,8 % (IR). Le RFR reste calculé avec ce revenu ; la CEHR est donc appliquée sur le RFR global.',

        'Calculés à 17,2 % du revenu réputé distribué (majoré le cas échéant) pour toutes les années, qu\'il soit imposé au barème ou au PFU.',

        '15,5 % jusqu\'aux revenus perçus avant 2018, 17,2 % à compter des revenus 2018. La formule ajuste automatiquement selon l\'année (colonne Année). Les PS sont ajoutés dans l\'impact net final.',

        'Taux : 0,40 %/mois jusqu’au 31/12/2017 ; 0,20 %/mois à compter du 01/01/2018 (CGI art. 1727 ; BOI-CF-INF-10-10-20). Point de départ IR : 1er juillet de l’année N+1 (revenus N). Point d’arrêt : dernier jour du mois de la proposition de rectification ; la période entre proposition et mise en recouvrelement est neutralisée. L’assiette retenue ici est l’impact net (IR + PS).',

        'Sélectionnez le type de majoration (AUCUNE / 10 / 40 / 80) et l\'assiette (IR_SEUL ou IR+PS). Le montant est calculé sur la base de l\'impact supplémentaire dû au 123 bis. L\'impact total additionne l\'impact (IR+PS), les intérêts de retard et la majoration.',

        'Les prélèvements sociaux (15,5 % avant 2018, 17,2 % à partir de 2018) sont calculés sur le revenu brut réputé distribué, sans appliquer la majoration de 25 % réservée à l\'IR (barème ou PFU).',

        'L’onglet IR_PersonnePhysique a été réordonné pour suivre le flux : Revenu → IR → PS → PFQF → Intérêts → Majorations. Les formules ont été réécrites pour tenir compte du nouvel ordre (avec gestion des colonnes au-delà de Z).',

        'Variables d’entrée (revenu déclaré, revenu 123 bis, majoration 25 %, PFU/barème) puis base par part et RFR.',

        'Calcul du barème, impôt brut, décote, CEHR, PFU, réductions/crédits et impôt net. Les scénarios « avec » et « sans 123 bis » sont présentés avec l’impact.',

        'Assiette = revenu 123 bis **brut** (sans majoration 25 %) ; taux 15,5 % avant 2018 et 17,2 % à partir de 2018.',

        'Plafond par demi-part, parts de référence, avantage, réintégration, miroir sans 123 bis.',

        'Point de départ (1er juillet N+1), découpage avant/après 2018, assiette = impact net, calcul au taux légal (0,40 %/mois puis 0,20 %/mois).',

        'Options de majoration 10/40/80 %, assiette au choix (IR seul / IR+PS), et total final avec intérêts + majoration.',

        'Choisissez AUCUNE / 30 / 50 pour appliquer une minoration de 30 % ou 50 % sur les intérêts de retard (appliquée à la colonne \'Interets_de_retard_euros\'). L\'impact total utilise désormais les \'Intérêts après minoration\'.'

    ]

}

df_notes_ir = pd.DataFrame(notes_ir_data)

write_df_to_gsheet_with_formulas(df_notes_ir, 'Notes_IR')



# Sheet: Param_IR (avec 2025 mis à jour)

param_ir_data = {

    'Année': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],

    'Decote_A_celib': [1165, 1177, 1196, 1208, 779, 779, 833, 833, 889, 905],

    'Decote_B_celib': [0.75, 0.75, 0.75, 0.75, 0.4525, 0.4525, 0.4525, 0.4525, 0.4525, 0.4525],

    'Decote_plafond_celib': [1553, 1569, 1595, 1611, 1722, 1722, 1841, 1841, 1965, 2000],

    'Decote_A_couple': [1920, 1939, 1970, 1990, 1289, 1289, 1378, 1378, 1470, 1497],

    'Decote_B_couple': [0.75, 0.75, 0.75, 0.75, 0.4525, 0.4525, 0.4525, 0.4525, 0.4525, 0.4525],

    'Decote_plafond_couple': [2560, 2585, 2627, 2653, 2849, 2849, 3045, 3045, 3249, 3308],

    'CEHR_seuil1_celib': [250000] * 10,

    'CEHR_seuil2_celib': [500000] * 10,

    'CEHR_taux1': [0.03] * 10,

    'CEHR_taux2': [0.04] * 10,

    'CEHR_seuil1_couple': [500000] * 10,

    'CEHR_seuil2_couple': [1000000] * 10,

    'QF_cap_par_demi_part (€)': [1512, 1527, 1552, 1570, 1552, 1570, 1592, 1678, 1751, 1783]

}

df_param_ir = pd.DataFrame(param_ir_data)

write_df_to_gsheet_with_formulas(df_param_ir, 'Param_IR')



# Sheet: Calcul IS (with formulas as strings)

calcul_is_columns = ['Année', 'Bénéfice imposable avant ajustements (€)', 'Dividendes perçus (€)', 'Régime mère-fille applicable (VRAI/FAUX)', 'Bénéfice imposable ajusté (€)', 'Chiffre d\'affaires (CA) (€)', 'PME éligible taux 15 % (VRAI/FAUX)', 'Contribution sociale 3,3 % (VRAI/FAUX)', 'Contributions exceptionnelles (VRAI/FAUX)', 'Plafond 15 % (€)', 'Base à 15 % (€)', 'IS à 15 % (€)', 'Base restante après 15 % (€)', 'IS théorique hors contributions (€)', 'Contribution sociale 3,3 % (€)', 'Contributions exceptionnelles (€)', 'IS théorique total (€)', 'Impôt étranger payé (€)', 'Seuil 60 % de l\'IS théorique (€)', 'Ratio impôt étranger / IS théorique', 'Régime fiscal privilégié ? (< 60 %)']

df_calcul_is = pd.DataFrame(index=range(10), columns=calcul_is_columns)

df_calcul_is['Année'] = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]



# Define the mapping from column name to Google Sheets formula string for Calcul IS

calcul_is_formulas = {

    'Bénéfice imposable ajusté (€)': '=IFERROR(IF(D{row}, B{row}-C{row}+0.05*C{row}, B{row}),0)',

    'Plafond 15 % (€)': """=IFERROR(VLOOKUP(A{row}, Param_IS!$A:$B, 2, FALSE), "")""", # Assuming Param_IS sheet exists

    'Base à 15 % (€)': '=MIN(E{row}, J{row})',

    'IS à 15 % (€)': '=K{row}*0.15',

    'Base restante après 15 % (€)': '=E{row}-K{row}',

    'IS théorique hors contributions (€)': """=IFERROR(

        IF(A{row}=2016, M{row}*0.3333,

        IF(A{row}=2017, IF(G{row}, IF(M{row}<=75000, M{row}*0.28, 75000*0.28 + (M{row}-75000)*0.3333), M{row}*0.3333),

        IF(A{row}=2018, IF(M{row}<=500000, M{row}*0.28, 500000*0.28 + (M{row}-500000)*0.3333),

        IF(A{row}=2019, IF(M{row}<=500000, M{row}*0.28, 500000*0.28 + (M{row}-500000)*0.31),

        IF(A{row}=2020, IF(F{row}<250000000, M{row}*0.28, IF(M{row}<=500000, M{row}*0.28, 500000*0.28 + (M{row}-500000)*0.31)),

        IF(A{row}=2021, IF(F{row}<250000000, M{row}*0.265, M{row}*0.275),

        IF(A{row}>=2022, M{row}*0.25,

        M{row}*0 # Default or error case

    ))))))),0)""", # A=Année, M=Base restante après 15 %, G=PME éligible taux 15 %, F=Chiffre d'affaires (CA)

    'Contribution sociale 3,3 % (€)': """=IFERROR(IF(H{row}, IF(F{row}>7630000, MAX(0, N{row}-763000)*0.033, 0), 0),0)""", # H=Contribution sociale 3,3 % (VRAI/FAUX), F=Chiffre d'affaires (CA), N=IS théorique hors contributions

    'Contributions exceptionnelles (€)': """=IFERROR(

        IF(A{row}=2016, IF(F{row}>=250000000, N{row}*0.107, 0),

        IF(OR(A{row}=2017, A{row}=2018), IF(F{row}>=3000000000, N{row}*0.30, IF(F{row}>1000000000, N{row}*0.15, 0)),

        0

    )),0)""", # A=Année, F=Chiffre d'affaires (CA), N=IS théorique hors contributions

    'IS théorique total (€)': '=IFERROR(L{row} + N{row} + O{row} + P{row},0)',

    'Seuil 60 % de l\'IS théorique (€)': '=IFERROR(Q{row}*0.6,0)',

    'Ratio impôt étranger / IS théorique': '=IFERROR(R{row}/Q{row}, IFERROR(R{row}/0.000001, 0)),0)', # R=Impôt étranger payé, Q=IS théorique total - Added small number division for IFERROR on zero IS

    'Régime fiscal privilégié ? (< 60 %)': '=IFERROR(S{row}<0.6, FALSE),0)' # S=Ratio impôt étranger / IS théorique

}



# Function to generate the formula with correct row reference for Calcul IS

def get_calcul_is_formula(col_name, row_index):

    formula = calcul_is_formulas[col_name]

    sheet_row = row_index + 2 # Sheets are 1-indexed and have header

    return formula.replace('{row}', str(sheet_row))



# Generate formulas for each calculated column and year in df_calcul_is

calcul_is_calculated_columns = list(calcul_is_formulas.keys()) # Get columns with formulas



for col in calcul_is_calculated_columns:

    df_calcul_is[col] = [get_calcul_is_formula(col, i) for i in range(len(df_calcul_is))]



# Identify formula columns for explicit update

calcul_is_formula_columns_to_update = calcul_is_calculated_columns # All calculated columns have formulas



write_df_to_gsheet_with_formulas(df_calcul_is, 'Calcul IS', formula_columns=calcul_is_formula_columns_to_update)





# Sheet: Variables_a_renseigner

variables_data = {

    'Année': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],

    'Parts fiscales': [None] * 10,

    'Revenu net imposable déclaré (€)': [None] * 10,

    'Revenu réputé distribué (123 bis CGI) (€)': [None] * 10,

    'Majoration 25 % (VRAI/FAUX)': [False] * 10,

    'Option PFU (VRAI/FAUX)': [True] * 10, # PFU par défaut à partir de 2018

    'Impôt étranger (Crédit d\'impôt ou Imputation) (€)': [None] * 10,

    'Reductions d\'impot non restituables (€)': [None] * 10,

    'Credits d\'impot imputables / restituables (€)': [None] * 10,

    'CEHR applicable (VRAI/FAUX)': [True] * 10, # CEHR applicable par default si seuils dépassés

    'Type de majoration (AUCUNE/10/40/80)': ['AUCUNE'] * 10,

    'Assiette majoration (IR_SEUL/IR+PS)': ['IR+PS'] * 10,

    'Date de proposition de rectification (AAAA-MM-JJ)': [None] * 10,

    'Date de mise en recouvrement (AAAA-MM-JJ)': [None] * 10,

    'Minoration interets de retard (AUCUNE/30/50)': ['AUCUNE'] * 10

}

df_variables = pd.DataFrame(variables_data)

write_df_to_gsheet_with_formulas(df_variables, 'Variables_a_renseigner')



# Sheet: IR_PersonnePhysique (with formulas as strings)

ir_physique_columns = [

    'Année', 'Parts fiscales', 'Revenu net imposable déclaré (€)',

    'Revenu réputé distribué (123 bis CGI) (€)', 'Majoration 25 % (VRAI/FAUX)',

    'Option PFU (VRAI/FAUX)', 'Impôt étranger (Crédit d\'impôt ou Imputation) (€)',

    'Reductions d\'impot non restituables (€)', 'Credits d\'impot imputables / restituables (€)',

    'CEHR applicable (VRAI/FAUX)', 'Type de majoration (AUCUNE/10/40/80)',

    'Assiette majoration (IR_SEUL/IR+PS)', 'Date de proposition de rectification (AAAA-MM-JJ)',

    'Date de mise en recouvrerement (AAAA-MM-JJ)', 'Minoration interets de retard (AUCUNE/30/50)',

    # Bloc Revenu

    'Base par part avec 123 bis (€)', 'RFR avec 123 bis (€)',

    'Base par part sans 123 bis (€)', 'RFR sans 123 bis (€)',

    # Bloc IR (avec 123 bis)

    'Impôt brut barème avec 123 bis (€)', 'Montant décote avec 123 bis (€)',

    'Impôt après décote avec 123 bis (€)', 'CEHR avec 123 bis (€)',

    'Base PFU avec 123 bis (€)', 'IR PFU avec 123 bis (€)',

    'IR total avec 123 bis (€)', 'Reductions non restituables appliquées avec 123 bis (€)',

    'Credits imputables / restituables appliqués avec 123 bis (€)', 'IR net avec 123 bis (€)',

     # Bloc IR (sans 123 bis)

    'Impôt brut barème sans 123 bis (€)', 'Montant décote sans 123 bis (€)',

    'Impôt après décote sans 123 bis (€)', 'CEHR sans 123 bis (€)',

    'Base PFU sans 123 bis (€)', 'IR PFU sans 123 bis (€)',

    'IR total sans 123 bis (€)', 'Reductions non restituables appliquées sans 123 bis (€)',

    'Credits imputables / restituables appliqués sans 123 bis (€)', 'IR net sans 123 bis (€)',

    # Impact IR

    'Impact IR net (€)',

    # Bloc Prélèvements sociaux

    'Assiette PS avec 123 bis (€)', 'Taux PS', 'PS avec 123 bis (€)',

    'Assiette PS sans 123 bis (€)', 'PS sans 123 bis (€)',

    # Impact PS

    'Impact PS (€)',

    # Bloc PFQF (avec 123 bis)

    'Parts de référence avec 123 bis', 'Nombre de demi-parts au-delà base avec 123 bis',

    'Avantage max QF avec 123 bis (€)', 'Plafond QF avec 123 bis (€)',

    'Réintégration QF avec 123 bis (€)',

    # Bloc PFQF (sans 123 bis)

    'Parts de référence sans 123 bis', 'Nombre de demi-parts au-delà base sans 123 bis',

    'Avantage max QF sans 123 bis (€)', 'Plafond QF sans 123 bis (€)',

    'Réintégration QF sans 123 bis (€)',

    # Impact PFQF

    'Impact Réintégration QF (€)',

    # Bloc Intérêts de retard

    'Nb mois avant 01/01/2018', 'Nb mois après 01/01/2018',

    'Taux intérêt avant 01/01/2018', 'Taux intérêt après 01/01/2018',

    'Assiette intérêts (€)', 'Interets de retard bruts (€)',

    'Minoration interets de retard (%)', 'Interets après minoration (€)',

    # Bloc Majorations

    'Taux majoration', 'Assiette majoration (€)', 'Montant majoration (€)',

    # Impact total

    'Impact net (IR + PS) (€)', 'Total à payer (Impact net + Intérêts + Majoration) (€)'

]

df_ir_physique = pd.DataFrame(index=range(10), columns=ir_physique_columns)

df_ir_physique['Année'] = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]



# Define the mapping from column name to Google Sheets formula string for IR_PersonnePhysique

ir_physique_formulas = {

    # Bloc Revenu

    'Base par part avec 123 bis (€)': '=IFERROR((C{row}+D{row}*IF(E{row},1.25,1))/B{row},0)',

    'RFR avec 123 bis (€)': '=IFERROR(C{row}+D{row},0)',

    'Base par part sans 123 bis (€)': '=IFERROR(C{row}/B{row},0)',

    'RFR sans 123 bis (€)': '=IFERROR(C{row},0)',



    # Bloc IR (avec 123 bis)

    'Impôt brut barème avec 123 bis (€)': """=IFERROR(B{row}*(

        IF(Q{row}>'Baremes_IR'!E{bareme_row}, (Q{row}-'Baremes_IR'!E{bareme_row})*'Baremes_IR'!F{bareme_row}, 0) +

        IF(Q{row}>'Baremes_IR'!G{bareme_row}, (Q{row}-'Baremes_IR'!G{bareme_row})*'Baremes_IR'!H{bareme_row}, 0) +

        IF(Q{row}>'Baremes_IR'!I{bareme_row}, (Q{row}-'Baremes_IR'!I{bareme_row})*'Baremes_IR'!J{bareme_row}, 0) +

        IF(Q{row}>'Baremes_IR'!K{bareme_row}, (Q{row}-'Baremes_IR'!K{bareme_row})*'Baremes_IR'!L{bareme_row}, 0) +

        IF(Q{row}>'Baremes_IR'!C{bareme_row}, (Q{row}-'Baremes_IR'!C{bareme_row})*'Baremes_IR'!D{bareme_row}, 0)

    ),0)""",

    'Montant décote avec 123 bis (€)': """=IFERROR(IF(B{row}<=1.5,

        MAX(0, MIN('Param_IR'!C{param_row}-R{row}*'Param_IR'!D{param_row}, 'Param_IR'!E{param_row})),

        MAX(0, MIN('Param_IR'!F{param_row}-R{row}*'Param_IR'!G{param_row}, 'Param_IR'!H{param_row}))

    ),0)""",

    'Impôt après décote avec 123 bis (€)': '=IFERROR(MAX(0, R{row}-S{row}),0)',

    'CEHR avec 123 bis (€)': """=IFERROR(IF(L{row},

        IF(B{row}<2,

            IF(R{row}>='Param_IR'!I{param_row}, IF(R{row}>'Param_IR'!J{param_row}, (R{row}-'Param_IR'!J{param_row})*'Param_IR'!L{param_row} + ('Param_IR'!J{param_row}-'Param_IR'!I{param_row})*'Param_IR'!K{param_row}, (R{row}-'Param_IR'!I{param_row})*'Param_IR'!K{param_row}), 0),

            IF(R{row}>='Param_IR'!M{param_row}, IF(R{row}>'Param_IR'!N{param_row}, (R{row}-'Param_IR'!N{param_row})*'Param_IR'!L{param_row} + ('Param_IR'!N{param_row}-'Param_IR'!M{param_row})*'Param_IR'!K{param_row}, (R{row}-'Param_IR'!M{param_row})*'Param_IR'!K{param_row}), 0)

        ), 0

    ),0)""",

    'Base PFU avec 123 bis (€)': '=IFERROR(IF(F{row}, D{row}, 0),0)',

    'IR PFU avec 123 bis (€)': '=IFERROR(IF(F{row}, U{row}*0.128, 0),0)',

    'IR total avec 123 bis (€)': '=IFERROR(IF(F{row}, V{row} + T{row} + MAX(0,R{row}-S{row}-BG{row}), MAX(0,R{row}-S{row}-BG{row}) + T{row}),0)',



    'Reductions non restituables appliquées avec 123 bis (€)': '=IFERROR(MIN(X{row}, H{row}),0)',

    'Credits imputables / restituables appliqués avec 123 bis (€)': '=IFERROR(I{row},0)',

    'IR net avec 123 bis (€)': '=IFERROR(X{row}-Y{row}-Z{row},0)',



     # Bloc IR (sans 123 bis)

    'Impôt brut barème sans 123 bis (€)': """=IFERROR(B{row}*(

        IF(T{row}>'Baremes_IR'!E{bareme_row}, (T{row}-'Baremes_IR'!E{bareme_row})*'Baremes_IR'!F{bareme_row}, 0) +

        IF(T{row}>'Baremes_IR'!G{bareme_row}, (T{row}-'Baremes_IR'!G{bareme_row})*'Baremes_IR'!H{bareme_row}, 0) +

        IF(T{row}>'Baremes_IR'!I{bareme_row}, (T{row}-'Baremes_IR'!I{bareme_row})*'Baremes_IR'!J{bareme_row}, 0) +

        IF(T{row}>'Baremes_IR'!K{bareme_row}, (T{row}-'Baremes_IR'!K{bareme_row})*'Baremes_IR'!L{bareme_row}, 0) +

        IF(T{row}>'Baremes_IR'!C{bareme_row}, (T{row}-'Baremes_IR'!C{bareme_row})*'Baremes_IR'!D{bareme_row}, 0)

    ),0)""",

    'Montant décote sans 123 bis (€)': """=IFERROR(IF(B{row}<=1.5,

        MAX(0, MIN('Param_IR'!C{param_row}-AC{row}*'Param_IR'!D{param_row}, 'Param_IR'!E{param_row})),

        MAX(0, MIN('Param_IR'!F{param_row}-AC{row}*'Param_IR'!G{param_row}, 'Param_IR'!H{param_row}))

    ),0)""",

    'Impôt après décote sans 123 bis (€)': '=IFERROR(MAX(0, AC{row}-AD{row}),0)',

    'CEHR sans 123 bis (€)': """=IFERROR(IF(L{row},

        IF(B{row}<2,

            IF(U{row}>='Param_IR'!I{param_row}, IF(U{row}>'Param_IR'!J{param_row}, (U{row}-'Param_IR'!J{param_row})*'Param_IR'!L{param_row} + ('Param_IR'!J{param_row}-'Param_IR'!I{param_row})*'Param_IR'!K{param_row}, (U{row}-'Param_IR'!I{param_row})*'Param_IR'!K{param_row}), 0),

            IF(U{row}>='Param_IR'!M{param_row}, IF(U{row}>'Param_IR'!N{param_row}, (U{row}-'Param_IR'!N{param_row})*'Param_IR'!L{param_row} + ('Param_IR'!N{param_row}-'Param_IR'!M{param_row})*'Param_IR'!K{param_row}, (U{row}-'Param_IR'!M{param_row})*'Param_IR'!K{param_row}), 0)

        ), 0

    ),0)""",

    'Base PFU sans 123 bis (€)': '=0',

    'IR PFU sans 123 bis (€)': '=0',

    'IR total sans 123 bis (€)': '=IFERROR(MAX(0,AC{row}-AD{row}-BL{row}) + AF{row},0)',



    'Reductions non restituables appliquées sans 123 bis (€)': '=IFERROR(MIN(AH{row}, H{row}),0)',

    'Credits imputables / restituables appliqués sans 123 bis (€)': '=IFERROR(I{row},0)',

    'IR net sans 123 bis (€)': '=IFERROR(AH{row}-AI{row}-AJ{row},0)',



    # Impact IR

    'Impact IR net (€)': '=IFERROR(AA{row}-AK{row},0)',



    # Bloc Prélèvements sociaux

    'Assiette PS avec 123 bis (€)': '=IFERROR(D{row},0)',

    'Taux PS': '=IFERROR(IF(A{row}<2018, 0.155, 0.172),0)',

    'PS avec 123 bis (€)': '=IFERROR(AN{row}*AO{row},0)',

    'Assiette PS sans 123 bis (€)': '=0',

    'PS sans 123 bis (€)': '=0',



    # Impact PS

    'Impact PS (€)': '=IFERROR(AP{row}-AR{row},0)',



    # Bloc PFQF (avec 123 bis)

    'Parts de référence avec 123 bis': '=IFERROR(IF(B{row}<=1, 1, 2),0)',

    'Nombre de demi-parts au-delà base avec 123 bis': '=IFERROR(B{row}-AS{row},0)',

    'Avantage max QF avec 123 bis (€)': '=IFERROR(R{row}*(B{row}-1),0)',

    'Plafond QF avec 123 bis (€)': """=IFERROR(AT{row}*VLOOKUP(A{row}, 'Param_IR'!$A:$N, 14, FALSE),0)""",

    'Réintegration QF avec 123 bis (€)': '=IFERROR(MAX(0, AU{row}-AV{row}),0)',



    # Bloc PFQF (sans 123 bis)

    'Parts de référence sans 123 bis': '=IFERROR(IF(B{row}<=1, 1, 2),0)',

    'Nombre de demi-parts au-delà base sans 123 bis': '=IFERROR(B{row}-AX{row},0)',

    'Avantage max QF sans 123 bis (€)': '=IFERROR(AC{row}*(B{row}-1),0)',

    'Plafond QF sans 123 bis (€)': """=IFERROR(AY{row}*VLOOKUP(A{row}, 'Param_IR'!$A:$N, 14, FALSE),0)""",

    'Réintegration QF sans 123 bis (€)': '=IFERROR(MAX(0, AZ{row}-BA{row}),0)',



    # Impact PFQF

    'Impact Réintégration QF (€)': '=IFERROR(BG{row}-BL{row},0)',



    # Bloc Intérêts de retard

    'Nb mois avant 01/01/2018': '=IFERROR(IF(N{row}<>""; MAX(0; DATEDIF(DATE(A{row}+1; 7; 1); MIN(N{row}; DATE(2017;12;31)); "m") + IF(DAY(MIN(N{row}; DATE(2017;12;31)))>=1;1;0)); 0),0)',

    'Nb mois après 01/01/2018': '=IFERROR(IF(N{row}<>""; MAX(0; DATEDIF(MAX(DATE(A{row}+1; 7; 1); DATE(2018;1;1)); N{row}; "m") + IF(DAY(N{row})>=1;1;0)); 0),0)',

    'Taux intérêt avant 01/01/2018': '=0.004',

    'Taux intérêt après 01/01/2018': '=0.002',

    'Assiette intérêts (€)': '=IFERROR(BB{row}+BC{row},0)',

    'Interets de retard bruts (€)': '=IFERROR(BF{row} * (BH{row}*BJ{row} + BI{row}*BK{row}),0)',

    'Minoration interets de retard (%)': """=IFERROR(IF(P{row}="30", 0.3, IF(P{row}="50", 0.5, 0)),0)""",

    'Interets après minoration (€)': '=IFERROR(BH{row}*(1-BI{row}),0)',



    # Bloc Majorations

    'Taux majoration': """=IFERROR(IF(K{row}="10", 0.1, IF(K{row}="40", 0.4, IF(K{row}="80", 0.8, 0))),0)""",

    'Assiette majoration (€)': """=IFERROR(IF(L{row}="IR_SEUL", BB{row}, IF(L{row}="IR+PS", BB{row}+BC{row}, 0)),0)""",

    'Montant majoration (€)': '=IFERROR(BK{row}*BL{row},0)',



    # Impact total

    'Impact net (IR + PS) (€)': '=IFERROR(BB{row}+BC{row},0)',

    'Total à payer (Impact net + Intérêts + Majoration) (€)': '=IFERROR(BN{row}+BJ{row}+BM{row},0)'

}



# Function to generate the formula with correct row and bareme/param row references for IR_PersonnePhysique

def get_ir_physique_formula(col_name, row_index):

    formula = ir_physique_formulas[col_name]

    sheet_row = row_index + 2 # Sheets are 1-indexed and have header

    bareme_row_formula = f"MATCH(A{sheet_row},'Baremes_IR'!$A:$A,0)"

    param_row_formula = f"MATCH(A{sheet_row},'Param_IR'!$A:$A,0)"

    formula = formula.replace('{row}', str(sheet_row))

    formula = formula.replace('{bareme_row}', bareme_row_formula)

    formula = formula.replace('{param_row}', param_row_formula)

    return formula



# Generate formulas for each calculated column and year for IR_PersonnePhysique

ir_physique_calculated_columns = list(ir_physique_formulas.keys()) # Get columns with formulas

for col in ir_physique_calculated_columns:

    df_ir_physique[col] = [get_ir_physique_formula(col, i) for i in range(len(df_ir_physique))]



# Identify formula columns for explicit update

ir_physique_formula_columns_to_update = ir_physique_calculated_columns # All calculated columns have formulas



write_df_to_gsheet_with_formulas(df_ir_physique, 'IR_PersonnePhysique', formula_columns=ir_physique_formula_columns_to_update)



# Sheet: CHECK_FORMULES (Can be empty or with a few lines for tests)

check_formules_data = {

    'Test': ['Formule 1', 'Formule 2'],

    'Résultat Attendu': ['X', 'Y'],

    'Résultat Obtenu (formule)': ['=A2', '=B2'] # Example Sheets formulas

}

df_check_formules = pd.DataFrame(check_formules_data)

write_df_to_gsheet_with_formulas(df_check_formules, 'CHECK_FORMULES')





# Share (optionnel)

# sh.share('your.email@example.com', perm_type='user', role='writer')  # Replace with your email



print(f"Google Sheet created and ready: https://docs.google.com/spreadsheets/d/{sh.id}")

print("Open the link to edit online. Fill in variables in 'Variables_a_renseigner'.")
