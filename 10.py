import pandas as pd
import random
import sklearn as s
from sklearn. preprocessing import OneHotEncoder
robot = 'robot'
human = 'human'
whoIAm = 'whoAmI'
lst = [robot] * 10
lst += [human] * 10
random.shuffle(lst)
data = pd.DataFrame({whoIAm:lst})
ohe = OneHotEncoder(handle_unknown='ignore')
arrayOhe = pd.DataFrame(ohe.fit_transform(data[[whoIAm]]).toarray())
result = data.join(arrayOhe)
result.drop(whoIAm, axis= 1, inplace= True)
result.columns = [robot, human]
print(result)