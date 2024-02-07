import aws_cdk as core
import aws_cdk.assertions as assertions
from mvp_v2_app.mvp_v2_app_stack import MvpV2AppStack


def test_sqs_queue_created():
    app = core.App()
    stack = MvpV2AppStack(app, "mvp-v2-app")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = MvpV2AppStack(app, "mvp-v2-app")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
