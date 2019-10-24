import  yaml
import os

from tool.config import BASE_URL


def read_yaml(filename):
    with open(BASE_URL+os.sep+"data"+os.sep+filename,"r",encoding="utf-8") as f:
        return yaml.load(f)

if __name__ == '__main__':
    print(read_yaml("login.yaml"))
    print("--"*80)
    arr = []
    for data in read_yaml("login.yaml").values():

        arr.append(tuple(data.values()))