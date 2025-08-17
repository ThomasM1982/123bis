from constants import PS_RATE_BEFORE_2018, PS_RATE_AFTER_2018

IR_PHYSIQUE_FORMULAS = {

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

    'Taux PS': f'=IFERROR(IF(A{{row}}<2018, {PS_RATE_BEFORE_2018}, {PS_RATE_AFTER_2018}),0)',

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

    formula = IR_PHYSIQUE_FORMULAS[col_name]

    sheet_row = row_index + 2 # Sheets are 1-indexed and have header

    bareme_row_formula = f"MATCH(A{sheet_row},'Baremes_IR'!$A:$A,0)"

    param_row_formula = f"MATCH(A{sheet_row},'Param_IR'!$A:$A,0)"

    formula = formula.replace('{row}', str(sheet_row))

    formula = formula.replace('{bareme_row}', bareme_row_formula)

    formula = formula.replace('{param_row}', param_row_formula)

    return formula

IR_PHYSIQUE_CALCULATED_COLUMNS = list(IR_PHYSIQUE_FORMULAS.keys())
