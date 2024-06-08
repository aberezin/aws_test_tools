# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
A factory function that returns the stubber for an AWS service, based on the
name of the service that is used by Boto 3.

This factory is used by the make_stubber fixture found in the set of common fixtures.
"""

from aws_test_tools.acm_stubber import AcmStubber
from aws_test_tools.apigateway_stubber import ApiGatewayStubber
from aws_test_tools.apigatewaymanagementapi_stubber import ApiGatewayManagementApiStubber
from aws_test_tools.apigateway_v2_stubber import ApiGatewayV2Stubber
from aws_test_tools.auditmanager_stubber import AuditManagerStubber
from aws_test_tools.autoscaling_stubber import AutoScalingStubber
from aws_test_tools.bedrock_stubber import BedrockStubber
from aws_test_tools.bedrock_runtime_stubber import BedrockRuntimeStubber
from aws_test_tools.bedrock_agent_stubber import BedrockAgentStubber
from aws_test_tools.bedrock_agent_runtime_stubber import BedrockAgentRuntimeStubber
from aws_test_tools.cloudformation_stubber import CloudFormationStubber
from aws_test_tools.cloudfront_stubber import CloudFrontStubber
from aws_test_tools.cloudwatch_stubber import CloudWatchStubber
from aws_test_tools.cloudwatch_logs_stubber import CloudWatchLogsStubber
from aws_test_tools.cognito_idp_stubber import CognitoIdpStubber
from aws_test_tools.comprehend_stubber import ComprehendStubber
from aws_test_tools.config_stubber import ConfigStubber
from aws_test_tools.dynamodb_stubber import DynamoStubber
from aws_test_tools.ec2_stubber import Ec2Stubber
from aws_test_tools.elbv2_stubber import ELBv2Stubber
from aws_test_tools.emr_stubber import EmrStubber
from aws_test_tools.eventbridge_stubber import EventBridgeStubber
from aws_test_tools.glacier_stubber import GlacierStubber
from aws_test_tools.glue_stubber import GlueStubber
from aws_test_tools.iam_stubber import IamStubber
from aws_test_tools.keyspaces_stubber import KeyspacesStubber
from aws_test_tools.kinesis_stubber import KinesisStubber
from aws_test_tools.kinesis_analytics_v2_stubber import KinesisAnalyticsV2Stubber
from aws_test_tools.kms_stubber import KmsStubber
from aws_test_tools.lambda_stubber import LambdaStubber
from aws_test_tools.lookoutvision_stubber import LookoutVisionStubber
from aws_test_tools.organizations_stubber import OrganizationsStubber
from aws_test_tools.pinpoint_stubber import PinpointStubber
from aws_test_tools.pinpoint_email_stubber import PinpointEmailStubber
from aws_test_tools.pinpoint_sms_voice_stubber import PinpointSmsVoiceStubber
from aws_test_tools.polly_stubber import PollyStubber
from aws_test_tools.rdsdata_stubber import RdsDataStubber
from aws_test_tools.rds_stubber import RdsStubber
from aws_test_tools.rekognition_stubber import RekognitionStubber
from aws_test_tools.route53_stubber import Route53Stubber
from aws_test_tools.s3_stubber import S3Stubber
from aws_test_tools.s3control_stubber import S3ControlStubber
from aws_test_tools.secretsmanager_stubber import SecretsManagerStubber
from aws_test_tools.ses_stubber import SesStubber
from aws_test_tools.sns_stubber import SnsStubber
from aws_test_tools.sqs_stubber import SqsStubber
from aws_test_tools.ssm_stubber import SsmStubber
from aws_test_tools.stepfunctions_stubber import StepFunctionsStubber
from aws_test_tools.sts_stubber import StsStubber
from aws_test_tools.support_stubber import SupportStubber
from aws_test_tools.textract_stubber import TextractStubber
from aws_test_tools.transcribe_stubber import TranscribeStubber
from aws_test_tools.medical_imaging_stubber import MedicalImagingStubber
from aws_test_tools.redshift_stubber import RedshiftStubber
from aws_test_tools.redshift_data_stubber import RedshiftDataStubber


class StubberFactoryNotImplemented(Exception):
    pass


def stubber_factory(service_name):
    if service_name == "acm":
        return AcmStubber
    elif service_name == "apigateway":
        return ApiGatewayStubber
    elif service_name == "apigatewaymanagementapi":
        return ApiGatewayManagementApiStubber
    elif service_name == "apigatewayv2":
        return ApiGatewayV2Stubber
    elif service_name == "auditmanager":
        return AuditManagerStubber
    elif service_name == "autoscaling":
        return AutoScalingStubber
    elif service_name == "bedrock":
        return BedrockStubber
    elif service_name == "bedrock-runtime":
        return BedrockRuntimeStubber
    elif service_name == "bedrock-agent":
        return BedrockAgentStubber
    elif service_name == "bedrock-agent-runtime":
        return BedrockAgentRuntimeStubber
    elif service_name == "cloudformation":
        return CloudFormationStubber
    elif service_name == "cloudfront":
        return CloudFrontStubber
    elif service_name == "cloudwatch":
        return CloudWatchStubber
    elif service_name == "logs":
        return CloudWatchLogsStubber
    elif service_name == "cognito-idp":
        return CognitoIdpStubber
    elif service_name == "comprehend":
        return ComprehendStubber
    elif service_name == "config":
        return ConfigStubber
    elif service_name == "dynamodb":
        return DynamoStubber
    elif service_name == "ec2":
        return Ec2Stubber
    elif service_name == "elbv2":
        return ELBv2Stubber
    elif service_name == "emr":
        return EmrStubber
    elif service_name == "events":
        return EventBridgeStubber
    elif service_name == "glacier":
        return GlacierStubber
    elif service_name == "glue":
        return GlueStubber
    elif service_name == "iam":
        return IamStubber
    elif service_name == "keyspaces":
        return KeyspacesStubber
    elif service_name == "kinesis":
        return KinesisStubber
    elif service_name == "kinesisanalyticsv2":
        return KinesisAnalyticsV2Stubber
    elif service_name == "kms":
        return KmsStubber
    elif service_name == "lambda":
        return LambdaStubber
    elif service_name == "lookoutvision":
        return LookoutVisionStubber
    elif service_name == "medical-imaging":
        return MedicalImagingStubber
    elif service_name == "organizations":
        return OrganizationsStubber
    elif service_name == "pinpoint":
        return PinpointStubber
    elif service_name == "pinpoint-email":
        return PinpointEmailStubber
    elif service_name == "pinpoint-sms-voice":
        return PinpointSmsVoiceStubber
    elif service_name == "polly":
        return PollyStubber
    elif service_name == "rds":
        return RdsStubber
    elif service_name == "rds-data":
        return RdsDataStubber
    elif service_name == "redshift":
        return RedshiftStubber
    elif service_name == "redshift-data":
        return RedshiftDataStubber
    elif service_name == "rekognition":
        return RekognitionStubber
    elif service_name == "route53":
        return Route53Stubber
    elif service_name == "s3":
        return S3Stubber
    elif service_name == "s3control":
        return S3ControlStubber
    elif service_name == "secretsmanager":
        return SecretsManagerStubber
    elif service_name == "ses":
        return SesStubber
    elif service_name == "sns":
        return SnsStubber
    elif service_name == "sqs":
        return SqsStubber
    elif service_name == "ssm":
        return SsmStubber
    elif service_name == "stepfunctions":
        return StepFunctionsStubber
    elif service_name == "sts":
        return StsStubber
    elif service_name == "support":
        return SupportStubber
    elif service_name == "textract":
        return TextractStubber
    elif service_name == "transcribe":
        return TranscribeStubber
    else:
        raise StubberFactoryNotImplemented(
            "If you see this exception, it probably means that you forgot to add "
            "a new stubber to stubber_factory.py."
        )
