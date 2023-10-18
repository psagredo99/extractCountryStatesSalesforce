
# Salesforce Country + States extract

```markdown
As Salesforce doesnt provide a native option for this featiure,this Python script allows you to connect to a Salesforce instance, retrieve metadata information for Accounts, and export it to an Excel file. The script uses the `simple_salesforce` library to establish a connection with Salesforce and `pandas` to manipulate the data.

## Prerequisites

Before using this script, ensure you have the necessary packages installed. You can install the required packages by running the following command:

```bash
pip install -r requirements.txt


Make sure you have the following information ready:

- Salesforce Username
- Salesforce Password
- Salesforce Security Token
- Salesforce Domain (use 'login' for production or 'test' for development)

-   If dont display reset token option add this to org url: https://****.com/_ui/system/security/ResetApiTokenEdit


## Usage

1. Fill in your Salesforce credentials in the script:

```python
username = ''
password = ''
security_token = ''
domain = 'login'  # 'login' for production or 'test' for development
```

2. Run the script to connect to Salesforce and retrieve metadata information for Accounts.

3. The script will export the data to an Excel file with customizable output columns. You can configure the output columns by editing the script.

```python
data.to_excel('output.xlsx', index=False)
```

4. Run the script:

```bash
python python extractCountryStates.py
```

## Output

The script will generate an Excel file named `output.xlsx` in the specified output directory.

![image](https://github.com/psagredo99/extractCountryStatesSalesforce/assets/72439144/9f036307-23b8-4ed4-b6e5-00cca20ee296)


## Configuration

You can customize the output columns by editing the script. Look for the section labeled "Opcion de configurar el mapeo de columnas de salida" and modify the `data` DataFrame to include the columns you need.

## Acknowledgments

- [Simple Salesforce](https://pypi.org/project/simple-salesforce/)
- [Pandas](https://pypi.org/project/pandas/)
- [Salesforce](https://www.salesforce.com/)

Feel free to modify this README to provide more specific details about your project and its usage.
