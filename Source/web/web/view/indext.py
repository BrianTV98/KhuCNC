import pandas as pd
import pyodbc
from web.contrains.base_url import base_url_model, conn
from web.model.YearFromTo import YearFromTo


def getYearFromTo():
    data = pd.read_sql_query('Exec SP_DASHBOARD_THONGKE_GET_YEAR', conn)  # get dat
    result = [
        (YearFromTo(row.MinYear, row.MaxYear)) for
        index, row in data.iterrows()]
    result_to_json = [vars(ob) for ob in result]
    return result_to_json[0]