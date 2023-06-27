import subprocess
import json

activity_id = input("ID Aktivitas: ")
token = input("KM Token: ")

curl_command = "curl --location --request GET 'https://api.kampusmerdeka.kemdikbud.go.id/studi/report/allweeks/{}' \
--header 'Accept: */*' \
--header 'Authorization: Bearer {}' \
--header 'Sec-Fetch-Site: same-site' \
--header 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
--header 'Accept-Encoding: gzip, deflate, br' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Host: api.kampusmerdeka.kemdikbud.go.id' \
--header 'Origin: https://kampusmerdeka.kemdikbud.go.id' \
--header 'Connection: keep-alive' \
--header 'Referer: https://kampusmerdeka.kemdikbud.go.id/' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Priority: u=3, i'".format(activity_id, token)

response = subprocess.run(curl_command, capture_output=True, text=True, shell=True)
response_json = json.loads(response.stdout)

# Write the JSON to a file
filename = "km-logbook-{}.json".format(activity_id)
with open(filename, 'w') as file:
    json.dump(response_json, file)

print("Response saved to {}".format(filename))