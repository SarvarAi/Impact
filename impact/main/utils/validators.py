from datetime import datetime

from ..models import Visitors, VisitorsTime


class VisitingValidator:
    """Class creates or adds visiting time of visitor by ip"""

    def __init__(self, request):
        """Constructor that takes argument request from the web-app
        and create visitor_ip for further use inner the class"""
        self.request = request
        self.visitor_ip = None

    def _is_visited_user(self):
        """Method _is_visited_user returns True or False it answers to
         the question is the visitor new or he/she was in our website"""
        self.visitor_ip = self.request.META.get('REMOTE_ADDR')

        try:
            Visitors.objects.get(ip_address=self.visitor_ip)
            return True
        except:
            return False

    def _add_times(self):
        """Method that adds time by visitor_ip and uses library datetime"""
        visitor = Visitors.objects.get(ip_address=self.visitor_ip)
        time = VisitorsTime.objects.create(Visitors=visitor, time=datetime.now())

        visitor.visited_times += 1

        time.save()
        visitor.save()

    def check(self):
        """Check is the main method of this class that we use to call it
        and all other methods are bounded to it"""
        is_new = self._is_visited_user()
        if not is_new:
            visitor, is_visitor_exist = Visitors.objects.get_or_create(ip_address=self.visitor_ip, visited_times=1)
            time, is_created_time = VisitorsTime.objects.get_or_create(Visitors=visitor, time=datetime.now())

            visitor.save()
            time.save()
        else:
            self._add_times()
