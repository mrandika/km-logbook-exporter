# Kampus Merdeka Logbook Exporter
Ever tired copying all logbook data from KM portal to your laporan akhir? Use this.

## Getting the logbook data
1. Login to the Kampus Merdeka Portal
2. Select the "Kegiatanku", then "Kegiatan Aktif"
3. Select the activity for which logbook you'd like to export
4. The URL should be `https://kampusmerdeka.kemdikbud.go.id/activity/active/<ACTIVITY_ID>`
5. Note the ACTIVITY_ID
6. Run the following script in dev console to get your KM bearer token:
```
const userLocalKey = `@mkbm/manager/user`;
const storageData = localStorage.getItem(userLocalKey);
const storageDataParsed = JSON.parse(storageData);
const token = storageDataParsed?.value?.token;

console.log(token)
```
7. Note the output, this will be your KM Token
8. Run the following script: [Logbook Downloader](https://github.com/mrandika/km-logbook-exporter/raw/main/logbook-downloader.py), input the ACTIVITY_ID and BEARER_TOKEN from previous step

... or you can use Postman to import the cURL:
```
curl --location --request GET 'https://api.kampusmerdeka.kemdikbud.go.id/studi/report/allweeks/{ACTIVITY_ID}' \
--header 'Accept: */*' \
--header 'Authorization: Bearer {BEARER_TOKEN}' \
--header 'Sec-Fetch-Site: same-site' \
--header 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
--header 'Accept-Encoding: gzip, deflate, br' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Host: api.kampusmerdeka.kemdikbud.go.id' \
--header 'Origin: https://kampusmerdeka.kemdikbud.go.id' \
--header 'Connection: keep-alive' \
--header 'Referer: https://kampusmerdeka.kemdikbud.go.id/' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Priority: u=3, i
```
9. The file from step 8 should be in your home folder (~/km-logbook-<ACTIVITY_ID>.json)

## Exporting to XLSX
0. Please note your logbook json file path. The following script assumes the json file and the script are in same level.
   ```
   - km-logbook-12345678.json
   - logbook-exporter.py
   ```
1. Run the following script: [Logbook Exporter](https://github.com/mrandika/km-logbook-exporter/raw/main/logbook-exporter.py), input the ACTIVITY_ID
2. The file from step 1 should be in your home folder (~/km-logbook-<ACTIVITY_ID>.xlsx)
