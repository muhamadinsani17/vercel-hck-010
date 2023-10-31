from fastapi import FastAPI, HTTPException, Header
from email import message

app = FastAPI()

#key perlu dimasukkan kedalam header
key = "hacktiv8mania2023"

#public
@app.get('/')
def helloFunction():
    return  {
        "message" : "hellow world"
    }

#secret -> harus memasukkan authentication
@app.get('/secret')
def helloFunction(api_key: str = Header (None)):
    if api_key is None or api_key != key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return  {
        "message" : "secret message"
    }