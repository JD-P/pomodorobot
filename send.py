import queue

class Send():
    """Prototype send module that can be later ported to auditbot."""
    def __init__(self, nickname, ideal_width=80):
        self.nickname = nickname
        self.ideal_width = ideal_width
        self.event_queue = queue.Queue()

    def safe_write(self, target, message):
        """Create a set of events from a string <message> to send to <target>.
        Splits lines as needed to make sure that message is not truncated by IRC
        length limits."""
        pass
    
    def write(self, target, message):
        """Low level write to a target, creating a single send event to <target>
        with <message> as the body."""
        self.event_queue.put((target, message))
