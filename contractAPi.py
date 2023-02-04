import sqlite3
from contract import Contract


class ContractAPI:
    conn = sqlite3.connect('contract.db')
    cursor = conn.cursor()

    def __init__(self) -> None:
        self.conn
        # self.cursor.execute("""create table Contract(
        #     contract_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        #     start_date text,
        #     duration int,
        #     working_days text)""")
        # self.conn.commit()    
    def create_contract(self,contract:Contract):
        self.cursor.execute("insert into Contract(start_date, duration,working_days) values(?,?,?)",(contract.get_start_date(),contract.get_duration(),contract.get_working_days()))
        self.conn.commit()

    def read_Contract(self):
        with self.conn:
             return (self.cursor.execute("""select * from Contract limit 50 """))
    
    def update_contract(self,contract:Contract):
        with self.conn:
            self.cursor.execute("""update Contract set contract_id = :contract_id , start_date = :start_date, duration = :duration,working_days = :working_days 
                           where contract_id = :contract_id""",{'contract_id':contract.get_id() , 'start_date': contract.get_start_date(), 'duration':contract.get_duration() , 'working_days': contract.get_working_days()}) 

    def delete_contract(self,contract_id):
        with self.conn:
            self.cursor.execute("""delete from Contract 
            where contract_id = :contract_id""",{'contract_id': contract_id})
#contract = ContractAPI()