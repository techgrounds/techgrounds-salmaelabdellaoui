#!/usr/bin/env python3

import aws_cdk as cdk

from mvp_v1_app.mvp_v1_app_stack import MvpV1AppStack


app = cdk.App()
MvpV1AppStack(app, "MvpV1AppStack")

app.synth()
