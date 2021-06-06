import argparse
import pandas as pd
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument('-f','--filename')
parser.add_argument('-o1','--output1')
parser.add_argument('-o2','--output2')
args = parser.parse_args()

with open(args.filename,'r') as csv_file, open(args.output1, 'w') as bankdata1,open(args.output2, "w") as bankdata2:
    df = pd.read_csv(csv_file)
    listOfDfOne = [2]
    listOfDfZero = [2]
    #print(df)
    valuesWithOne = df.loc[df["9"] == 1.0]
    valuesWithZero = df.loc[df["9"] == 0.0]

    #print(f"length one: {len(valuesWithOne)}")
    #print(f"length zero: {len(valuesWithZero)}")

    valuesWithOnePartI = valuesWithOne.iloc[:int(len(valuesWithOne) / 2),:]
    valuesWithOnePartII = valuesWithOne.iloc[int(len(valuesWithOne) / 2) :,:]

    valuesWithZeroPartI = valuesWithZero.iloc[:int(len(valuesWithZero) / 2),:]
    valuesWithZeroPartII = valuesWithZero.iloc[int(len(valuesWithZero) / 2) :,:]

    trainingData = valuesWithOnePartI.append(valuesWithZeroPartI)
    testData = valuesWithOnePartII.append(valuesWithZeroPartII)

    trainingData.to_csv(bankdata1, index=False)
    testData.to_csv(bankdata2, index=False)
    

    
          