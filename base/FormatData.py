import pandas as pd
import numpy as np

class Data():
  def __init__(self,data_read):
    self.data_read = data_read.sort_values(by=["TIME"]).reset_index(drop = True)

  def GetField(self):
    return self.data_read.columns.copy()

  def SetupData(self):
    data_ETL = pd.DataFrame(
        {
            'BUY': self.data_read['BUY'],
            'SELL': self.data_read['SELL'],
            'VOLUME': self.data_read['VOLUME'],
            'MARKET CAPITALIZATION': self.data_read['MARKET CAPITALIZATION'],
            'EARNINGS': self.data_read['EARNINGS'],
            'COGS': self.data_read['COGS'],
            'SALES': self.data_read['SALES'],
            'CASH': self.data_read['CASH'],
            'INVESTMENTS': self.data_read['INVESTMENTS'],
            'RECEIVABLES': self.data_read['RECEIVABLES'],
            'INVENTORY': self.data_read['INVENTORY'],
            'DEBTS': self.data_read['DEBTS'],
            'PROFIT': self.data_read['PROFIT'],
        }, dtype=np.float
    )
    data_ETL.insert(loc=0, column='TIME', value=self.data_read['TIME'])
    data_ETL.insert(loc=1, column='SYMBOL', value=self.data_read['SYMBOL'])
    return data_ETL
  def ExportDataForArray(self,):
    data = self.SetupData()
    A = np.array(data['MARKET CAPITALIZATION'])
    B = np.array(data['EARNINGS'])
    C = np.array(data['COGS'])
    D = np.array(data['SALES'])
    E = np.array(data['CASH'])
    F = np.array(data['INVESTMENTS'])
    G = np.array(data['RECEIVABLES']),
    H = np.array(data['INVENTORY'])
    I = np.array(data['DEBTS'])
    profit = np.array(data['PROFIT'])
    return A,B,C,D,E,F,G,H,I,profit


class DataYear(Data):
  pass

class DataQuater(Data):
  pass