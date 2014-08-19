{% macro capFirst(line) -%}
{{line[0].upper() + line[1:]}}
{%- endmacro %}


class {{capFirst(resourceName)}}(object):
    def __init__(self, conn):
        self._conn = conn
        {%for k in resourceDict.get('resources', {}).keys()%}
        self.{{k}} = {{capFirst(k)}}(conn)
        {%endfor%}
        {%for v in methodsDict.values()%}
{{v}}
        {%endfor%}
