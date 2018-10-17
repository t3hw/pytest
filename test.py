from OutputManager import FWFactory
from Interface import Producer, Consumer
from MessageHandler import Message
from DB import DBManager

def main():
    messageBody = Message.Message().initParams('MyDatabase', 'An Awesome File Type')

    print('******************* 0 ')

    Producer.Sender.send(messageBody)
    Producer.Sender.send(messageBody)
    Producer.Sender.send(messageBody)
    Producer.Sender.send([messageBody, messageBody, messageBody, messageBody, messageBody])

    print('******************* 1 ')

    Consumer.Consumer().read()

    print('******************* 2 ')




if __name__ == '__main__':
    a = 1

    dbm = DBManager.DBManager
    results = dbm.executeAllQueries("chinook")
    '''
    #main()
    writer = FWFactory.FWFactory.getFW("CSV")
    writer.write(results)
    writer = FWFactory.FWFactory.getFW("JSON")
    writer.write(results)
    writer = FWFactory.FWFactory.getFW("XML")
    writer.write(results)

    '''
    writer = FWFactory.FWFactory.getFW("TABLE")
    writer.write(results)
    a=1

##