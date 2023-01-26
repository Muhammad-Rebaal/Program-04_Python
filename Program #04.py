


                    #Classes , Objects and Instances
                    #______________________________
                    
class Company:
    def __init__(self,iname,isalary,iposition):
        self.name= iname
        self.salary = isalary
        self.position = iposition
    def details(self):
        return ("This is your Employee name " +str(self.name) +" , this is his salary " + str(self.salary) +\
            " and this is his position " + str(self.position))

Rebaal = Company("M.Rebaal",5000,"Ceo")
# Rebaal.name = "M.Rebaal"
# Rebaal.salary = 5000
# Rebaal.position = "Ceo"

print(Rebaal.details())
    