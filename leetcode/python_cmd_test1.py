data = [['13', '02', '>'], ['13', '04', 'Boot Manager'], ['14', '02', '>'], ['14', '04', 'Boot Maintenance Manager']]

h = ['14', 'Boot Maintenance Manager', None]


class SSHOutput(object):
    """Display the bios setup menu"""

    def __init__(self, status: bool, terminal_size=(80, 26)):
        self.width = terminal_size[0]
        self.height = terminal_size[1]
        self.status = status
        self.page = None
        self.high_sign = ' *'
        self.column = 0
        self.row = 0
        self.next_row = 0

    def display_page(self, page_data: list, highlight_line: list):
        page_data.sort()
        self.row = int(page_data[0][0])
        self.page = '\n' * self.row

        if self.status:
            for line_num, line_data in enumerate(page_data):
                self.column = int(line_data[1])

                # row
                self.next_row = int(line_data[0]) - self.row
                if self.next_row:
                    self.page += '\n' * self.next_row
                    self.row = int(line_data[0])
                    self.column = int(line_data[1])

                # column
                elif not self.next_row and line_num > 0:
                    self.column = int(line_data[1]) - len(page_data[line_num-1][2])

                self.page += ' ' * self.column
                self.page += line_data[2]

        self.page += '\n'*2

        self._display_highlight(highlight_line)
        return self.page

    def _display_highlight(self, highlight_line):
        if highlight_line[2]:
            highlight_line[1] = highlight_line[2]
        self.page = self.page.replace(highlight_line[1], highlight_line[1] + self.high_sign)


ssh = SSHOutput(True)
print(ssh.display_page(data, h))
