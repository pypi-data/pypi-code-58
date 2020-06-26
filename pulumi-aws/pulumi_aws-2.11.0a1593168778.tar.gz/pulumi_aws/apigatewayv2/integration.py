# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Integration(pulumi.CustomResource):
    api_id: pulumi.Output[str]
    """
    The API identifier.
    """
    connection_id: pulumi.Output[str]
    """
    The ID of the VPC link for a private integration. Supported only for HTTP APIs.
    """
    connection_type: pulumi.Output[str]
    """
    The type of the network connection to the integration endpoint. Valid values: `INTERNET`, `VPC_LINK`. Default is `INTERNET`.
    """
    content_handling_strategy: pulumi.Output[str]
    """
    How to handle response payload content type conversions. Valid values: `CONVERT_TO_BINARY`, `CONVERT_TO_TEXT`. Supported only for WebSocket APIs.
    """
    credentials_arn: pulumi.Output[str]
    """
    The credentials required for the integration, if any.
    """
    description: pulumi.Output[str]
    """
    The description of the integration.
    """
    integration_method: pulumi.Output[str]
    """
    The integration's HTTP method. Must be specified if `integration_type` is not `MOCK`.
    """
    integration_response_selection_expression: pulumi.Output[str]
    """
    The [integration response selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions) for the integration.
    """
    integration_type: pulumi.Output[str]
    """
    The integration type of an integration.
    Valid values: `AWS`, `AWS_PROXY`, `HTTP`, `HTTP_PROXY`, `MOCK`.
    """
    integration_uri: pulumi.Output[str]
    """
    The URI of the Lambda function for a Lambda proxy integration, when `integration_type` is `AWS_PROXY`.
    For an `HTTP` integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.
    """
    passthrough_behavior: pulumi.Output[str]
    """
    The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the `request_templates` attribute.
    Valid values: `WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`. Default is `WHEN_NO_MATCH`. Supported only for WebSocket APIs.
    """
    payload_format_version: pulumi.Output[str]
    """
    The [format of the payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) sent to an integration. Valid values: `1.0`, `2.0`. Default is `1.0`.
    """
    request_templates: pulumi.Output[dict]
    """
    A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.
    """
    template_selection_expression: pulumi.Output[str]
    """
    The [template selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions) for the integration.
    """
    timeout_milliseconds: pulumi.Output[float]
    """
    Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
    """
    def __init__(__self__, resource_name, opts=None, api_id=None, connection_id=None, connection_type=None, content_handling_strategy=None, credentials_arn=None, description=None, integration_method=None, integration_type=None, integration_uri=None, passthrough_behavior=None, payload_format_version=None, request_templates=None, template_selection_expression=None, timeout_milliseconds=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages an Amazon API Gateway Version 2 integration.
        More information can be found in the [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html).

        ## Example Usage
        ### Basic

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigatewayv2.Integration("example",
            api_id=aws_apigatewayv2_api["example"]["id"],
            integration_type="MOCK")
        ```
        ### Lambda Integration

        ```python
        import pulumi
        import pulumi_aws as aws

        example_function = aws.lambda_.Function("exampleFunction",
            code=pulumi.FileArchive("example.zip"),
            handler="index.handler",
            role=aws_iam_role["example"]["arn"],
            runtime="nodejs10.x")
        example_integration = aws.apigatewayv2.Integration("exampleIntegration",
            api_id=aws_apigatewayv2_api["example"]["id"],
            connection_type="INTERNET",
            content_handling_strategy="CONVERT_TO_TEXT",
            description="Lambda example",
            integration_method="POST",
            integration_type="AWS",
            integration_uri=example_function.invoke_arn,
            passthrough_behavior="WHEN_NO_MATCH")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] connection_id: The ID of the VPC link for a private integration. Supported only for HTTP APIs.
        :param pulumi.Input[str] connection_type: The type of the network connection to the integration endpoint. Valid values: `INTERNET`, `VPC_LINK`. Default is `INTERNET`.
        :param pulumi.Input[str] content_handling_strategy: How to handle response payload content type conversions. Valid values: `CONVERT_TO_BINARY`, `CONVERT_TO_TEXT`. Supported only for WebSocket APIs.
        :param pulumi.Input[str] credentials_arn: The credentials required for the integration, if any.
        :param pulumi.Input[str] description: The description of the integration.
        :param pulumi.Input[str] integration_method: The integration's HTTP method. Must be specified if `integration_type` is not `MOCK`.
        :param pulumi.Input[str] integration_type: The integration type of an integration.
               Valid values: `AWS`, `AWS_PROXY`, `HTTP`, `HTTP_PROXY`, `MOCK`.
        :param pulumi.Input[str] integration_uri: The URI of the Lambda function for a Lambda proxy integration, when `integration_type` is `AWS_PROXY`.
               For an `HTTP` integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.
        :param pulumi.Input[str] passthrough_behavior: The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the `request_templates` attribute.
               Valid values: `WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`. Default is `WHEN_NO_MATCH`. Supported only for WebSocket APIs.
        :param pulumi.Input[str] payload_format_version: The [format of the payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) sent to an integration. Valid values: `1.0`, `2.0`. Default is `1.0`.
        :param pulumi.Input[dict] request_templates: A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.
        :param pulumi.Input[str] template_selection_expression: The [template selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions) for the integration.
        :param pulumi.Input[float] timeout_milliseconds: Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if api_id is None:
                raise TypeError("Missing required property 'api_id'")
            __props__['api_id'] = api_id
            __props__['connection_id'] = connection_id
            __props__['connection_type'] = connection_type
            __props__['content_handling_strategy'] = content_handling_strategy
            __props__['credentials_arn'] = credentials_arn
            __props__['description'] = description
            __props__['integration_method'] = integration_method
            if integration_type is None:
                raise TypeError("Missing required property 'integration_type'")
            __props__['integration_type'] = integration_type
            __props__['integration_uri'] = integration_uri
            __props__['passthrough_behavior'] = passthrough_behavior
            __props__['payload_format_version'] = payload_format_version
            __props__['request_templates'] = request_templates
            __props__['template_selection_expression'] = template_selection_expression
            __props__['timeout_milliseconds'] = timeout_milliseconds
            __props__['integration_response_selection_expression'] = None
        super(Integration, __self__).__init__(
            'aws:apigatewayv2/integration:Integration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, api_id=None, connection_id=None, connection_type=None, content_handling_strategy=None, credentials_arn=None, description=None, integration_method=None, integration_response_selection_expression=None, integration_type=None, integration_uri=None, passthrough_behavior=None, payload_format_version=None, request_templates=None, template_selection_expression=None, timeout_milliseconds=None):
        """
        Get an existing Integration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API identifier.
        :param pulumi.Input[str] connection_id: The ID of the VPC link for a private integration. Supported only for HTTP APIs.
        :param pulumi.Input[str] connection_type: The type of the network connection to the integration endpoint. Valid values: `INTERNET`, `VPC_LINK`. Default is `INTERNET`.
        :param pulumi.Input[str] content_handling_strategy: How to handle response payload content type conversions. Valid values: `CONVERT_TO_BINARY`, `CONVERT_TO_TEXT`. Supported only for WebSocket APIs.
        :param pulumi.Input[str] credentials_arn: The credentials required for the integration, if any.
        :param pulumi.Input[str] description: The description of the integration.
        :param pulumi.Input[str] integration_method: The integration's HTTP method. Must be specified if `integration_type` is not `MOCK`.
        :param pulumi.Input[str] integration_response_selection_expression: The [integration response selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions) for the integration.
        :param pulumi.Input[str] integration_type: The integration type of an integration.
               Valid values: `AWS`, `AWS_PROXY`, `HTTP`, `HTTP_PROXY`, `MOCK`.
        :param pulumi.Input[str] integration_uri: The URI of the Lambda function for a Lambda proxy integration, when `integration_type` is `AWS_PROXY`.
               For an `HTTP` integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service.
        :param pulumi.Input[str] passthrough_behavior: The pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the `request_templates` attribute.
               Valid values: `WHEN_NO_MATCH`, `WHEN_NO_TEMPLATES`, `NEVER`. Default is `WHEN_NO_MATCH`. Supported only for WebSocket APIs.
        :param pulumi.Input[str] payload_format_version: The [format of the payload](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.proxy-format) sent to an integration. Valid values: `1.0`, `2.0`. Default is `1.0`.
        :param pulumi.Input[dict] request_templates: A map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. Supported only for WebSocket APIs.
        :param pulumi.Input[str] template_selection_expression: The [template selection expression](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-template-selection-expressions) for the integration.
        :param pulumi.Input[float] timeout_milliseconds: Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000 milliseconds or 29 seconds.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["api_id"] = api_id
        __props__["connection_id"] = connection_id
        __props__["connection_type"] = connection_type
        __props__["content_handling_strategy"] = content_handling_strategy
        __props__["credentials_arn"] = credentials_arn
        __props__["description"] = description
        __props__["integration_method"] = integration_method
        __props__["integration_response_selection_expression"] = integration_response_selection_expression
        __props__["integration_type"] = integration_type
        __props__["integration_uri"] = integration_uri
        __props__["passthrough_behavior"] = passthrough_behavior
        __props__["payload_format_version"] = payload_format_version
        __props__["request_templates"] = request_templates
        __props__["template_selection_expression"] = template_selection_expression
        __props__["timeout_milliseconds"] = timeout_milliseconds
        return Integration(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
