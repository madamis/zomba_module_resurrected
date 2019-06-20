"""this will be handling database objects.
basically, the classes are clearly defined here
and access to database is through this"""
import psycopg2 as psycopg2


connection = psycopg2.connect(user='postgres', password='12345678', host='localhost', port='5432',
                                  database='zomba_malawi')
    # def available_plot_numbers(self):
    #     connection = self.connection()
    #     cursor = connection.cursor()
    #     query = """SELECT plot_no, plot_name FROM plot"""
    #     cursor.execute(query)
    #     for i in cursor:
    #         print(i[1])
    #         self.matabu.plot_combo.addItem(str(i[0])+"      "+i[1])

class Owner:
    def __init__(self):
        self.__id__ = 0
        self.__firstname__ = ''
        self.__lastname__ = ''
        self.__plotnumber__ = ''
        self.__amount__ = 0.0

    def setid(self, id):
        self.__id__ = id
    def getid(self):
        return self.__id__
    def setfirstname(self, firstname):
        self.__firstname__ = firstname
    def getfirstname(self):
        return self.selectattribute('firstname')
    def setlastname(self, lastname):
        self.__lastname__ = lastname
    def getlastname(self):
        return self.selectattribute('lastname')
    def setplotnumber(self, plotnumber):
        self.__plotnumber__ = plotnumber
    def getplonumber(self):
        return self.__plotnumber__
    def createowner(self):
        stingquery = """insert into finale_owner(firstname, lastname) values('"""+self.__firstname__+"""', '"""+self.__lastname__+"""'); """
    def deleteowner(self,id):
        stringquery = """delete from owner where id = '"""+id+"""';"""
    def updateowner(self,id):
        stringquery = """udate owner set col1"""
    def selectattribute(self, attribute):
        "select "+attribute+" from finale_owner where id = "+str(self.getid())



class Location:
    def __init__(self):
        self.__id__ = 0
        self.__TAname__ = ''
        self.__TAcode__ = ''
        self.__villagename__ = ''
        self.__villagecode__ = ''

    def setid(self, id):
        self.__id__ = id
    def getid(self):
        return self.__id__
    
    def setvillagecode(self, villagecode):
        self.__villagecode__ = villagecode
    def getvillagecode(self):
        return self.__villagecode__
    
    def setvillagename(self, villagename):
        self.__villagename__ = villagename
    def getvillagename(self):
        return self.__villagename__
        
    def setTAcode(self, TAcode):
        self.__TAcode__ = TAcode
    def getTAcode(self):
        return self.__TAcode__
    
    def setTAname(self, TAname):
        self.__TAname__ = TAname
    def getTAname(self):
        return self.__TAname__
    def createlocation(self):
        stingquery = """insert into location """
    def deletelocation(self,id):
        stringquery = """delete from location where id = '"""+id+"""';"""
    def updatelocation(self,id):
        stringqiery = """udate location set col1"""
    

class Plot:
    def __init__(self):
        self.__plotnumber__ = 0
        self.__category__ = 0 #0 = residential, 1 = bussiness, 2 = industrial category
        self.__geom__ = 0
        self.__publicfeature__ = False #denotes if the plot is occupied by public feature eg school, hospital
        self.__location__ = 0

    def setplotnumber(self, plotnumber):
        self.__plotnumber__ = plotnumber

    def getplotnumber(self):
        return self.__plotnumber__
    
    def setcategory(self, category):
        self.__category__ = category

    def getcategory(self):
        return self.__category__
    
    def setgeom(self, geom):
        self.__geom__ = geom

    def getgeom(self):
        return self.__geom__
    
    def setpublicfeature(self, publicfeature):
        self.__publicfeature__ = publicfeature

    def getpublicfeature(self):
        return self.__publicfeature__
    
    def setlocation(self, location):
        self.__location__ = location

    def getlocation(self):
        return self.__location__
    def createplot(self):
        stingquery = """insert into plot """
    def deleteplot(self,id):
        stringquery = """delete from plot where id = '"""+id+"""';"""
    def updateplot(self,id):
        stringqiery = """udate plot set col1"""


class Payment:
    def __init__(self):
        self.__paymentid__ = 0
        self.__paymentamount__ = 0.0
        self.__owner__ = 0
        self.__plot__ = 0
        self.__comment__ = ''
    
    def setpaymentid(self, paymentid):
        self.__paymentid__ = paymentid

    def getpaymentid(self):
        return self.__paymentid__

    def setowner(self, owner):
        self.__owner__ = owner

    def getowner(self):
        return self.__owner__

    
    def setplot(self, plot):
        self.__plot__ = plot

    def getplot(self):
        return self.__plot__

    def setcomment(self, comment):
        self.__comment__ = comment

    def getcomment(self):
        return self.__comment__

    def setpaymentnumber(self, paymentnumber):
        self.__paymentnumber__ = paymentnumber

    def getpaymentnumber(self):
        return self.__paymentnumber__
    def createpayment(self):
        stingquery = """insert into payment """
    def deletepayment(self,id):
        stringquery = """delete from payment where id = '"""+id+"""';"""
    def updatepayment(self,id):
        stringqiery = """udate payment set col1"""
