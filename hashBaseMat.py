import json

"""
Written By:
Mor Nagli, Tom Eliya, Hen Ben LuLu, Niv Nagli
"""


class hashBaseMat:
    def __init__(self):
        self.baseHashMap = {}

    def buildJsonHashFromBasesFile(self, fileName, dim):
        try:
            basesFile = open(fileName)
            data = json.load(basesFile)
            basesFile.close()
            self.fillHashFromFileData(data)
            with open(f'basesHash{dim}.json', 'w') as fp:
                json.dump(self.baseHashMap, fp)

        except Exception as e:
            raise ValueError(f'buildJsonHashFromBasesFile failed following to : {e} \n')

    def fillHashFromFileData(self, fileData):
        self.baseHashMap = {}  # Reset the previous result if we have one.
        for base in fileData:
            self.baseHashMap[int(base, 2)] = True


if __name__ == '__main__':
    hashBuilder = hashBaseMat()
    hashBuilder.buildJsonHashFromBasesFile('bases_5.json', 5)
