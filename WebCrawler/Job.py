class Job(object):
    def __init__(self, title="", company="", location=""):
        self.title = title
        self.company = company
        self.location = location
    
    def make_Job(title, company, location):
       return Job(title, company, location)

    def echo(self):
        print(self.title)
        print(self.company)
        print(self.location)