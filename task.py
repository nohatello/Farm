# The farm have Farmers, chickens, chicks, ducks, duckling , and also cocks/Roasters
# class that contain the Authentication Utilities and common used helper methods
class Farm:
    # helper methods
    def __init__(self, name): 
        self.name = name
    def Weight(self):              
        raise NotImplementedError
    def Count(self):              
        raise NotImplementedError
    def Gender(self):              
        raise NotImplementedError
    def Age(self):              
        raise NotImplementedError
    def House(self):              
        raise NotImplementedError
    def Vaccines(self):              
        raise NotImplementedError
    def Date(self):              
        raise NotImplementedError
    def Eggs(self):              
        raise NotImplementedError
    def Feed(self):              
        raise NotImplementedError
    def Salary(self):              
        raise NotImplementedError

class Farmers(Farm):
    # Helper method to get name
    def getName(self):
        return 'Farmers'
    # Helper method to get count of farmers in the farm 
    def getCount(self):
        return 'There are 10 farmers in the farm'
    # Helper method to get farmer's salary
    def getSalary(self):
        return 'The average salary is 2000 Dollar'  
    # Helper method to set count of farmers in the farm 
    def setCount(newCount):
        self.Count = newCount  
    # Helper method to set farmer's salary
    def setSalary(newSalary):
        self.Salary = newSalary   

class Chickens(Farm):
    # Helper method to get name
    def getName(self):
        return 'Chickens'
    # Helper method to get count of chickens
    def getCount(self):
        return 'These are 200 chickens in the farm'
    # Helper method to get chicken's average weight
    def getWeight(self):
        return 'The average weight is 1,700 gm '
    # Helper method to get gender
    def getGender(self):
        return 'Females'
    # Helper method to get chicken's average age
    def getAge(self):
        return 'The average age is 7 months'
    # Helper method to get chicken's house
    def getHouse(self):
        return 'White henhouses'
    # Helper method to get chicken's vaccine
    def getVaccines(self):
        return 'These need lasota vaccine'
    # Helper method to get when chickens came to farm
    def getDate(self):
        return 'These came to farm at 20\10\2016'
    # Helper method to get how much chicken's eggs in one day
    def getEggs(self):
        return 'The average is one egg/day '
    # Helper method to get chicken's feed
    def getFeed(self):
        return 'These need pullet developer and layer rations ' 
    # Helper method to set count of chickens in the farm 
    def setCount(newCount):
        self.Count = newCount   
    # Helper method to set chicken's average weight
    def setWeight(newWeight):
        self.Weight= newWeight 
    # Helper method to set chicken's average age
    def setAge(newAge):
        self.Age = newAge    
        
class Roasters(Farm):
    # Helper method to get name
    def getName(self):
        return 'Roasters'
    # Helper method to get count of roasters
    def getCount(self):
        return 'These are 80 roasters in the farm'
    # Helper method to get roaster's average weight
    def getWeight(self):
        return 'The average weight is 2,200 gm '
    # Helper method to get gender
    def getGender(self):
        return 'Males'
    # Helper method to get roaster's average age
    def getAge(self):
        return 'The average age is 7 months'
    # Helper method to get roaster's house
    def getHouse(self):
        return 'White henhouses'
    # Helper method to get roaster's vaccine
    def getVaccines(self):
        return 'These need lasota vaccine '
    # Helper method to get when roasters came to farm
    def getDate(self):
        return 'These came to farm at 20\10\2016'
    # Helper method to get roaster's feed
    def getFeed(self):
        return 'These need pullet developer and layer rations'
    # Helper method to set count of roasters in the farm 
    def setCount(newCount):
        self.Count = newCount   
    # Helper method to set roaster's average weight
    def setWeight(newWeight):
        self.Weight= newWeight 
    # Helper method to set roaster's average age
    def setAge(newAge):
        self.Age = newAge     

class Chicks(Farm):
    # Helper method to get name
    def getName(self):
        return 'Chicks'
    # Helper method to get count of chicks
    def getCount(self):
        return 'These are 300 chicks in the farm'
    # Helper method to get chick's average weight
    def getWeight(self):
        return 'The average weight is 200 gm '
    # Helper method to get gender
    def getGender(self):
        return 'Both of genders'
    # Helper method to get chick's average age
    def getAge(self):
        return 'The average age is 15 days'
    # Helper method to get chick's house
    def getHouse(self):
        return 'White henhouses'
    # Helper method to get chick's vaccine
    def getVaccines(self):
        return 'These need 3 types of vaccines: hitchner b1 , ND clon30 and gumboro D78 '
    # Helper method to get chick's feed
    def getFeed(self):
        return 'These need chick starter then grower pullet'
    # Helper method to set count of chicks in the farm 
    def setCount(newCount):
        self.Count = newCount   
    # Helper method to set chick's average weight
    def setWeight(newWeight):
        self.Weight= newWeight 
    # Helper method to set chick's average age
    def setAge(newAge):
        self.Age = newAge     

class Ducks(Farm):
    # Helper method to get name
    def getName(self):
        return 'Ducks'
    # Helper method to get count of ducks
    def getCount(self):
        return 'These are 200 ducks in the farm'
    # Helper method to get duck's average weight
    def getWeight(self):
        return 'The average weight is 4000 gm '
    # Helper method to get gender
    def getGender(self):
        return 'Females'
    # Helper method to get duck's average age
    def getAge(self):
        return 'The average age is 5 months'
    # Helper method to get duck's house
    def getHouse(self):
        return 'Brown henhouses'
    # Helper method to get duck's vaccine
    def getVaccines(self):
        return 'These are need 2 types of vaccines: duck viral enteritis and duck viral hepatitis'
    # Helper method to get how much ducks's eggs in 5 days
    def getEggs(self):
        return 'The average is one egg/5days '    
    # Helper method to get when ducks came to farm
    def getDate(self):
        return 'These came to farm at 10\10\2016'
    # Helper method to get duck's feed
    def getFeed(self):
        return 'These need corn and soyabeen meal '
    # Helper method to set count of ducks in the farm 
    def setCount(newCount):
        self.Count = newCount   
    # Helper method to set duck's average weight
    def setWeight(newWeight):
        self.Weight= newWeight 
    # Helper method to set duck's average age
    def setAge(newAge):
        self.Age = newAge     
    
class Cocks(Farm):
    # Helper method to get name
    def getName(self):
        return 'Cocks'
    # Helper method to get count of cocks
    def getCount(self):
        return 'These are 80 cocks in the farm'
    # Helper method to get cock's average weight
    def getWeight(self):
        return 'The average weight is 4500 gm '
    # Helper method to get gender
    def getGender(self):
        return 'Males'
    # Helper method to get cock's average age
    def getAge(self):
        return 'The average age is 7 months'
    # Helper method to get cock's house
    def getHouse(self):
        return 'Brown henhouses'
    # Helper method to get cock's vaccine
    def getVaccines(self):
        return 'These are need 2 types of vaccines: duck viral enteritis and duck viral hepatitis'
    # Helper method to get when cocks came to farm
    def getDate(self):
        return 'These came to farm at 10\10\2016'
    # Helper method to get cock's feed
    def getFeed(self):
        return 'These need corn and soyabeen meal '
    # Helper method to set count of cocks in the farm 
    def setCount(newCount):
        self.Count = newCount   
    # Helper method to set cocks's average weight
    def setWeight(newWeight):
        self.Weight= newWeight 
    # Helper method to set cock's average age
    def setAge(newAge):
        self.Age = newAge     

class Duckling(Farm):
    # Helper method to get name
    def getName(self):
        return 'Duckling'
    # Helper method to get count of duckling
    def getCount(self):
        return 'These are 300 duckling in the farm'
    # Helper method to get duckling's average weight
    def getWeight(self):
        return 'The average weight is 500 gm '
    # Helper method to get gender
    def getGender(self):
        return 'Both sex'
    # Helper method to get duckling's average age
    def getAge(self):
        return 'The average age is 15 days'
    # Helper method to get duckling's house
    def getHouse(self):
        return 'Brown henhouses'
    # Helper method to get duckling's vaccine
    def getVaccines(self):
        return 'These need R-anatipestifer '
    # Helper method to get duckling's feed
    def getFeed(self):
        return 'These need tiny fresh water snail and fountains'
    # Helper method to set count of ducklings in the farm 
    def setCount(newCount):
        self.Count = newCount   
    # Helper method to set duckling's average weight
    def setWeight(newWeight):
        self.Weight= newWeight 
    # Helper method to set duckling's average age
    def setAge(newAge):
        self.Age = newAge     
        
#for example
animals = [Ducks]

for animal in animals:
    print ("Name = " + animal.getName('self') + ('\n') + 'Age = ' + animal.getAge('self')
           + ('\n') + 'House = ' + animal.getHouse('self')
           + ('\n') + 'Vaccines = ' + animal.getVaccines('self')
           + ('\n') + 'Feed = ' + animal.getFeed('self'))

# prints the following:
#
# Name = Ducks
# Age = The average age is 5 months
# House = Brown henhouses
# Vaccines = These are need 2 types of vaccines: duck viral enteritis and duck viral hepatitis
# Feed = These need corn and soyabeen meal 