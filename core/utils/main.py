from core.utils.s3 import S3Filesystem
from core.utils.defaultStorage import DefaultStorage


class FileStorage(object):
    def __init__(self, type='default'):
        if type == 's3':
            self.storage = S3Filesystem()
        else:
            self.storage = DefaultStorage()

    def create(self, filename, file):
        return self.storage.create(filename, file)

    def delete(self, filename):
        return self.storage.delete(filename)

    def rename(self, new_name, previous_name):
        return self.storage.rename(new_name, previous_name)

    def fetch(self, filename):
        return self.storage.fetch(filename)

    def list(self):
        return self.storage.list()
