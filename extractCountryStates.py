import json
import pandas as pd
from simple_salesforce import SalesforceLogin, SFType, Salesforce, bulk
import base64

#Instalar requirements

username = ''
password = ''
security_token = ''
domain = 'login'  #login para prod o test para desarrollo

session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance=instance, session_id=session_id)
print(sf)

acc_metadata = SFType('Account', session_id, instance).describe().get('fields')
acc_df = pd.DataFrame(acc_metadata)
States_data = acc_df[acc_df['name'] == 'BillingStateCode']['picklistValues']
Country_data = acc_df[acc_df['name'] == 'BillingCountryCode']['picklistValues']

for i in States_data:
    States = pd.DataFrame(i)
    print(States)
    break

for i in Country_data:
    Countries = pd.DataFrame(i)
    break

def getCountry(encoded_value):
    encoded_value
    decoded_bytes = base64.b64decode(encoded_value)
    binary_representation = ''.join(format(byte, '08b') for byte in decoded_bytes)
    position = binary_representation.find('1')
    return position

States['CountryPosition'] = States['validFor'].apply(getCountry)
States = States.rename(columns={'active': 'State_isActive', 'label': 'State_Label', 'validFor': 'validFor', 'value': 'StateValue', 'CountryPosition': 'Index'})
Countries['Index'] = range(0, len(Countries))
result = pd.merge(States, Countries, on='Index', how='outer')
result = result.drop(['validFor_x', 'validFor_y', 'Index'], axis=1)

#Opcion de configurar el mapeo de columnsas de salida
result = result.rename(columns={'defaultValue_x': 'State_IsdefaultValue', 'defaultValue_y': 'Country_IsdefaultValue', 'label': 'CountryLabel', 'value': 'CountryValue', 'active': 'CountryIsactive'})
data = result[['CountryLabel', 'CountryValue', 'Country_IsdefaultValue', 'CountryIsactive', 'State_Label', 'StateValue', 'StateValue', 'State_isActive', 'State_IsdefaultValue']]

#Cuidado con las rutas relativas y completas + extension del archivo
data.to_excel(r'C:\Users\pablo.sagredo\OneDrive - PKF Attest\Documentos\Scripts\output.xlsx', index=False)


