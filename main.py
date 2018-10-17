from Interface import Producer, Consumer
from MessageHandler import Message


class Main:

    consumerRunning = False

    @staticmethod
    def main():
        messageBody1 = Message.Message().initParams('chinook', 'JSON')
        messageBody2 = Message.Message().initParams('chinook', 'XML')
        messageBody3 = Message.Message().initParams('chinook', 'CSV')
        messageBody4 = Message.Message().initParams('chinook', 'TABLE')
        messageBody5 = Message.Message().initParams('', 'StopConsuming')


        print('*** Before send messages *** ')


        Producer.Sender.send(messageBody1)
        Producer.Sender.send(messageBody2)
        Producer.Sender.send([messageBody3,messageBody4])
        #Producer.Sender.send(messageBody4)
        #Producer.Sender.send([messageBody, messageBody, messageBody, messageBody, messageBody])

        Producer.Sender.send(messageBody5)

        print('*** Messages sent *** ')

        print('*** listener running *** ')
        Consumer.Consumer().read()


if __name__ == '__main__':

    Main.main()
