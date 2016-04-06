from behave import when, then
from django.core.urlresolvers import reverse

from test_app.models import BehaveTestModel


@when(u'I call get_url() without arguments')
def without_args(context):
    context.result = context.get_url()


@when(u'I call get_url("{url_path}") with an absolute path')
def path_arg(context, url_path):
    context.result = context.get_url(url_path)


@when(u'I call get_url("{view_name}") with a view name')
def view_arg(context, view_name):
    context.result = context.get_url(view_name)


@when(u'I call get_url(model) with a model instance')
def model_arg(context):
    context.model = BehaveTestModel(name='Foo', number=3)
    context.result = context.get_url(context.model)


@then(u'it returns the value of base_url')
def is_baseurl_value(context):
    context.test.assertEquals(context.result, context.base_url)


@then(u'the result is the base_url with "{url_path}" appended')
def baseurl_plus_path(context, url_path):
    context.test.assertEquals(context.result, context.base_url + url_path)


@then(u'the result is the base_url with reverse("{view_name}") appended')
def baseurl_plus_reverse(context, view_name):
    path = reverse(view_name)
    assert len(path) > 0, "Non-empty path expected"
    context.test.assertEquals(context.result, context.base_url + path)


@then(u'the result is the base_url with model.get_absolute_url() appended')
def baseurl_plus_absolute_url(context):
    path = context.model.get_absolute_url()
    assert len(path) > 0, "Non-empty path expected"
    context.test.assertEquals(context.result, context.base_url + path)


@then(u'this returns the same result as get_url(reverse("{view_name}"))')
def explicit_reverse(context, view_name):
    path = reverse(view_name)
    context.test.assertEquals(context.result, context.get_url(path))


@then(u'this returns the same result as get_url(model.get_absolute_url())')
def get_model_url(context):
    path = context.model.get_absolute_url()
    context.test.assertEquals(context.result, context.get_url(path))
