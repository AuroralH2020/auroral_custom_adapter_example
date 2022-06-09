import requests
from config import config
import logging
logger = logging.getLogger('root')


# Retrieving OID from agent by adapter ID
def getOidByAdapterId(adapterId: str)-> str:
    try:
        response = requests.get(config.agentUrl +'/api/registration/oid/'+ adapterId)
        if(response.status_code == 200 and response.json()['message'] is not None):
            return response.json()['message']
        else:
            logger.error('Adapter not found for adapterId '+ adapterId)
            return None
    except Exception as e:
        logger.error('Error while getting oid for adapterId '+ adapterId + ' ('+ str(e) +')')
        return None

# Retrieving registration detail from agent by adapter oid
def getRegistration(oid: str)-> dict:
    try:
        response = requests.get(config.agentUrl +'/api/registration/'+ oid)
        if(response.status_code == 200 and response.json()['message'] is not None):
            return response.json()['message']
        else:
            logger.error('Registration not found for oid '+ oid)
            return None
    except Exception as e:
        logger.error('Error while getting registration for oid '+ oid + ' ('+ str(e) +')')
        return None
