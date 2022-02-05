class Note:
    def __init__(self, id, title, description, creation_date):
        self.title = title
        self.description = description
        self.creation_date = creation_date
    
    def __str__(self, title, description, creation_date):
        return "Note: " + str(title)

    def get_values(self, id, title, description, creation_date):
        dictionary = {
            "id": id,
            "title": title,
            "description": description,
            "creation_date": creation_date
        }