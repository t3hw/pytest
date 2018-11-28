class IO:

    # Override this by IO child classes
    def getResults(self, dataSource):
        pass

    # Override this by IO chile classes
    def write(self, data):
        pass

    # General file write method
    def writeFile(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)
