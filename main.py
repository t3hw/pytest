from Interface import Producer, Consumer
from MessageHandler import Message


class Main:

    consumerRunning = False

    @staticmethod
    def main():
        messageBody1 = Message.Message().initParams('chinook', 'DB', 'JSON')
        messageBody2 = Message.Message().initParams('chinook2', 'DB', 'XML')
        messageBody3 = Message.Message().initParams('InputFile1', 'JSON', 'DB')
        messageBody4 = Message.Message().initParams('InputFile1', 'JSON', 'CSV')
        messageBody5 = Message.Message().initParams('', 'StopConsuming', '')


        print('*** Before send messages *** ')


        Producer.Sender.send(messageBody1)
        Producer.Sender.send(messageBody2)
        Producer.Sender.send([messageBody3,messageBody4])
        Producer.Sender.send(messageBody5)
        #Producer.Sender.send([messageBody, messageBody, messageBody, messageBody, messageBody])

        print('*** Messages sent *** ')

        print('*** listener running *** ')
        Consumer.Consumer().read()

    @staticmethod
    def fibonacci(n):

        curr = 1
        prev = 1

        if n == 0:
            return 0
        elif n > 2:
            i = 2
            while i < n:
                next = curr + prev
                prev = curr
                curr = next
                i += 1

        return curr

    @staticmethod
    def fibonacci_rec(n):
        if n < 2:
            return n
        else:
            return Main.fibonacci_rec(n - 1) + Main.fibonacci_rec(n - 2)

    @staticmethod
    def runFib():
        print(Main.fibonacci_rec(0))
        print(Main.fibonacci_rec(1))
        print(Main.fibonacci_rec(2))
        print(Main.fibonacci_rec(3))
        print(Main.fibonacci_rec(4))
        print(Main.fibonacci_rec(5))
        print(Main.fibonacci(6))
        print(Main.fibonacci(7))
        print(Main.fibonacci(8))
        print(Main.fibonacci(9))
        print(Main.fibonacci(10))

if __name__ == '__main__':

    Main.main()

    Main.runFib()

