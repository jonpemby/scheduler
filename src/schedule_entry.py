class ScheduleEntry:
    def __init__(self, company, depart, ret, time_format='%a %b %d'):
        """
        Data object to handle a schedule entry
        :param company: interviewing company
        :param depart: departure time
        :param ret: return time
        """
        self.company = company
        self.depart = depart
        self.ret = ret
        self.time_format = time_format

    def set_format(self, time_format):
        """
        Set the format of the pretty formatted times
        :param time_format: format string for times
        :return: self
        """
        self.time_format = time_format
        return self

    def __repr__(self):
        """
        Returns the string representation of the schedule entry
        :return: str
        """
        return "{}\n" \
               "Leave: {}\n" \
               "Return: {}".format(self.company, self.formatted_departure(), self.formatted_return())

    def formatted_departure(self):
        """
        Returns a pretty formatted string for departure time
        :return: str
        """
        return self.depart.strftime(self.time_format)

    def formatted_return(self):
        """
        Returns a pretty formatted string for return time
        :return: str
        """
        return self.ret.strftime(self.time_format)
