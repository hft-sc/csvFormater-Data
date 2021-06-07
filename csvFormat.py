import argparse
import pandas as pd
import re

parser = argparse.ArgumentParser()
parser.add_argument('-f','--filename')
parser.add_argument('-o1','--output1')
parser.add_argument('-o2','--output2')
parser.add_argument('-wR','--wantedRows', type=int)
args = parser.parse_args()

with open(args.filename,'r') as csv_file, open(args.output1, "w+") as bankdata1,open(args.output2, "w+") as bankdata2:
    df = pd.read_csv(csv_file)
    listOfDfOne = [2]
    listOfDfZero = [2]
    #print(df)
    valuesWithOne = df.loc[df["9"] == 1.0]
    valuesWithZero = df.loc[df["9"] == 0.0]

    wantedRows = args.wantedRows
    percentageOne = len(valuesWithOne) / (len(valuesWithZero) + len(valuesWithOne))
    percentageZero = 1 - percentageOne

    #print(f"length one: {len(valuesWithOne)}")
    #print(f"length zero: {len(valuesWithZero)}")

    split = int(percentageOne * (2 * wantedRows / 3))
    valuesWithOnePartI = valuesWithOne.iloc[:split, :]
    valuesWithOnePartII = valuesWithOne.iloc[split: wantedRows, :]

    split = int(percentageZero * (2 * wantedRows / 3))
    valuesWithZeroPartI = valuesWithZero.iloc[:split, :]
    valuesWithZeroPartII = valuesWithZero.iloc[split : wantedRows,:]

    trainingData = valuesWithOnePartI.append(valuesWithZeroPartI)
    testData = valuesWithOnePartII.append(valuesWithZeroPartII)

    trainingData.to_csv(bankdata1, index=False, line_terminator='\n')
    testData.to_csv(bankdata2, index=False, line_terminator='\n')