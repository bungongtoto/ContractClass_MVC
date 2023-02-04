import sys
import constant

from contract import Contract
from contractAPi import ContractAPI
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog
import sqlite3

class MainWindow(QMainWindow):
    workDB = ContractAPI()
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("GUI.ui",self)

        self.contractTable.setColumnWidth(3,400)

        self.startDay.setMaximum(6)
        self.endDay.setMaximum(6)
        self.contract_id.setValue(0)
        self.duration.setValue(0)

        self.loadDataToTable() 

        self.Add_contract.clicked.connect(self.Add_new_contract)
        self.update_contract.clicked.connect(self.update_Existing_contract)
        self.checkBoxdel.clicked.connect(self.checkboxdelPressed)
        self.delete_contract.clicked.connect(self.delete_existing_contract)

        if  (self.checkBoxdel.isChecked()):
            self.startDay.setVisible(False)
            self.endDay.setVisible(False)
            self.duration.setVisible(False)
            self.start_date.setVisible(False)
            
        else:
            self.startDay.setVisible(True)
            self.endDay.setVisible(True)
            self.duration.setVisible(True)
            self.start_date.setVisible(True)

    

    def checkboxdelPressed(self):
        if  (self.checkBoxdel.isChecked()):
            self.startDay.setVisible(False)
            self.endDay.setVisible(False)
            self.duration.setVisible(False)
            self.start_date.setVisible(False)
            
        else:
            self.startDay.setVisible(True)
            self.endDay.setVisible(True)
            self.duration.setVisible(True)
            self.start_date.setVisible(True)

    def Add_new_contract(self):
        contract = Contract(int(self.contract_id.value()),str(self.start_date.text()),int(self.duration.value()),str(constant.DaysoftheWeek[self.startDay.value(): self.endDay.value() +1]))
        self.workDB.create_contract(contract)

        self.contract_id.setValue(0)
        self.duration.setValue(0)
        self.startDay.setValue(0)
        self.endDay.setValue(0) 
        self.loadDataToTable() 

    def update_Existing_contract(self):
        contract = Contract(int(self.contract_id.value()),str(self.start_date.text()),int(self.duration.value()),str(constant.DaysoftheWeek[self.startDay.value(): self.endDay.value() +1]))
        self.workDB.update_contract(contract)

        self.contract_id.setValue(0)
        self.duration.setValue(0)
        self.startDay.setValue(0)
        self.endDay.setValue(0) 
        self.loadDataToTable()       

    def delete_existing_contract(self):
        self.workDB.delete_contract(self.contract_id.value()) 
        self.contract_id.setValue(0) 
        self.loadDataToTable()  

    def loadDataToTable(self):
        self.contractTable.clearContents()
        self.contractTable.setRowCount(50)
        tableRow = 0

        for row in self.workDB.read_Contract():
            self.contractTable.setItem(tableRow,0,QtWidgets.QTableWidgetItem(str(row[0])))
            self.contractTable.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.contractTable.setItem(tableRow,2,QtWidgets.QTableWidgetItem(str(row[2])))
            self.contractTable.setItem(tableRow,3,QtWidgets.QTableWidgetItem(row[3]))

            tableRow +=1    