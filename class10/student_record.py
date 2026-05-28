class studentRecord:
    def __init__ (self,name,gpa,credits): ## En la task dice validar que name no sea empty pero no dice que creemos una property
                                            ##Como podemos validar name sin usar property?
        self.name=name
        self.gpa=gpa
        self.credits=credits

    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self,gpa):
        if 0 <=  gpa <= 4.0:
            self.__gpa=gpa
        else:
            raise ValueError('Gpa needs to be between 0 and 4.0')
            
    @property
    def credits(self):
        return self.__credits
    
    @credits.setter
    def credits(self,amount):
        
            if amount >=0:
                self.__credits=amount

            else:
                raise ValueError('Credits need to be equal or greater than 0 ')

    def add_credits(self,amount):
        if amount>=0:
            self.__credits+=amount
            print(f"${amount} credits were added")
        else:
            raise ValueError('You cannot substract CREDITS')
    
    def update_gpa(self,value):
        self.gpa=value
        print (f"Your Gpa was updated. New Gpa: {self.__gpa}")

    def display_info(self):
        print(f"{self.name} your current Gpa is : {self.__gpa} and you have {self.credits} credits")

##Creating studentRecord
student1=studentRecord("Danielle",2.0,36)
print(student1.gpa)
##student1.gpa=7.0 ##-> Tratando de cambiar el gpa pero al llamar al setter la invariant impide que el valor se cambie ya que no cumple con la regla
##print(student1.gpa)

student1.update_gpa(3.63)
##Adding credits
student1.add_credits(12)
student1.display_info()
    

    