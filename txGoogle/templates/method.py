{%macro methodFun(dct, indent=16)-%}
    {%for k, v in dct.iteritems() recursive%}
        {%if v is mapping%}
{{''|indent(indent, true)}}'{{k}}': {
{{methodFun(v, indent+4)}}{{''|indent(indent, true)}}},
        {%else%}
{{''|indent(indent, true)}}'{{k}}': {{v}},
        {%endif%}
    {%endfor%}
{%-endmacro%}

    def {{methodName}}(self{%for a in rParams%}, {{a}}{%endfor%}{%for a in oParams%}, {{a}}=None{%endfor%}):
        '''{{methodDict.get('description', '')}}'''
        queryParams = {
            'url': '{{apiDict['baseUrl']}}{{methodDict['path']}}',
            'method': '{{methodDict['httpMethod']}}',
            {%if 'response' in methodDict%}
            'resultType': '{{methodDict['response']['$ref']}}',
            {%else%}
            'resultType': 'empty',
            {%endif%}
            'httpUrlParams': {
                {%for k in apiDict.get('parameters', {})%}
                '{{k}}': {{k}},
                {%endfor%}
                {%for k in methodDict.get('parameters', {})%}
                '{{k}}': {{k}},
                {%endfor%}
            },
            'httpBodyParams': {
{{methodFun(bodyParams)}}            },
        }
        return self._request(queryParams)