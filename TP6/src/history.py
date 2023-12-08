import pymongo

class History:
    def __init__(self):
        self.client = pymongo.MongoClient(f"mongodb://localhost:27017/")
        self.db = self.client["chat"]
        
    def createRoom(self, roomName: str):
        if not self.isRoomExist(roomName):                
            self.db[roomName].drop()
            self.db.create_collection(roomName)

    def insertMessage(self, roomName: str, message: dict) -> None:
        self.db[roomName].insert_one(message)

    def isRoomExist(self, roomName: str) -> bool:
        return roomName in self.db.list_collection_names()

    def getRoomMessages(self, roomName: str) -> list:
        return list(self.db[roomName].find())
    
    def getRooms(self) -> list:
        return self.db.list_collection_names()
    
    def close(self):
        self.client.close()

if __name__ == "__main__":
    history = History()
    history.createRoom("test")
    history.insertMessage("test", {"message": "test"})
    history.insertMessage("test", {"message": "test2"})
    print(history.getRoomMessages("test"))
    print(history.getRooms())
    history.close()