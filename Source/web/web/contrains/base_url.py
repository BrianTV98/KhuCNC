import pyodbc
base_url_model = "D:\\KhuCNC\\Source\\model"

conn = pyodbc.connect('Driver={SQL Server};'  # connect with SQL server
                      'Server=DESKTOP-RRUVR94;'
                      'Database=DUAN_KHUCNC;'
                      'Trusted_Connection=yes;')