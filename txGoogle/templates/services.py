'''
Warning this is generated code.
Do not edit
'''

from txGoogle.utils import leaveOutNulls


{% for resource in resources %}
class {{ resource.capName }}(object):
    def __init__(self, connection, *args, **kwargs):
        self._conn = connection

    {% for method in resource.methods %}

	{% endfor %}    

{% endfor %}