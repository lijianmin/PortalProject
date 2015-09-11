from django.shortcuts               import render, get_object_or_404, render_to_response
from postman_attachments.models     import Attachment
from django.core.files.uploadedfile import UploadedFile
from django.views.decorators.csrf   import csrf_exempt
from django.http                    import HttpResponse, HttpResponseBadRequest
from django.conf                    import settings
