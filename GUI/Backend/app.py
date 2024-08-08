from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd



# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/search', methods=['GET'])
def filter_func():
    

    input_file = "params700k.csv"  # Name der Eingabedatei
    df = pd.read_csv(input_file)

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

    return (df_filtered.to_html(header="true", table_id="table"))






    


if __name__ == '__main__':
    app.run()
