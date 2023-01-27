# OHJELMA, JOKA KYSYY BMI-TIETOJA USEASTA KUNTOILIJASTA
# ======================================================

# KIRJASTOT JA MODUULIT
# ----------------------
# Tuodaan fitness.py:n sisältämät toiminnot tähän ohjelmaan

import fitness

# Kysutään tiedot ja tulostetaan painoindeksi kunnes halutaan lopettaa
while True:

pituus_teksti = input("Pituus (cm), tyhjä lopettaa: ")

# Tutkitaan onko syötetty pituudeksi tyhjä (pelkkä enter)
if pituus_teksti == '':
    break
paino_teksti = input("Paino: ")

pituus = float(pituus_teksti)
paino = float(paino_teksti)

bmi = fitness.laske_bmi(paino, pituus)

print('Painoindeksi on', bmi)
