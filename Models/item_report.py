from abc import ABC, abstractmethod



class ItemReport(ABC):
    def __init__(self, report_id, title, description, category, location, date):
        self._report_id = report_id
        self.title = title
        self.description = description
        self.category = category
        self.location = location
        self.date = date

    @abstractmethod
    def get_details(self):
        pass




class LostReport(ItemReport):
    def __init__(self, last_seen_date, **kwargs):
        super().__init__(**kwargs)
        self.last_seen_date = last_seen_date

    def get_details(self):
        a = f"""\tLOST ITEM REPORT
        
\t{self.title}
        
REPORT ID: {self._report_id}
        
DESCRIPTION: {self.description}
        
CATEGORY: {self.category}
        
LOCATION: {self.location}
        
DATE: {self.date}
"""
        b = f"""
LAST SEEN DATE: {self.last_seen_date}
"""
        a = a + b
        return a



class FoundReport(ItemReport):
    def __init__(self, found_date, **kwargs):
        super().__init__(**kwargs)
        self.found_date = found_date
        

    def get_details(self):
        a = f"""\tLOST ITEM REPORT
    
\t{self.title}
    
REPORT ID: {self._report_id}
        
DESCRIPTION: {self.description}
    
CATEGORY: {self.category}
    
LOCATION: {self.location}
    
DATE: {self.date}
"""

        b = f"""
FOUND DATE: {self.found_date}
"""
        a = a + b
        return a






# b = LostReport(
#     last_seen_date = "12-Oct-2026",
#     report_id = 123,
#     title = "Lost Bag", 
#     description ="lost leather bag in mall near a shop", 
#     category ="Bags", 
#     location = "near Dr.Fixit", 
#     date = "12-Oct-2026",
# )


# c = FoundReport(
#     found_date = "18-Oct-2026",
#     report_id = 123,
#     title = "Lost Bag", 
#     description ="lost leather bag in mall near a shop", 
#     category ="Bags", 
#     location = "near Dr.Fixit", 
#     date = "12-Oct-2026"
# )


# l1 = [b,c]

# for i in l1:
#     print(i.get_details())