import pandas as pd

df = pd.read_csv('ketqua.csv')
df = pd.DataFrame(df, columns=['TRUE', 'predict'])
dfLen = int(df.shape[0])

dict_result = {'predict_true': [], 'predict_false': [], 'sumary': []}
predict_true, predict_false, sumary = [], [], []

for i in range(dfLen):
    true, false = 0, 0

    for j in range(len(df.TRUE[i])):
        if df.TRUE[i][j] == df.predict[i][j]:
            true += 1
        else:
            false += 1
    true = int(true - 1)
    lenTRUE = int(len(df.TRUE[i]) - 1)
    predict_true.append(true)
    predict_false.append(false)
    sumary.append(lenTRUE)

dict_result['predict_true'] = predict_true
dict_result['predict_false'] = predict_false
dict_result['sumary'] =  sumary

df = pd.DataFrame(dict_result, columns=['predict_true', 'predict_false', 'sumary'])
df.to_csv(r'result.csv', index=False, header=True)
    