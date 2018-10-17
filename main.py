from OutputManager import FWFactory
from Interface import Producer, Consumer
from MessageHandler import Message
from DB import DBManager

def main():
    messageBody1 = Message.Message().initParams('chinook', 'JSON')
    messageBody2 = Message.Message().initParams('chinook', 'XML')
    messageBody3 = Message.Message().initParams('chinook', 'CSV')
    messageBody4 = Message.Message().initParams('chinook', 'TABLE')
    print('*** Before send messages *** ')

    Producer.Sender.send(messageBody1)
    Producer.Sender.send(messageBody2)
    Producer.Sender.send([messageBody3,messageBody4])
    #Producer.Sender.send(messageBody4)
    #Producer.Sender.send([messageBody, messageBody, messageBody, messageBody, messageBody])

    print('*** Messages sent *** ')

    Consumer.Consumer().read()

    print('*** end  *** ')




if __name__ == '__main__':

    main()
