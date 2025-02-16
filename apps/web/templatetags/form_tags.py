from django import template
from django.utils.safestring import mark_safe


register = template.Library()



@register.simple_tag
def render_form_fields(form):
    rendered_values = [render_field(form[field]) for field in form.fields]
    return mark_safe(''.join(rendered_values))


@register.simple_tag
def render_field(form_field):
    # multi-css support for forms
    render_function = {
        'select': render_select_input,
        'checkbox': render_checkbox_input,
    }.get(form_field.widget_type, render_text_input)
    return render_function(form_field)



@register.simple_tag
def render_text_input(form_field):
    TEXT_INPUT_TEMPLATE = """<div class="field">
      <label class="label">{{ form_field.label }}</label>
      <div class="control">
        {{ form_field }}
      </div>
      <div class="help">{{ form_field.help_text|safe }}</div>
      {{ form_field.errors }}
    </div>
    """
    return _render_field(TEXT_INPUT_TEMPLATE, form_field)


@register.simple_tag
def render_select_input(form_field):
    SELECT_INPUT_TEMPLATE = """<div class="field">
      <label class="label">{{ form_field.label }}</label>
      <div class="control">
        <div class="select">
          {{ form_field }}
        </div>
      </div>
      <div class="help">{{ form_field.help_text|safe }}</div>
      {{ form_field.errors }}
    </div>
    """
    return _render_field(SELECT_INPUT_TEMPLATE, form_field)


@register.simple_tag
def render_checkbox_input(form_field):
    CHECKBOX_INPUT_TEMPLATE = """<div class="field">
      <div class="control">
        <label class="checkbox">
          {{ form_field }}
          {{ form_field.label }}
        </label>
      </div>
      <div class="help">{{ form_field.help_text|safe }}</div>
      {{ form_field.errors }}
    </div>
    """
    return _render_field(CHECKBOX_INPUT_TEMPLATE, form_field)


def _render_field(template_text, form_field):
    if not form_field.is_hidden:
        template_object = template.Template(template_text)
    else:
        template_object = template.Template('{{ form_field }}')
    context = template.Context({"form_field": form_field})
    return template_object.render(context)
