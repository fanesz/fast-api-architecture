# Fast API Architecture

Simple architecture without database implementation yet.

---

core package:
`pip install fastapi uvicorn pydantic[email]`

copas `example.env` to `.env`

command to run:
`python bin/main.py`

curl example:
```
curl -H "X-API-Key: llllllavacccccchicken" "http://127.0.0.1:5000/v1/playwright?brand_name=samsung"
```
output:
```
{"brand_name":"samsung","sentiments":["yeah","cool","anjass"]}
```