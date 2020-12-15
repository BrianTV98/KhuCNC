import pyodbc

base_url_model = "D:\\KhuCNC\\Source\\model"

conn = pyodbc.connect('Driver={SQL Server};'  # connect with SQL server
                      'Server=DESKTOP-LAFLFDC;'
                      'Database=DUAN_KHUCNC;'
                      'Trusted_Connection=yes;')

# base_url_model = "E:\do_an_tot_nghiep\Source\model"
# conn = pyodbc.connect('Driver={SQL Server};'  # connect with SQL server
#                       'Server=DESKTOP-05ICLAS\SERVER2;'
#                       'Database=DUAN_KHUCNC;'
#                       'Trusted_Connection=yes;')
