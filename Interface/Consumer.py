import sys
import pika
from pika import exceptions, BlockingConnection
from MessageHandler import IncomingMessageHandler, Message


class Consumer:
    # Recieve the message from the queue and move it over to the message handler
    def callback(self, ch, method, properties, body):
        msg = Message.Message().initFromJson(body)

        if msg.action == "StopConsuming":
            print('*** consumer ending *** ')
            ch.stop_consuming()
        else:
            IncomingMessageHandler.IncomingMessageHandler().HandleMessage(msg.dbName,msg.action)

    def read(self):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel: BlockingConnection = connection.channel()

            queueName = 'testQueue'
            channel.basic_consume(self.callback,
                                  queue=queueName,
                                  no_ack=True)

            print('*** Waiting for messages. ***')

            channel.start_consuming()

        except exceptions.AMQPError:
            type, value, traceback = sys.exc_info()
            print('Error receiving message %s: ' % (value.args[0]))
        # close the connection if it is was opened
        finally:
            connection.close()