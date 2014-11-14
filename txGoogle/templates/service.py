{% macro capFirst(line) -%}
{{line[0].upper() + line[1:]}}
{%- endmacro %}


class {{capFirst(resourceName)}}(GoogleService):
    '''{{resourceDict.get('description', '')}}'''
    _DEFAULT_SCOPES = {{scopes}}

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super({{capFirst(resourceName)}}, self).__init__(conn, *args, **kwargs)
        {%for k in resourceDict.get('resources', {}).keys()%}
        self.{{k}} = {{capFirst(k)}}(self, conn, *args, **kwargs)
        {%endfor%}
        {%for v in methodsDict.values()%}
{{v}}
        {%endfor%}
