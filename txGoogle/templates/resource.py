{% macro capFirst(line) -%}
{{line[0].upper() + line[1:]}}
{%- endmacro %}


class {{capFirst(resourceName)}}(Service):
    def __init__(self, conn, *args, **kwargs):
        super({{capFirst(resourceName)}}, self).__init__(conn, *args, **kwargs)
        {%for k in resourceDict.get('resources', {}).keys()%}
        self.{{k}} = {{capFirst(k)}}(conn)
        {%endfor%}
        {%for v in methodsDict.values()%}
{{v}}
        {%endfor%}
