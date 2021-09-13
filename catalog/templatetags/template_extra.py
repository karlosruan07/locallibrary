
from django import template

register = template.Library()

@register.inclusion_tag('catalog/paginacao.html', takes_context=True)
def paginacao(context):
    return{
        'paginator':context['paginator'],
        'request':context['request'],
        'page_obj':context['page_obj']
    }

