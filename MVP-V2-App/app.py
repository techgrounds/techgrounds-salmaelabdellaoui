#!/usr/bin/env python3

import aws_cdk as cdk

from mvp_v2_app.mvp_v2_app_stack import MvpV2AppStack


app = cdk.App()
MvpV2AppStack(app, "MvpV2AppStack")

app.synth()
