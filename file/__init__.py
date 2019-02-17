from os import remove, getcwd


class File:
    # TODO: add variable for absolute path
    def __init__(self, path):
        """
        Defines the path and file ending of the file in the supplied path param
        :param path: path to the file which the class will define. Can be local or absolute
        """
        dot = False
        self.fileEnding = '.'
        self.path = path
        for char in self.path:
            if not dot:
                if char == '.':
                    dot = True
                else:
                    pass
            elif dot:
                self.fileEnding += char

    def __str__(self):
        """
        :return: the files path
        """
        return self.path

    # the comparison operators compare the size of the file the path points to
    def __lt__(self, other):
        if isinstance(other, File):
            return self.size() < other.size()
        if isinstance(other, int):
            return self.size() < other

    def __le__(self, other):
        if isinstance(other, File):
            return self.size() <= other.size()
        if isinstance(other, int):
            return self.size() <= other

    def __gt__(self, other):
        if isinstance(other, File):
            return self.size() > other.size()
        if isinstance(other, int):
            return self.size() > other

    def __ge__(self, other):
        if isinstance(other, File):
            return self.size() >= other.size()
        if isinstance(other, int):
            return self.size() >= other

    def info(self):
        file_info = {
            "File-name": self.path,
            "Size_of_file": self.aprop_size(),
            "File-type": self.fileEnding
        }
        return file_info

    def delete(self, delete_object=True):
        """
        Deletes the file that self.path points to
        :param delete_object: determines if the object will be deleted too
        """
        remove(self.path)
        if delete_object:
            del self
        else:
            pass

    def content(self):
        """
        :return: the content of the file which the object.path points to
        """
        with open(self.path, 'r') as f:
            string_content = f.read()
            return string_content

    def size(self, prefix='bytes'):
        """
        :param prefix: determines if the returned value will be bytes, megabytes... etc
        :return: returns the number of bytes with the chosen prefix
        """
        file_bytes = 0
        with open(self.path, 'rb') as file:
            for row in file:
                for char in row:
                    file_bytes += 1
        if prefix == 'bytes':
            return file_bytes
        if prefix == 'kB':
            kilobytes = file_bytes / 1000
            return kilobytes
        if prefix == 'mB':
            megabytes = file_bytes / 1000000
            return megabytes
        if prefix == 'gB':
            gigabytes = file_bytes / 1000000000
            return gigabytes

    def aprop_size(self):
        if self.size() < 1000:
            size = str(self.size()) + " bytes"
            return size
        elif self.size() > 1000:
            size = str(self.size() / 1000) + " kB"
            return size
        elif self.size() > 1000000:
            size = str(self.size() / 1000000) + " mB"
            return size
        elif self.size() > 1000000000:
            size = str(self.size() / 1000000000) + " gB"
            return size


class NewFile(File):
    """
    Same as the class "File" but creates a file at the provided path first
    """
    def __init__(self, path, content=''):
        """
        :param path: path to the file which the object will handle
        """
        try:
            with open(path, 'r'):
                print(path, ' already exists')
            super().__init__(path)
        except FileNotFoundError:
            with open(path, 'a') as f:
                f.write(content)
            super().__init__(path)


file1 = File('test.txt')
file2 = NewFile('test2.txt', 'he')
print(file1.info())