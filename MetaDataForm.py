import tkinter as tk
from datetime import datetime

def MetaDataCollection(AttDict):
    """
    Creating a GUI based on the input dictionary "AttDict".

    If the value for a item is None, the GUI will put a hint "Requiring Inputs" (but it won't reject empty inputs)

    If no modification is conduct for an item,
    the value for that item will keep the same as the original input dictionary.
    Otherwise, the data format will be changed to String.

    The keys of the original dictionary will be kept.
    """

    class Att():
        """
        Class for all the attributes.
        """
        def __init__(self, value, key):
            self.value = value
            self.key = key

        @property
        def value(self):
            return self.__value

        @property
        def strValue(self):
            if self.isInstance:
                return str(self.__value)
            else:
                return "Requiring Inputs"
        @value.setter
        def value(self, value):
            if value is not None:
                self.__value = value
                self.isInstance = True
            else:
                self.__value = None

                self.isInstance = False
        @property
        def key(self):
            return self.__key
        @key.setter
        def key(self, key):
            self.__key = key
        @property
        def strKey(self):
            return str(self.__value)


    processedDict = {}
    for key, value in AttDict.items():
        processedDict[str(key)] = Att(value, key)

    def fetch(entries, processedDict):
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            if "Requiring Inputs" not in text and text != processedDict[field].strValue:
                processedDict[field].value = text

    def makeform(root, processedDict):
        entries = []
        for key, value in processedDict.items():
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=key, anchor='w')
            ent = tk.Entry(row, textvariable=tk.StringVar(root, value=value.strValue))
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((key, ent))
        return entries

    root = tk.Tk()
    root.geometry("600x300")
    ents = makeform(root, processedDict)

    root.bind('<Return>', (lambda event, e=ents: fetch(e, processedDict)))

    b1 = tk.Button(root, text='Submit',
                   command=(lambda e=ents: fetch(e, processedDict)))

    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()

    finalDict = {}
    for key in processedDict.keys():
        finalDict[processedDict[key].key] = processedDict[key].value
    return finalDict

if __name__ == '__main__':
    initDict = {"scalers":123, "string": "sadasd", 0: None, "datatime": datetime.now()}
    finalDict = MetaDataCollection(initDict)
    for key, value in finalDict.items():
        print(finalDict[key])
        print(finalDict[key].__class__)
        print(key)
        print(key.__class__)
        print("====================")