from datetime import datetime,date
from models import Lembrete
data='31/12/2021'
data_atual= datetime.date.today().strftime('%d/%m/%Y')
data_formatada= datetime.strptime(data, '%d/%m/%Y').date()
if data_formatada >= data_atual:
   print('é')
else: 
    print('não é')