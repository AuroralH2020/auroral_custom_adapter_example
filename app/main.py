
import string
from fastapi import FastAPI, HTTPException
from models import ErrorMessage
from dataSource import getDummyData
import requests
import log as log

# Variables
agentUrl = 'http://localhost:81'
adapterId = 'testDevice'
myPid = 'temp'
myOid = None

# Initialize logger
logger = log.setup_custom_logger('root')

app = FastAPI(    
    title="AUROAL Custom adapter example",
    description='Exposing example random data to AUROAL platform',
    # version="0.0.1",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    })

@app.get("/api/property/{oid}/{pid}", response_model=int, tags=["AuroralAgentAPI"], responses={404: {"model": ErrorMessage}})
async def getData(oid: str, pid: str) -> int:
    logger.info('Request:  OID: ' + oid + ' PID: ' + pid)
    if oid == myOid and pid == myPid:
        return getDummyData(oid, pid)
    else:
        raise HTTPException(status_code=404, detail="Device not found")

@app.on_event("startup")
async def startup_event():
    global myOid, myPid
    response = requests.get(agentUrl +'/api/registration/oid/'+ adapterId)
    if(response.status_code == 200 and response.json()['message'] != None):
        myOid = response.json()['message']
        logger.info('Adapter listening to OID: ' + myOid + ' PID: ' + myPid)
    else:
        logger.error('Error: Object with adapterId'+ adapterId +' does not exists')
    
