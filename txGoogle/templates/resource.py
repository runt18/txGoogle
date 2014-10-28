{% macro capFirst(line) -%}
{{line[0].upper() + line[1:]}}
{%- endmacro %}


class {{capFirst(resourceName)}}(Resource):
    def __init__(self, service, conn, *args, **kwargs):
        super({{capFirst(resourceName)}}, self).__init__(service, conn, *args, **kwargs)
        {%for k in resourceDict.get('resources', {}).keys()%}
        self.{{k}} = {{capFirst(k)}}(service, conn)
        {%endfor%}
        {%for v in methodsDict.values()%}
{{v}}
        {%endfor%}
