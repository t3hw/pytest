import sys
import pika
from pika import exceptions
from MessageHandler import IncomingMessageHandler, Message


class Consumer:
    # Recieve the message from the queue and move it over to the message handler
    def callback(self, ch, method, properties, body):
        msg = Message.Message().initFromJson(body)

        IncomingMessageHandler.IncomingMessageHandler().HandleMessage(msg)

    def read(self):
        errCode = 0

        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()

            queueName = 'testQueue'
            channel.basic_consume(self.callback,
                                  queue=queueName,
                                  no_ack=True)

            print(' [*] Waiting for messages. To exit press CTRL+C')

            channel.start_consuming()

        except exceptions.AMQPError:
            type, value, traceback = sys.exc_info()
            print('Error receiving message %s: ' % (value.args[0]))

            errCode = -99

        # close the connection if it is was opened
        try:
            connection
        except NameError:
            pass
        else:
            connection.close()

        # successful execution
        return errCode
