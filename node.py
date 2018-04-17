import hashlib
from base64 import b64encode
import os
class Node:
  def __init__(self, number):
    nodeName = "node"+str(number)
    hash_object = hashlib.md5(nodeName.encode('utf-8'))
    self.guid = hash_object.hexdigest()
    if not os.path.exists("./repository/"+self.guid):
      os.makedirs("./repository/"+self.guid)
    self.maps= {}
    
  def setKey(self, letter):
    self.key.append(letter)

  def joinRing(self, nodeSet):
    nodeSet[len(nodeSet)-2].predecessor = self    
    self.successor = nodeSet[len(nodeSet)-2]
    self.predecessor = nodeSet[0]
    nodeSet[0].successor = self
    
  def printInfo(self):
    print("Guid: %s" %self)
    print("Successor: %s" %self.successor)
    print("Predecessor: %s"  %self.predecessor)
