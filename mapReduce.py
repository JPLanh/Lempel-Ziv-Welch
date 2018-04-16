import hashlib
import json

class map:
  def __init__(self, nodes):
    self.Nodes = nodes
    self.maps = {}

  def mapping(self, toMap):
    hash_object = hashlib.md5(toMap)
    self.writeFile(toMap, hash_object.hexdigest())
    self.maps[len(self.maps)] = hash_object.hexdigest()
    f=open("./repository/metadata.txt", 'w')
    json.dump(self.maps, f)
    f.close()

  def writeFile(self, toMap, hashCode):
    f=open("./repository/"+hashCode, 'wb')
    f.write(toMap)
    f.close()
    
