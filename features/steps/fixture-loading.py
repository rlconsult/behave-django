from behave import then

from test_app.models import BehaveTestModel


@then(u'the fixture should be loaded')
def check_fixtures(context):
    context.test.assertEqual(BehaveTestModel.objects.count(), 1)


@then(u'the fixture for the second scenario should be loaded')
def check_second_fixtures(context):
    context.test.assertEqual(BehaveTestModel.objects.count(), 2)


@then(u'the sequences should be reset')
def check_reset_seqeunces(context):
    context.test.assertEqual(BehaveTestModel.objects.first().pk, 1)
    context.test.assertEqual(BehaveTestModel.objects.last().pk, 2)
