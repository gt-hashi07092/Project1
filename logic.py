from PyQt6 import QtWidgets
import csv
from votemenu import Ui_MainWindow
import os

class VotingWindow(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.setupUi(self)
       self.pushButton_vote.clicked.connect(self.submit_vote)
       
       if not os.path.exists("votes.csv"):
            open("votes.csv", "w").close()

   def submit_vote(self):
       # Get user input data
       first_name = self.lineEdit_firstname.text()
       last_name = self.lineEdit_latname.text()
       street_address = self.lineEdit_stadress.text()
       city = self.lineEdit_city.text()
       state = self.comboBox_state.currentText()
       zipcode = self.lineEdit_zipcode.text()
       month = self.comboBox_month.currentText()
       date = self.comboBox_date.currentText()
       year = self.lineEdit_year.text()
       candidate = self.get_selected_candidate()

       # Check if any field is empty
       if not all([first_name, last_name, street_address, city, state, zipcode, month, date, year, candidate]):
           self.label_text.setText("Please fill all information")
           for lineEdit in self.findChildren(QtWidgets.QLineEdit):
               if not lineEdit.text():
                   lineEdit.setPlaceholderText("Please fill this information")
           return

       # Check if the user has already voted
       user_data = [first_name, last_name, street_address, city, state, zipcode, f"{month}/{date}/{year}", candidate]
       with open("votes.csv", "r") as file:
           reader = csv.reader(file)
           if user_data in [row for row in reader]:
               self.label_text.setText("You have already voted.")
               return
               
           
        # Check if zipcode is numeric
       if not zipcode.isdigit():
           if not year.isdigit():
               self.label_text.setText("Please fill all information correctly. Please fill zip code and year with number.")
               return
           else:
               self.label_text.setText("Please fill all information correctly. Please fill zip code with number.")
               return
       else:
           if not year.isdigit():
               self.label_text.setText("Please fill all information correctly. Please fill year with number.")
               return
           

       # Write the vote data to the CSV file
       with open("votes.csv", "a", newline="") as file:
           writer = csv.writer(file)
           writer.writerow(user_data)

       # Clear the input fields
       for lineEdit in self.findChildren(QtWidgets.QLineEdit):
           lineEdit.clear()
       self.label_text.setText("You successfully voted!")

   def get_selected_candidate(self):
       if self.radioButton_bianca.isChecked():
           return "Bianca"
       elif self.radioButton_edward.isChecked():
           return "Edward"
       elif self.radioButton_felicia.isChecked():
           return "Felicia"
       else:
           return ""

if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = VotingWindow()
   MainWindow.show()
   sys.exit(app.exec())