from postman_attachments.models        import Attachment
from django 					       import forms
from postman.forms                     import *
from django.conf                       import settings
from django.db                         import IntegrityError, transaction
from multiupload.fields                import MultiFileField
from postman_attachments.models        import Attachment
from postman.models                    import Message

allow_copies = not getattr(settings, 'POSTMAN_DISALLOW_COPIES_ON_REPLY', False)

class FullWriteAttachmentForm(WriteForm):

    print('FullWriteAttachmentForm Loaded')

    """The complete reply form."""
    if allow_copies:
        recipients = CommaSeparatedUserField(label=(("Additional recipients"), ("Additional recipient")), required=False)

    files = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    class Meta(BaseWriteForm.Meta):
        fields = (['recipients'] if allow_copies else []) + ['subject', 'body','files',]

    @transaction.atomic
    def save(self, *args, **kwargs):
        instance = super(FullWriteAttachmentForm, self).save(self.recipient, *args, **kwargs)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(attachment=each, message=instance)

        return instance


class FullReplyAttachmentForm(BaseReplyForm):

    print('FullReplyAttachmentForm Loaded')

    """The complete reply form."""
    if allow_copies:
        recipients = CommaSeparatedUserField(label=(("Additional recipients"), ("Additional recipient")), required=False)

    files = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    class Meta(BaseReplyForm.Meta):
        fields = (['recipients'] if allow_copies else []) + ['subject', 'body']

    @transaction.atomic
    def save(self, recipient=None, parent=None, auto_moderators=[], *args, **kwargs):
        print(self)
        instance = super(FullReplyAttachmentForm, self).save(self.recipient, *args, **kwargs)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(attachment=each, message=self.instance)
