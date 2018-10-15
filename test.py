from Interface import Producer, Consumer
from MessageHandler import Message


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
    main()
##