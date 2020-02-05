from pymongo import MongoClient
import pandas as pd
class database:
    def __init__(self):
        self.client=MongoClient()
        self.db1=self.client.users
        self.name=[]
        self.attendance=[]

        self.db2=self.client.attendance
        self.userid=[]
        self.date=[]

    def updateUser(self,name):
        self.db.pa.update_one({"name":name},{"$inc":{"attendance":1}})

    def updateAttendance(self,userid)
        self.db.timesheet.insertOne({"userid":abhi},"date": datetime.datetime.now())

    def clockOut(self,userid)

    def view(self):
        self.name=[]
        self.attendance=[]
        records=self.db.pa.find()
        j=0
        for i in records:
            j=j+1
            self.name.append(i["name"])
            self.attendance.append(i["attendance"])
        for i in range(j):
            print(self.name[i],self.attendance[i])
    def export_csv(self):
        self.view()
        data={"name":self.name,"attendance":self.attendance}
        df=pd.DataFrame(data,columns=["name","attendance"])
        df.to_csv("attendance.csv",index=True)
