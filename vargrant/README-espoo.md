# Espoon Linked eventsin asennus

Näillä ohjeilla saat Vagrant-virtuaalikoneeseen asennettua
Linked eventsin (6Aika-versio) sekä haettua siihen

* YSO-Keywordit
* Toimipisterekisteristä pääkaupunkiseudun Placet
* Espoon tapahtumat espoo.fi NC:n rajapinnasta

```
# Vagrant
sudo locale-gen "en_GB.UTF-8"

# Oiotaan vähän mutkia ja tehdään linkedevents ja vagrant PostgreSQL superuserit
sudo su - postgres -c "createuser -s linkedevents"
sudo su - postgres -c "createuser -s vagrant"

# Tietokannan alustus
createdb linkedevents
psql linkedevents -c "create extension hstore"
psql linkedevents -c "create extension postgis"

# Koodin kloonaus
git clone https://github.com/6aika/linkedevents.git linkedevents-espoo

# Virtualenvin luominen virtualenvwrapperin avulla
mkvirtualenv -p `which python3` le_espoo

# Python-pakettien asennus
cd linkedevents-espoo
pip install -r requirements.txt

# Tietokantataulujen luominen
python manage.py migrate

# Keywordsien tallennus
python manage.py event_import --keywords yso

# Paikkojen nouto toimipisterekisteristä 
# (näitä ei kai käytetä vielä espoo-importterissa, vaikka Espoon paikat löytyvätkin)
python manage.py event_import --places tprek

# Espoon tapahtumien nouto NC:stä
python manage.py event_import --events espoo
```
