from rollyourown import seo
from django.utils import hashcompat

class MyMetadata(seo.Metadata):
    title       = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords    = seo.KeywordTag()
    heading     = seo.Tag(name="h1")