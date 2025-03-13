import pandas as pd

def generateCsv(data):
    df = pd.DataFrame(data)
    csv_file = 'newssentiment.csv'
    df.to_csv(csv_file, index=False)