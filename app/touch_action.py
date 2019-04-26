class action:
    def __init__(self):
        self._content = ''

    def append(self, new_content):
        self._content += new_content + '\n'

    def commit(self):
        """ minitouch command, eg: 'c\n' """
        self.append('c')

    def wait(self, ms):
        """ minitouch command, eg: 'w 1000\n' """
        self.append('w {}'.format(ms))

    def up(self, contact_id):
        """ minitouch command, eg: 'u 0\n' """
        self.append('u {}'.format(contact_id))

    def down(self, contact_id, x, y, pressure):
        """ minitouch command, eg: 'd 0 200 200 50\n' """
        self.append('d {} {} {} {}'.format(contact_id, x, y, pressure))

    def move(self, contact_id, x, y, pressure):
        """ minitouch command, eg: 'm 0 200 200 50\n' """
        self.append('m {} {} {} {}'.format(contact_id, x, y, pressure))


def click(x,y,pressure=50):
    action().down(x,y,pressure)
    action().commit()
    return action()._content

