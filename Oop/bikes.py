class Bikes:
    def __init__(self,brand,bkname,rent):
        self._brandname =  brand
        self.__bikename =  bkname
        self.rentperday = rent
    @property
    def bikename(self):
        return self.__bikename
    @bikename.setter
    def bikename(self,bikename):
        self.__bikename = bikename
    def calculate_rent(self,days):
        return self.__rentperday*days
# by default all variables are public
 # _ is for protected variable
 # __ is for private variable
 #  to access private and protected variables have to use property in python which means getter and setter