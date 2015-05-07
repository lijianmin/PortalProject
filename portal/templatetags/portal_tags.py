from django                     import template
from portal.models              import category
from django.template            import resolve_variable, NodeList
from django.contrib.auth.models import Group

register = template.Library()

@register.inclusion_tag('portal/tags/_categories.html')
def categories():
    health_threats = category.objects.filter(master_category = 1)
    categories = category.objects.filter(master_category = 2)
    return {'health_threats':health_threats,'categories':categories}

@register.tag()
def ifusergroup(parser, token):
    """ Check to see if the currently logged in user belongs to a specific
    group. Requires the Django authentication contrib app and middleware.

    Usage: {% ifusergroup Admins %} ... {% endifusergroup %}, or
           {% ifusergroup Admins|Group1|Group2 %} ... {% endifusergroup %}, or
           {% ifusergroup Admins %} ... {% else %} ... {% endifusergroup %}

    """
    try:
        tag, group = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("Tag 'ifusergroup' requires 1 argument.")

    nodelist_true = parser.parse(('else', 'endifusergroup'))
    token = parser.next_token()

    if token.contents == 'else':
        nodelist_false = parser.parse(('endifusergroup',))
        parser.delete_first_token()
    else:
        nodelist_false = NodeList()

    return GroupCheckNode(group, nodelist_true, nodelist_false)


class GroupCheckNode(template.Node):
    def __init__(self, group, nodelist_true, nodelist_false):
        self.group = group
        self.nodelist_true = nodelist_true
        self.nodelist_false = nodelist_false
    def render(self, context):
        user = resolve_variable('user', context)

        if not user.is_authenticated():
            return self.nodelist_false.render(context)

        try:
            for group in self.group.split("|"):

                if Group.objects.get(name=group) in user.groups.all():
                    return self.nodelist_true.render(context)

        except Group.DoesNotExist:
            return self.nodelist_false.render(context)


        return self.nodelist_false.render(context)
