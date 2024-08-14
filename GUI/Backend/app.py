from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd



# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


input_file = "parameters.xlsx"  # Name der Eingabedatei
df = pd.read_excel(input_file)
df_filtered = pd.DataFrame( )

# sanity check route
@app.route('/search', methods=['GET'])
def filter_func():
    
    global df_filtered

    #if general filter, apply it 

    #TODO BUGFIXING HERE
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
        return (df_filtered.iloc[:, 0].to_list())


    else:


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
    print('DF FILTERED SIZE',str(len(df_filtered.index)))
    pic_name = request.args.get("pic_name")  
    print(pic_name)


    # Create a mask that checks each element of the DataFrame for the string
    mask = df.apply(lambda row: row.astype(str).str.contains(pic_name, case=False).any(), axis=1)


    # Return the first row that contains the string
    #  first_row = df[mask].iloc[0] if not df[mask].empty else None
    first_row_list = df[mask].iloc[0].astype(str).tolist() if not df[mask].empty else None

    print("first row",first_row_list)
    return (first_row_list)
