echo 'Pricelist Gen Starting ---------- '


echo '----------------- Generating DKK Pricelist ---------- '
python3 _pricelist_dkk_rec.py
echo '----------------- Successfully Generated DKK Pricelist ---------- '


echo '----------------- Generating NOK Pricelist ---------- '
python3 _pricelist_nok_rec.py
echo '----------------- Successfully Generated NOK Pricelist ---------- '


echo '----------------- Generating SEK Pricelist ---------- '
python3 _pricelist_sek_rec.py
echo '----------------- Successfully Generated SEK Pricelist ---------- '

echo '----------------- Generating SEK _pricelist_sek_kk-a.py ---------- '
python3 _pricelist_sek_kk-a.py
echo '----------------- Successfully Generated SEK _pricelist_sek_kk-a.py ---------- '

echo '----------------- Generating SEK _pricelist_sek_kk-b.py ---------- '
python3 _pricelist_sek_kk-b.py
echo '----------------- Successfully Generated _pricelist_sek_kk-b.py ---------- '


echo '----------------- Generating EUR Pricelist ---------- '
python3 _pricelist_eur_rec.py
echo '----------------- Successfully Generated EUR Pricelist ---------- '

echo '----------------- Generating _pricelist_eur_exworks ---------- '
python3 _pricelist_eur_exworks.py
echo '----------------- Successfully Generated _pricelist_eur_exworks ---------- '


echo '----------------- Generating _pricelist_eur_dap.py ---------- '
python3 _pricelist_eur_dap.py
echo '----------------- Successfully Generated _pricelist_eur_dap.py ---------- '


echo 'Pricelist Gen Ended ---------- '
