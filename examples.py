from snipeitpythonapi import Assets

server = 'http://snipeitserver.example.com'
token = 'mysnipeittoken'

snipeit_assets = Assets()
payload = '{"asset_tag":"thisisunique17", "status_id":1, "model_id": 5}'
response = snipeit_assets.create(server, token, payload)