import sys
import pika
from pika import exceptions


class Sender:

    # open a connection if it was not yet initilized
    @staticmethod
    def initConnection():
        try:
            if Sender.connection.is_closed:
                Sender.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        except AttributeError:
            type, value, traceback = sys.exc_info()
            Sender.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    # close the connection if it is was opened
    @staticmethod
    def closeConnection():
        try:
            Sender.connection
        except AttributeError:
            pass
        else:
            Sender.connection.close()

    @staticmethod
    def send(messages):
        errCode = 0

        try:
            Sender.initConnection()

            channel = Sender.connection.channel()

            queueName = 'testQueue'
            channel.queue_declare(queue=queueName)

            if isinstance(messages, list):
                for singleMessage in messages:
                    channel.basic_publish(exchange='',
                                          routing_key=queueName,
                                          body=singleMessage.toJson())
            else:
                channel.basic_publish(exchange='',
                                      routing_key=queueName,
                                      body=messages.toJson())

        except exceptions.AMQPError:
            type, value, traceback = sys.exc_info()

            print('Error sending message %s: ' % (value.args[0]))

            errCode = -99

        Sender.closeConnection()

        # successful execution
        return errCode
