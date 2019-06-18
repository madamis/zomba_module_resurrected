import psycopg2


class Plot:
    def __init__(self):
        self.__plotnumber__ = 0
        self.__category__ = 0  # 0 = residential, 1 = bussiness, 2 = industrial category
        self.__geom__ = 0
        self.__publicfeature__ = False  # denotes if the plot is occupied by public feature eg school, hospital
        self.__location__ = 0
        try:
            connection = psycopg2.connect(user='postgres', password='12345678', host='localhost', port='5432',
                                      database='zomba_malawi')
            cursor = connection.cursor()
            query = """select * from finale_plot;"""
            cursor.execute(query)
            master_plot = [x for x in cursor]

        except(Exception, psycopg2.Error) as error:
            if (connection):
                print('failed to connect', error)

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

    def deleteplot(self, id):
        stringquery = """delete from plot where id = '""" + id + """';"""

    def updateplot(self, id):
        stringqiery = """udate plot set col1"""