import sys
import pika
from pika import exceptions, BlockingConnection
from DB.DBManager import DBManager
from MessageHandler import IncomingMessageHandler, Message


class Consumer:
    dbConnection = None

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

    # Recieve the message from the queue and move it over to the message handler
    def callback(self, ch, method, properties, body):
        msg = Message.Message().initFromJson(body)

        print('Recieved incoming message')
        print('DB Name: ' + msg.dbName)
        print('Output Type: ' + msg.action)

        if msg.action != "StopConsuming":
            if self.dbConnection is None:
                self.dbConnection = DBManager.getConnection(msg.dbName)
            IncomingMessageHandler.IncomingMessageHandler().HandleMessage(self.dbConnection, msg.action)
        else:
            print('*** consumer ending *** ')
            DBManager.closeConnection(self.dbConnection)
            ch.stop_consuming()

