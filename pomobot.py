import argparse
from irc import client
from irc import buffer
import send

irc.client.ServerConnection.buffer_class = irc.buffer.LenientDecodingLineBuffer



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname", help="The hostname of the server to connect to.")
    parser.add_argument("channel", help="The name of the channel to connect to.")
    parser.add_argument("nickname", help="The nickname for the bot to connect as to the server.")
    parser.add_argument("-p", "--port", default=667, type=int, help="The port on which to connect.")
    arguments = parser.parse_args()
    PomoBot(arguments.hostname, arguments.port, arguments.nickname, arguments.channel)

class PomoBot(irc.client.Reactor):
    def __init__(hostname, port, nickname, channel):
        self.nickname = nickname
        self.Send = send.Send()
        self.pomobot = self.server()
        self.pomobot_connection = self.pomobot.connect(hostname, port, nickname)
        self.pomobot_connection.add_global_handler("pubmsg", parse_pubmsg)
        self.pomobot_connection.join(channel)
        self.process_forever()
    
        def parse_pubmsg(connection, event):
            """Parses all messages sent to channel to see if any are meant for
            pomobot. 

            Each command in a module is named cmd_* so that when a dot command
            is given all commands implemented by pomodoro.py can be parsed to 
            see if they share the name of the command. If so the rest of the
            arguments given are passed directly as strings to the associated
            handler function.

            Handler functions return events which are parsed by this function
            and handled in turn. Each event is a list of lists or tuples where 
            each list starts with the type of event as a string and each of these 
            events is handled."""
            if (event.arguments[0][0:len("." + self.nickname + " ")] == 
                "." + self.nickname + " "):
                
                
                                             
        def handle_events(self):
            while not Send.event_queue.empty():
                try:
                    event = Send.event_queue.get(timeout=0.2)
                except Empty:
                    return True
                self.pomobot_connection.privmsg(event[0], event[1])
            return True
        
    
    
