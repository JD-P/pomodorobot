def process_data(self, sockets):

c.process_data()

class Connection(object):

def process_data(self):

self._process_line(line)

def _process_line(self, line):

event = Event("all_raw_messages", self.get_server_name(), None,
            [line])
        
self._handle_event(event)

def _handle_event(self, event):

fn(self, event)

Writing handlers for events:

Each event type in the irc framework can have associated handlers. 
A function which handles an event should accept as parameters the connection on
which the event occurred and the event itself which is stored as an object with
the following properties:

type -- A string describing the event.

source -- The originator of the event (a nick mask or a server).

target -- The target of the event (a nick or a channel).

arguments -- Any event-specific arguments.

Further information can be found in client.py.