import hashlib
import json
import os

class map:
  def __init__(self, nodes):
    self.Nodes = nodes

  def mapping(self, toMap, finger):
    hash_object = hashlib.md5(toMap)
    self.writeFile(toMap, hash_object.hexdigest(), finger.guid)
    finger.maps[len(finger.maps)] = hash_object.hexdigest()
    JsonFormatter = {}
    JsonFormatter["Pages"] = finger.maps
    f=open("./repository/"+finger.guid+"/metadata.txt", 'w')
    json.dump(JsonFormatter, f)
    f.close()

  def writeFile(self, toMap, hashCode, guid):
    f=open("./repository/"+guid+"/"+hashCode, 'wb')
    f.write(toMap)
    f.close()
    
  def emit(self, finger):
    f=open("./repository/"+finger.guid+"/metadata.txt")
    jsonStuff = json.load(f)
    f.close()
    maps = jsonStuff["Pages"]
    i = len(maps)-1
    while i >= 0:
      if i%2 == 0:
        emitNode = finger.successor
      elif i%2 == 1:
        emitNode = finger.predecessor
      emitNode.maps[len(emitNode.maps)] = maps[str(i)]
      f=open("./repository/"+finger.guid+"/"+maps[str(i)], 'rb')
      data = f.read()
      f.close()
      self.writeFile(data, maps[str(i)], emitNode.guid) 
      os.remove("./repository/"+finger.guid+"/"+maps[str(i)])
      maps.pop(str(i))
      i-=1
    JsonFormatter = {}
    f=open("./repository/"+finger.guid+"/metadata.txt", 'w')
    json.dump(JsonFormatter, f)
