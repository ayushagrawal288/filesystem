import os

directory = 'core/files/'


class DefaultStorage(object):
    @staticmethod
    def create(filename, file):
        if not os.path.exists(directory):
            os.mkdir(directory)
        path = os.path.join(directory, filename)
        new_file = open(path, 'wb')
        new_file.write(file.read())
        new_file.close()

    @staticmethod
    def delete(filename):
        if not os.path.exists(directory):
            os.mkdir(directory)
        path = os.path.join(directory, filename)
        try:
            os.remove(path)
        except FileNotFoundError:
            raise ValueError('invalid filename')


    @staticmethod
    def fetch(filename):
        if not os.path.exists(directory):
            os.mkdir(directory)
        path = os.path.join(directory, filename)
        try:
            file = open(path, 'rb')
        except FileNotFoundError:
            raise ValueError('invalid filename')
        data = file.read().decode('utf-8')
        file.close()
        return data

    @staticmethod
    def rename(new_name, previous_name):
        if not os.path.exists(directory):
            os.mkdir(directory)
        new_path = os.path.join(directory, new_name)
        previous_path = os.path.join(directory, previous_name)
        try:
            os.rename(new_path, previous_path)
        except FileNotFoundError:
            raise ValueError('invalid filename')

    @staticmethod
    def list():
        data = list()
        if not os.path.exists(directory):
            os.mkdir(directory)
        for f in os.listdir(directory):
            path = os.path.join(directory, f)
            if os.path.isfile(path):
                statinfo = os.stat(path)
                data.append({
                    "filename": f,
                    "size": statinfo.st_size,
                    "last_modified": statinfo.st_mtime
                })
        return data