from abc import abstractmethod, ABC
from Bot import Bot


class Output(ABC):

    @abstractmethod
    def output(self, result):
        pass


class TerminalOutput(Output):
    
    def __init__(self):
        self.delimiter = '-----'

    def output(self, result: str):
        print(self.delimiter, result, self.delimiter, sep='\n')


if __name__ == "__main__":
    terminal = TerminalOutput()
    terminal.output('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")
    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            result = ''
            format_str = str('{:%s%d}' % ('^',20))
            for command in commands:
                result = '\n'.join([result, format_str.format(command)])
            terminal.output(result)
            # action = input().strip().lower()
            # result = bot.handle(action)
            # if action in ['add', 'remove', 'edit']:
            #     bot.book.save("auto_save")
            # terminal.output(result)
        else:
            result = bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
            terminal.output(result)
        if action == 'exit':
            terminal.output('Goodbye!')
            break
        
