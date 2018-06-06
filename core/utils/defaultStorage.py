import os

directory = '/core/files/'


class DefaultStorage(object):
    @staticmethod
    def create(filename, file):
        new_file = open(directory + filename, 'wb')
        new_file.write(file.read())
        new_file.close()

    @staticmethod
    def delete(filename):
        os.remove(directory + filename)


    @staticmethod
    def fetch(filename):
        file = open(directory + filename, 'rb')
        data = file.read()
        file.close()
        return data

    @staticmethod
    def rename(new_name, previous_name):
        os.rename(directory + new_name, directory + previous_name)

    @staticmethod
    def list():
        data = list()
        for f in os.listdir(directory):
            path = os.path.join(directory, f)
            if os.path.isfile():
                statinfo = os.stat(path)
                data.append({
                    "filename": f,
                    "size": statinfo.st_size,
                    "last_modified": statinfo.st_mtime
                })
        return data