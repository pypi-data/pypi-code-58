# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Listener(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) of the target group.
    """
    certificate_arn: pulumi.Output[str]
    """
    The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the `lb.ListenerCertificate` resource.
    """
    default_actions: pulumi.Output[list]
    """
    An Action block. Action blocks are documented below.

      * `authenticateCognito` (`dict`)
        * `authenticationRequestExtraParams` (`dict`) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
        * `onUnauthenticatedRequest` (`str`) - The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
        * `scope` (`str`) - The set of user claims to be requested from the IdP.
        * `sessionCookieName` (`str`) - The name of the cookie used to maintain session information.
        * `sessionTimeout` (`float`) - The maximum duration of the authentication session, in seconds.
        * `userPoolArn` (`str`) - The ARN of the Cognito user pool.
        * `userPoolClientId` (`str`) - The ID of the Cognito user pool client.
        * `userPoolDomain` (`str`) - The domain prefix or fully-qualified domain name of the Cognito user pool.

      * `authenticateOidc` (`dict`)
        * `authenticationRequestExtraParams` (`dict`) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
        * `authorizationEndpoint` (`str`) - The authorization endpoint of the IdP.
        * `client_id` (`str`) - The OAuth 2.0 client identifier.
        * `client_secret` (`str`) - The OAuth 2.0 client secret.
        * `issuer` (`str`) - The OIDC issuer identifier of the IdP.
        * `onUnauthenticatedRequest` (`str`) - The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
        * `scope` (`str`) - The set of user claims to be requested from the IdP.
        * `sessionCookieName` (`str`) - The name of the cookie used to maintain session information.
        * `sessionTimeout` (`float`) - The maximum duration of the authentication session, in seconds.
        * `tokenEndpoint` (`str`) - The token endpoint of the IdP.
        * `userInfoEndpoint` (`str`) - The user info endpoint of the IdP.

      * `fixedResponse` (`dict`) - Information for creating an action that returns a custom HTTP response. Required if `type` is `fixed-response`.
        * `content_type` (`str`) - The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.
        * `messageBody` (`str`) - The message body.
        * `status_code` (`str`) - The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.

      * `forward` (`dict`) - Information for creating an action that distributes requests among one or more target groups. Specify only if `type` is `forward`. If you specify both `forward` block and `target_group_arn` attribute, you can specify only one target group using `forward` and it must be the same target group specified in `target_group_arn`.
        * `stickiness` (`dict`) - The target group stickiness for the rule.
          * `duration` (`float`) - The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).
          * `enabled` (`bool`) - Indicates whether target group stickiness is enabled.

        * `targetGroups` (`list`) - One or more target groups block.
          * `arn` (`str`) - The Amazon Resource Name (ARN) of the target group.
          * `weight` (`float`) - The weight. The range is 0 to 999.

      * `order` (`float`)
      * `redirect` (`dict`) - Information for creating a redirect action. Required if `type` is `redirect`.
        * `host` (`str`) - The hostname. This component is not percent-encoded. The hostname can contain `#{host}`. Defaults to `#{host}`.
        * `path` (`str`) - The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to `/#{path}`.
        * `port` (`str`) - The port. Specify a value from `1` to `65535` or `#{port}`. Defaults to `#{port}`.
        * `protocol` (`str`) - The protocol. Valid values are `HTTP`, `HTTPS`, or `#{protocol}`. Defaults to `#{protocol}`.
        * `query` (`str`) - The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?". Defaults to `#{query}`.
        * `status_code` (`str`) - The HTTP redirect code. The redirect is either permanent (`HTTP_301`) or temporary (`HTTP_302`).

      * `target_group_arn` (`str`) - The ARN of the Target Group to which to route traffic. Specify only if `type` is `forward` and you want to route to a single target group. To route to one or more target groups, use a `forward` block instead.
      * `type` (`str`) - The type of routing action. Valid values are `forward`, `redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.
    """
    load_balancer_arn: pulumi.Output[str]
    """
    The ARN of the load balancer.
    """
    port: pulumi.Output[float]
    """
    The port on which the load balancer is listening.
    """
    protocol: pulumi.Output[str]
    """
    The protocol for connections from clients to the load balancer. Valid values are `TCP`, `TLS`, `UDP`, `TCP_UDP`, `HTTP` and `HTTPS`. Defaults to `HTTP`.
    """
    ssl_policy: pulumi.Output[str]
    """
    The name of the SSL Policy for the listener. Required if `protocol` is `HTTPS` or `TLS`.
    """
    def __init__(__self__, resource_name, opts=None, certificate_arn=None, default_actions=None, load_balancer_arn=None, port=None, protocol=None, ssl_policy=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Load Balancer Listener resource.

        > **Note:** `alb.Listener` is known as `lb.Listener`. The functionality is identical.

        ## Example Usage
        ### Forward Action

        ```python
        import pulumi
        import pulumi_aws as aws

        front_end_load_balancer = aws.lb.LoadBalancer("frontEndLoadBalancer")
        front_end_target_group = aws.lb.TargetGroup("frontEndTargetGroup")
        front_end_listener = aws.lb.Listener("frontEndListener",
            certificate_arn="arn:aws:iam::187416307283:server-certificate/test_cert_rab3wuqwgja25ct3n4jdj2tzu4",
            default_actions=[{
                "target_group_arn": front_end_target_group.arn,
                "type": "forward",
            }],
            load_balancer_arn=front_end_load_balancer.arn,
            port="443",
            protocol="HTTPS",
            ssl_policy="ELBSecurityPolicy-2016-08")
        ```
        ### Redirect Action

        ```python
        import pulumi
        import pulumi_aws as aws

        front_end_load_balancer = aws.lb.LoadBalancer("frontEndLoadBalancer")
        front_end_listener = aws.lb.Listener("frontEndListener",
            default_actions=[{
                "redirect": {
                    "port": "443",
                    "protocol": "HTTPS",
                    "status_code": "HTTP_301",
                },
                "type": "redirect",
            }],
            load_balancer_arn=front_end_load_balancer.arn,
            port="80",
            protocol="HTTP")
        ```
        ### Fixed-response Action

        ```python
        import pulumi
        import pulumi_aws as aws

        front_end_load_balancer = aws.lb.LoadBalancer("frontEndLoadBalancer")
        front_end_listener = aws.lb.Listener("frontEndListener",
            default_actions=[{
                "fixedResponse": {
                    "content_type": "text/plain",
                    "messageBody": "Fixed response content",
                    "status_code": "200",
                },
                "type": "fixed-response",
            }],
            load_balancer_arn=front_end_load_balancer.arn,
            port="80",
            protocol="HTTP")
        ```
        ### Authenticate-cognito Action

        ```python
        import pulumi
        import pulumi_aws as aws

        front_end_load_balancer = aws.lb.LoadBalancer("frontEndLoadBalancer")
        front_end_target_group = aws.lb.TargetGroup("frontEndTargetGroup")
        pool = aws.cognito.UserPool("pool")
        client = aws.cognito.UserPoolClient("client")
        domain = aws.cognito.UserPoolDomain("domain")
        front_end_listener = aws.lb.Listener("frontEndListener",
            default_actions=[
                {
                    "authenticateCognito": {
                        "userPoolArn": pool.arn,
                        "userPoolClientId": client.id,
                        "userPoolDomain": domain.domain,
                    },
                    "type": "authenticate-cognito",
                },
                {
                    "target_group_arn": front_end_target_group.arn,
                    "type": "forward",
                },
            ],
            load_balancer_arn=front_end_load_balancer.arn,
            port="80",
            protocol="HTTP")
        ```
        ### Authenticate-oidc Action

        ```python
        import pulumi
        import pulumi_aws as aws

        front_end_load_balancer = aws.lb.LoadBalancer("frontEndLoadBalancer")
        front_end_target_group = aws.lb.TargetGroup("frontEndTargetGroup")
        front_end_listener = aws.lb.Listener("frontEndListener",
            default_actions=[
                {
                    "authenticateOidc": {
                        "authorizationEndpoint": "https://example.com/authorization_endpoint",
                        "client_id": "client_id",
                        "client_secret": "client_secret",
                        "issuer": "https://example.com",
                        "tokenEndpoint": "https://example.com/token_endpoint",
                        "userInfoEndpoint": "https://example.com/user_info_endpoint",
                    },
                    "type": "authenticate-oidc",
                },
                {
                    "target_group_arn": front_end_target_group.arn,
                    "type": "forward",
                },
            ],
            load_balancer_arn=front_end_load_balancer.arn,
            port="80",
            protocol="HTTP")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_arn: The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the `lb.ListenerCertificate` resource.
        :param pulumi.Input[list] default_actions: An Action block. Action blocks are documented below.
        :param pulumi.Input[str] load_balancer_arn: The ARN of the load balancer.
        :param pulumi.Input[float] port: The port on which the load balancer is listening.
        :param pulumi.Input[str] protocol: The protocol for connections from clients to the load balancer. Valid values are `TCP`, `TLS`, `UDP`, `TCP_UDP`, `HTTP` and `HTTPS`. Defaults to `HTTP`.
        :param pulumi.Input[str] ssl_policy: The name of the SSL Policy for the listener. Required if `protocol` is `HTTPS` or `TLS`.

        The **default_actions** object supports the following:

          * `authenticateCognito` (`pulumi.Input[dict]`)
            * `authenticationRequestExtraParams` (`pulumi.Input[dict]`) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
            * `onUnauthenticatedRequest` (`pulumi.Input[str]`) - The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
            * `scope` (`pulumi.Input[str]`) - The set of user claims to be requested from the IdP.
            * `sessionCookieName` (`pulumi.Input[str]`) - The name of the cookie used to maintain session information.
            * `sessionTimeout` (`pulumi.Input[float]`) - The maximum duration of the authentication session, in seconds.
            * `userPoolArn` (`pulumi.Input[str]`) - The ARN of the Cognito user pool.
            * `userPoolClientId` (`pulumi.Input[str]`) - The ID of the Cognito user pool client.
            * `userPoolDomain` (`pulumi.Input[str]`) - The domain prefix or fully-qualified domain name of the Cognito user pool.

          * `authenticateOidc` (`pulumi.Input[dict]`)
            * `authenticationRequestExtraParams` (`pulumi.Input[dict]`) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
            * `authorizationEndpoint` (`pulumi.Input[str]`) - The authorization endpoint of the IdP.
            * `client_id` (`pulumi.Input[str]`) - The OAuth 2.0 client identifier.
            * `client_secret` (`pulumi.Input[str]`) - The OAuth 2.0 client secret.
            * `issuer` (`pulumi.Input[str]`) - The OIDC issuer identifier of the IdP.
            * `onUnauthenticatedRequest` (`pulumi.Input[str]`) - The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
            * `scope` (`pulumi.Input[str]`) - The set of user claims to be requested from the IdP.
            * `sessionCookieName` (`pulumi.Input[str]`) - The name of the cookie used to maintain session information.
            * `sessionTimeout` (`pulumi.Input[float]`) - The maximum duration of the authentication session, in seconds.
            * `tokenEndpoint` (`pulumi.Input[str]`) - The token endpoint of the IdP.
            * `userInfoEndpoint` (`pulumi.Input[str]`) - The user info endpoint of the IdP.

          * `fixedResponse` (`pulumi.Input[dict]`) - Information for creating an action that returns a custom HTTP response. Required if `type` is `fixed-response`.
            * `content_type` (`pulumi.Input[str]`) - The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.
            * `messageBody` (`pulumi.Input[str]`) - The message body.
            * `status_code` (`pulumi.Input[str]`) - The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.

          * `forward` (`pulumi.Input[dict]`) - Information for creating an action that distributes requests among one or more target groups. Specify only if `type` is `forward`. If you specify both `forward` block and `target_group_arn` attribute, you can specify only one target group using `forward` and it must be the same target group specified in `target_group_arn`.
            * `stickiness` (`pulumi.Input[dict]`) - The target group stickiness for the rule.
              * `duration` (`pulumi.Input[float]`) - The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).
              * `enabled` (`pulumi.Input[bool]`) - Indicates whether target group stickiness is enabled.

            * `targetGroups` (`pulumi.Input[list]`) - One or more target groups block.
              * `arn` (`pulumi.Input[str]`) - The Amazon Resource Name (ARN) of the target group.
              * `weight` (`pulumi.Input[float]`) - The weight. The range is 0 to 999.

          * `order` (`pulumi.Input[float]`)
          * `redirect` (`pulumi.Input[dict]`) - Information for creating a redirect action. Required if `type` is `redirect`.
            * `host` (`pulumi.Input[str]`) - The hostname. This component is not percent-encoded. The hostname can contain `#{host}`. Defaults to `#{host}`.
            * `path` (`pulumi.Input[str]`) - The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to `/#{path}`.
            * `port` (`pulumi.Input[str]`) - The port. Specify a value from `1` to `65535` or `#{port}`. Defaults to `#{port}`.
            * `protocol` (`pulumi.Input[str]`) - The protocol. Valid values are `HTTP`, `HTTPS`, or `#{protocol}`. Defaults to `#{protocol}`.
            * `query` (`pulumi.Input[str]`) - The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?". Defaults to `#{query}`.
            * `status_code` (`pulumi.Input[str]`) - The HTTP redirect code. The redirect is either permanent (`HTTP_301`) or temporary (`HTTP_302`).

          * `target_group_arn` (`pulumi.Input[str]`) - The ARN of the Target Group to which to route traffic. Specify only if `type` is `forward` and you want to route to a single target group. To route to one or more target groups, use a `forward` block instead.
          * `type` (`pulumi.Input[str]`) - The type of routing action. Valid values are `forward`, `redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.
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

            __props__['certificate_arn'] = certificate_arn
            if default_actions is None:
                raise TypeError("Missing required property 'default_actions'")
            __props__['default_actions'] = default_actions
            if load_balancer_arn is None:
                raise TypeError("Missing required property 'load_balancer_arn'")
            __props__['load_balancer_arn'] = load_balancer_arn
            if port is None:
                raise TypeError("Missing required property 'port'")
            __props__['port'] = port
            __props__['protocol'] = protocol
            __props__['ssl_policy'] = ssl_policy
            __props__['arn'] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="aws:applicationloadbalancing/listener:Listener")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Listener, __self__).__init__(
            'aws:alb/listener:Listener',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, certificate_arn=None, default_actions=None, load_balancer_arn=None, port=None, protocol=None, ssl_policy=None):
        """
        Get an existing Listener resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the target group.
        :param pulumi.Input[str] certificate_arn: The ARN of the default SSL server certificate. Exactly one certificate is required if the protocol is HTTPS. For adding additional SSL certificates, see the `lb.ListenerCertificate` resource.
        :param pulumi.Input[list] default_actions: An Action block. Action blocks are documented below.
        :param pulumi.Input[str] load_balancer_arn: The ARN of the load balancer.
        :param pulumi.Input[float] port: The port on which the load balancer is listening.
        :param pulumi.Input[str] protocol: The protocol for connections from clients to the load balancer. Valid values are `TCP`, `TLS`, `UDP`, `TCP_UDP`, `HTTP` and `HTTPS`. Defaults to `HTTP`.
        :param pulumi.Input[str] ssl_policy: The name of the SSL Policy for the listener. Required if `protocol` is `HTTPS` or `TLS`.

        The **default_actions** object supports the following:

          * `authenticateCognito` (`pulumi.Input[dict]`)
            * `authenticationRequestExtraParams` (`pulumi.Input[dict]`) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
            * `onUnauthenticatedRequest` (`pulumi.Input[str]`) - The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
            * `scope` (`pulumi.Input[str]`) - The set of user claims to be requested from the IdP.
            * `sessionCookieName` (`pulumi.Input[str]`) - The name of the cookie used to maintain session information.
            * `sessionTimeout` (`pulumi.Input[float]`) - The maximum duration of the authentication session, in seconds.
            * `userPoolArn` (`pulumi.Input[str]`) - The ARN of the Cognito user pool.
            * `userPoolClientId` (`pulumi.Input[str]`) - The ID of the Cognito user pool client.
            * `userPoolDomain` (`pulumi.Input[str]`) - The domain prefix or fully-qualified domain name of the Cognito user pool.

          * `authenticateOidc` (`pulumi.Input[dict]`)
            * `authenticationRequestExtraParams` (`pulumi.Input[dict]`) - The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
            * `authorizationEndpoint` (`pulumi.Input[str]`) - The authorization endpoint of the IdP.
            * `client_id` (`pulumi.Input[str]`) - The OAuth 2.0 client identifier.
            * `client_secret` (`pulumi.Input[str]`) - The OAuth 2.0 client secret.
            * `issuer` (`pulumi.Input[str]`) - The OIDC issuer identifier of the IdP.
            * `onUnauthenticatedRequest` (`pulumi.Input[str]`) - The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
            * `scope` (`pulumi.Input[str]`) - The set of user claims to be requested from the IdP.
            * `sessionCookieName` (`pulumi.Input[str]`) - The name of the cookie used to maintain session information.
            * `sessionTimeout` (`pulumi.Input[float]`) - The maximum duration of the authentication session, in seconds.
            * `tokenEndpoint` (`pulumi.Input[str]`) - The token endpoint of the IdP.
            * `userInfoEndpoint` (`pulumi.Input[str]`) - The user info endpoint of the IdP.

          * `fixedResponse` (`pulumi.Input[dict]`) - Information for creating an action that returns a custom HTTP response. Required if `type` is `fixed-response`.
            * `content_type` (`pulumi.Input[str]`) - The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.
            * `messageBody` (`pulumi.Input[str]`) - The message body.
            * `status_code` (`pulumi.Input[str]`) - The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.

          * `forward` (`pulumi.Input[dict]`) - Information for creating an action that distributes requests among one or more target groups. Specify only if `type` is `forward`. If you specify both `forward` block and `target_group_arn` attribute, you can specify only one target group using `forward` and it must be the same target group specified in `target_group_arn`.
            * `stickiness` (`pulumi.Input[dict]`) - The target group stickiness for the rule.
              * `duration` (`pulumi.Input[float]`) - The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).
              * `enabled` (`pulumi.Input[bool]`) - Indicates whether target group stickiness is enabled.

            * `targetGroups` (`pulumi.Input[list]`) - One or more target groups block.
              * `arn` (`pulumi.Input[str]`) - The Amazon Resource Name (ARN) of the target group.
              * `weight` (`pulumi.Input[float]`) - The weight. The range is 0 to 999.

          * `order` (`pulumi.Input[float]`)
          * `redirect` (`pulumi.Input[dict]`) - Information for creating a redirect action. Required if `type` is `redirect`.
            * `host` (`pulumi.Input[str]`) - The hostname. This component is not percent-encoded. The hostname can contain `#{host}`. Defaults to `#{host}`.
            * `path` (`pulumi.Input[str]`) - The absolute path, starting with the leading "/". This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to `/#{path}`.
            * `port` (`pulumi.Input[str]`) - The port. Specify a value from `1` to `65535` or `#{port}`. Defaults to `#{port}`.
            * `protocol` (`pulumi.Input[str]`) - The protocol. Valid values are `HTTP`, `HTTPS`, or `#{protocol}`. Defaults to `#{protocol}`.
            * `query` (`pulumi.Input[str]`) - The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading "?". Defaults to `#{query}`.
            * `status_code` (`pulumi.Input[str]`) - The HTTP redirect code. The redirect is either permanent (`HTTP_301`) or temporary (`HTTP_302`).

          * `target_group_arn` (`pulumi.Input[str]`) - The ARN of the Target Group to which to route traffic. Specify only if `type` is `forward` and you want to route to a single target group. To route to one or more target groups, use a `forward` block instead.
          * `type` (`pulumi.Input[str]`) - The type of routing action. Valid values are `forward`, `redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["certificate_arn"] = certificate_arn
        __props__["default_actions"] = default_actions
        __props__["load_balancer_arn"] = load_balancer_arn
        __props__["port"] = port
        __props__["protocol"] = protocol
        __props__["ssl_policy"] = ssl_policy
        return Listener(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
