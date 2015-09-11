from django.db          import models
from postman.models     import Message

class Attachment(models.Model):
    message = models.ForeignKey(Message)
    attachment = models.FileField(('attachments'), upload_to="attachments/")

    def __str__(self):
        return str(self.message) + self.attachment.__str__()
