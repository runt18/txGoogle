


'''
Warning this is generated code.
Do not edit
'''

from txGoogle.utils import leaveOutNulls

'''
{% for resource in resources %}
class {{ resource.capName }}(object):
    def __init__(self, connection, *args, **kwargs):
        self._conn = connection

    {% for method in resource.methods %}

	{% endfor %}    

{% endfor %}
'''

{% for resource in apiDict recursive %}
class {{ resource }}(object):
    def __init__(self, connection, *args, **kwargs):
        self._conn = connection
    {% for method in resource.methods %}
    {% endfor %}    
{% endfor %}

asdasdasdasdasdasdasdasdasdasd

{% for item, values in apiDict.iteritems() recursive %}
{{item}}{{values}}
    {% if item == "resources" %}
        {% for resource in values %}
            class {{ resource }}(object):
                def __init__(self, connection, *args, **kwargs):
                    self._conn = connection
        {% endfor %}
    {% endif %}
{% endfor %}

