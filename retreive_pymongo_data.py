from pymongo import MongoClient
import datetime
import pandas as pd
class database:
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.users
        self.name=[]
        self.attendance=[]

        self.db2=self.client.timesheet
        self.userid=[]
        self.date=[]

    def create(self,name):
        self.db.pa.insert({"name":name, "attendance":0})

    def update(self,name):
        self.db.pa.update({"name":name},{"$inc":{"attendance":1}})

    def updateAttendance(self,userid):
        self.db2.date.insert({"userid":userid, "date": datetime.datetime.now()})

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
