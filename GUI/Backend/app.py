from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS 
CORS(app, resources={r'/*': {'origins': '*'}})

#loading basic dataset
input_file = "parameters.xlsx"  # Name der Eingabedatei
df = pd.read_excel(input_file)
#df_filtered = pd.DataFrame()

#loading optional 10k dataset
input_file10k= "parameters.xlsx"
df10k = pd.read_excel(input_file10k)

#loading optional 10k random dataset
input_file10kr= "parameters.xlsx"
df10kr  = pd.read_excel(input_file10kr)

# sanity check route
@app.route('/search', methods=['GET'])
def filter_func():

    global df_filtered
    global df

    #if general filter, apply it 

    #DEPRACTICED function for 
    """     # takes too long to search every column, so better manually select the ones in question
    if request.args.get('all_content') != None: 
        searchvalues = request.args.get('all_content').split('%')
        # Initialize a series of True values
        mask = pd.Series([True] * len(df))
        for column in df.columns.to_list():
        #print(filter_dict)
            pattern = '|'.join(searchvalues)
            print(searchvalues)
            mask &= df[column].astype(str).str.contains(pattern, case=False, na=False)
            print ('filtered',column)  
        df_filtered=df[mask]
        
            
               
        #return (df[mask].to_html(header="true", table_id="table"))

        #return (str(len(df_filtered.index)))
        return (df_filtered.iloc[:, 0].to_list()) """
    input = ()
    input = request.args.get('input')
    print("recieved input request for file", input)
    if input==['5k']:
        df=df

    elif input==['10k']:
        df=df10k

    elif input==['10kr']:
        df=df10kr
    # filters to be applied for each column   
    filter_dict = {}
    for column in df.columns:
        if request.args.get(column) != None: 
            filter_dict[column] = request.args.get(column, default=None).split('%')
    #print(filter_dict)
   


    # Initialize a series of True values
    mask = pd.Series([True] * len(df))
            
    # change bool mask to filters from dict
    for column, values in filter_dict.items():
        print('checking column',column)
        if values:  # Only apply filter if values list is not empty
            pattern = '|'.join(values)
            mask &= df[column].str.contains(pattern, case=False, na=False)
            print ('filtered',column)  
    
    df_filtered=df[mask]
    #return (df[mask].to_html(header="true", table_id="table"))

    #return (str(len(df_filtered.index)))
    return (df_filtered.iloc[:, 0].to_list())

    #return (df_filtered.to_html(header="true", table_id="table"))




@app.route('/params', methods=['GET'])

def return_params():
    # Um die werte des aktuellen bildes abzurufen
    #TODO Performance improvement here, the df gets read again, raising complexibility to O(2n)
    # solution would be caching the results from previous request
    """ print('DF FILTERED SIZE',str(len(df_filtered.index)))
    pic_name = str(request.args.get("pic_name"))
    print(pic_name)
    print(df.iloc[:,[0]].astype(str))

    mask = df.iloc[:,[0]].astype(str) == pic_name
    # Check if any match is found and return the first matching row as a list
    result=df[mask].iloc[0].astype(str).tolist()
    print('Ergebnis',result)
    return (result) """
    
    pic_name = str(request.args.get("pic_name"))
    mask = pd.Series([True] * len(df))

    mask &= df['image'].str.contains(pic_name, case=False, na=False)
    df_filtered=df[mask].astype(str)
    result=df_filtered.iloc[0].tolist()

    return(result)
    # Create a mask that checks each element of the DataFrame for the string
    """ mask = df.apply(lambda row: row.astype(str).str.contains(pic_name, case=False).any(), axis=1)

    print("mask created")
    # Return the first row that contains the string
    #  first_row = df[mask].iloc[0] if not df[mask].empty else None
    first_row_list = df[mask].iloc[0].astype(str).tolist() if not df[mask].empty else None

    print("first row",first_row_list)
    return (first_row_list) """
