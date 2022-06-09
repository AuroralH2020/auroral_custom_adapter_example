from curses import has_key
from log import setup_custom_logger
from fastapi import FastAPI, HTTPException
from agent import getOidByAdapterId, getRegistration
from models import ErrorMessage
from dataSource import getDummyData
from config import config, Item

# Init logger
logger = setup_custom_logger('default')

app = FastAPI(    
    title="AUROAL Custom adapter example",
    description='Exposing example random data to AUROAL platform',
    # version="0.0.1",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    })

# On request
@app.get("/api/property/{oid}/{pid}", response_model=int, tags=["AuroralAgentAPI"], responses={404: {"model": ErrorMessage}})
async def getData(oid: str, pid: str) -> int:
    logger.info('Request:  OID: ' + oid + ' PID: ' + pid)
    if config.myItems[oid] is not None and pid in config.myItems[oid].pids:
        return getDummyData(oid, pid)
    else:
        raise HTTPException(status_code=404, detail="Device not found")

# On startup
@app.on_event("startup")
async def startup_event():
    global myOid, myPid
    # get OIDs and PIDs from Agent
    for a in config.adapterIds:
        oid = getOidByAdapterId(a)
        item = getRegistration(oid) if oid is not None else None
        pids = item.get('properties') if item is not None else None
        if pids is not None:
            logger.info('Listening on OID: ' + oid + ' PIDs: ' + str(pids))
            config.myItems[oid] = Item(oid, a, pids)