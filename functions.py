import pandas as pd

def generateCsv(data):
    df = pd.DataFrame(json_data)
    csv_file = 'newssentiment.csv'
    df.to_csv(csv_file, index=False)