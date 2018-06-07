import os


class DefaultStorage(object):
    def __init__(self, directory):
        self.directory = directory

    def create(self, filename, file):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        path = os.path.join(self.directory, filename)
        new_file = open(path, 'wb')
        new_file.write(file.read())
        new_file.close()

    def delete(self, filename):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        path = os.path.join(self.directory, filename)
        try:
            os.remove(path)
        except FileNotFoundError:
            raise ValueError('invalid filename')

    def fetch(self, filename):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        path = os.path.join(self.directory, filename)
        try:
            file = open(path, 'rb')
        except FileNotFoundError:
            raise ValueError('invalid filename')
        dic = dict(
            filename=file.name,
            data=file.read().decode('utf-8')
        )
        file.close()
        return dic

    def rename(self, new_name, previous_name):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        new_path = os.path.join(self.directory, new_name)
        previous_path = os.path.join(self.directory, previous_name)
        try:
            os.rename(new_path, previous_path)
        except FileNotFoundError:
            raise ValueError('invalid filename')

    def list(self):
        data = list()
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        for f in os.listdir(self.directory):
            path = os.path.join(self.directory, f)
            if os.path.isfile(path):
                statinfo = os.stat(path)
                data.append({
                    "filename": f,
                    "size": statinfo.st_size,
                    "last_modified": statinfo.st_mtime
                })
        return data