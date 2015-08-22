pkg_info = {"dependencies":[{"name":"send", "version":"1.0+", "type":"mandatory"}]} 

class Pomodoro():
    """A pomodoro timer.

    Pomodoro registers what users in a channel are working on, keeps track of
    pomodoros issued by users, and keeps track of pomodoro start and stop times."""
    def __init__(self):
        self.pomodoros = []
        self.register = PomodoroRegister()

    def pomo(self):
        pass

    def cmd_view_table(self, event):
        """Send a register table to the user or channel specified by target."""
        formatted_table = self.register.format_table()
        send_events = []
        for line in formatted_table:
            send_events.append(("send", event.source, line))
        return send_events 

    def add_pomodoro(self, split):
        """Add a pomodoro to the stack.
        Keyword arguments:
            split | A tuple of the form (working, break) where working is how many
                    minutes you will spend working and break is how many minutes
                    are in the break.
        """
        if split[0] + split[1] > 60:
            #Create event to tell user that they entered invalid split.

        elif self.pomodoros:
            self.pomodoros.insert(0, split)
        else:
            self.pomodoros.append(split)

    def pomodoro_break(self):
        """Pull current pomodoro from stack and start the break period of a pomodoro."""
        split = self.pomodoros.pop()
        break_ = split[1]
        # IMPLEMENT: However we want to wait X minutes for the break
        self.pomodoro_start()

    def pomodoro_start(self):
        """Start the next pomodoro on the stack."""
        # IMPLEMENT: Schedule an event working minutes in the future for pomodoro
        # to end at and break to start.

    def send_pomodoros(self, target):
        """Send a list of pomodoros on the stack to the user or channel specified by target."""
        # IMPLEMENT

    def clear_pomodoros(self):
        """Clear all pomodoros on the stack besides the current one."""
        for pomodoro in self.pomodoros:
            if pomodoro is not self.pomodoros[0]:
                self.pomodoros.remove(pomodoro)

class PomodoroRegister():
    """A register table for users in channel to register their project to the timer with."""
    def __init__(self):
        self.working = {}

    def register(self, user, task):
        """Register a user as working on task for this Pomodoro."""
        self.working[user] = task
        # IMPLEMENT: Send back a confirmation to the user who registered.
        # IDEA: Perhaps limit the length of the string a user can use to describe their pomodoro?
    
    def working_on(self, user):
        """Return the task that a user is registered as working on."""
        return self.working[user]
    
    def get_table(self):
        """Return the entire table of user:task pairs."""
        return self.working

    def format_table(self):
        """Return a formatted ready-to-send table.

        Each line of the formatted table is 80 characters. The format is to start
        with the name of the user and then a colon seperating their task and a space.
        If the task is longer than the rest of the line it's truncated so that three
        ellipsis can be printed at the end instead and the task is continued onto
        the next line.
        
        Example: JD: Working on pomodoro bot.
        Example: JD: Working on the format_table feature of the pomodoro bot ...
        which allows one to have a table of what users are working on sent to...
        themselves."""
        table_lines = []
        for user in self.working.keys():
            user_task = user + ": " + self.working[user]
            while user_task:
                if len(user_task) >= 80:
                    table_lines.append(user_task[0:77] + "...")
                    user_task = user_task[77:]
                else:
                    table_lines.append(user_task)
                    user_task = ''
            return table_lines
        

        
