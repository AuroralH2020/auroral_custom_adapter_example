import os
from dotenv import load_dotenv

load_dotenv()

class Item:
  def __init__(self, oid: str, agentId: str, pids: dict):
    self.oid = oid
    self.agentId = agentId
    self.pids = pids

class Config():
    agentUrl = os.environ.get("AGENT_URL") + ':' + os.environ.get("AGENT_PORT")
    adapterIds = os.environ.get("ADAPTER_IDS").split(',') if os.environ.get("ADAPTER_IDS") is not None else []
    myItems = {}
# Singleton class
config = Config()