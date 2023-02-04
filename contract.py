import constant

class Contract:
    def __init__(self,contract_id,start_date,duration,working_days) -> None:
        self.__contract_id = contract_id
        self.__start_date = start_date
        self.__duration = duration
        self.__working_days = working_days

    def get_id(self):
        return self.__contract_id
    def get_start_date(self):
        return self.__start_date 
    def get_duration(self):
        return self.__duration 
    def get_working_days(self):
        return self.__working_days


    def set_id(self,id):
        self.__contract_id = id
    def set_start_date(self,date):
        self.__start_date = date 
    def set_duration(self,duration):
        self.__duration = duration
    def set_working_days(self,working_days):
        self.__working_days = working_days  

    def __str__(self) -> str:
        return(f"Contract \ncontract_id:{self.get_id()}\nstart_date:{self.get_start_date()}\n duration:{self.get_duration()}\n Working days: {self.get_working_days()}.. ")            



# contract = Contract(6,"03/48",7,constant.chooce_working_days())
# print(str(contract))