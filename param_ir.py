"""Constantes de paramètres IR.

Ce module centralise les taux des prélèvements sociaux (PS) et
les taux d'intérêts de retard applicables selon la période.
"""

# Taux de prélèvements sociaux par période
TAUX_PS = {
    "avant_2018": 0.155,
    "apres_2018": 0.172,
}

# Taux d'intérêts de retard par période
TAUX_INTERETS_RETARD = {
    "avant_2018": 0.004,
    "apres_2018": 0.002,
}
