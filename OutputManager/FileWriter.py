class FileWriter:

    def write(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)
