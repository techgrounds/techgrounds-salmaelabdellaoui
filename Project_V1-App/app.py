#!/usr/bin/env python3

import aws_cdk as cdk

from project_v1_app.project_v1_app_stack import ProjectV1AppStack


app = cdk.App()
ProjectV1AppStack(app, "ProjectV1AppStack")

app.synth()
