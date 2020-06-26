# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Repository(pulumi.CustomResource):
    name: pulumi.Output[str]
    """
    Resource name of the repository, of the form `{{repo}}`.
    The repo name may contain slashes. eg, `name/with/slash`
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    pubsub_configs: pulumi.Output[list]
    """
    How this repository publishes a change in the repository through Cloud Pub/Sub.
    Keyed by the topic names.  Structure is documented below.

      * `messageFormat` (`str`) - The format of the Cloud Pub/Sub messages.
        - PROTOBUF: The message payload is a serialized protocol buffer of SourceRepoEvent.
        - JSON: The message payload is a JSON string of SourceRepoEvent.
      * `service_account_email` (`str`) - Email address of the service account used for publishing Cloud Pub/Sub messages.
        This service account needs to be in the same project as the PubsubConfig. When added,
        the caller needs to have iam.serviceAccounts.actAs permission on this service account.
        If unspecified, it defaults to the compute engine default service account.
      * `topic` (`str`) - The identifier for this object. Format specified above.
    """
    size: pulumi.Output[float]
    """
    The disk usage of the repo, in bytes.
    """
    url: pulumi.Output[str]
    """
    URL to clone the repository from Google Cloud Source Repositories.
    """
    def __init__(__self__, resource_name, opts=None, name=None, project=None, pubsub_configs=None, __props__=None, __name__=None, __opts__=None):
        """
        A repository (or repo) is a Git repository storing versioned source content.

        To get more information about Repository, see:

        * [API documentation](https://cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/source-repositories/)

        ## Example Usage
        ### Sourcerepo Repository Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        my_repo = gcp.sourcerepo.Repository("my-repo")
        ```
        ### Sourcerepo Repository Full

        ```python
        import pulumi
        import pulumi_gcp as gcp

        test_account = gcp.service_account.Account("test-account",
            account_id="my-account",
            display_name="Test Service Account")
        topic = gcp.pubsub.Topic("topic")
        my_repo = gcp.sourcerepo.Repository("my-repo", pubsub_configs=[{
            "topic": topic.id,
            "messageFormat": "JSON",
            "service_account_email": test_account.email,
        }])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Resource name of the repository, of the form `{{repo}}`.
               The repo name may contain slashes. eg, `name/with/slash`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[list] pubsub_configs: How this repository publishes a change in the repository through Cloud Pub/Sub.
               Keyed by the topic names.  Structure is documented below.

        The **pubsub_configs** object supports the following:

          * `messageFormat` (`pulumi.Input[str]`) - The format of the Cloud Pub/Sub messages.
            - PROTOBUF: The message payload is a serialized protocol buffer of SourceRepoEvent.
            - JSON: The message payload is a JSON string of SourceRepoEvent.
          * `service_account_email` (`pulumi.Input[str]`) - Email address of the service account used for publishing Cloud Pub/Sub messages.
            This service account needs to be in the same project as the PubsubConfig. When added,
            the caller needs to have iam.serviceAccounts.actAs permission on this service account.
            If unspecified, it defaults to the compute engine default service account.
          * `topic` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
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

            __props__['name'] = name
            __props__['project'] = project
            __props__['pubsub_configs'] = pubsub_configs
            __props__['size'] = None
            __props__['url'] = None
        super(Repository, __self__).__init__(
            'gcp:sourcerepo/repository:Repository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, name=None, project=None, pubsub_configs=None, size=None, url=None):
        """
        Get an existing Repository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Resource name of the repository, of the form `{{repo}}`.
               The repo name may contain slashes. eg, `name/with/slash`
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        :param pulumi.Input[list] pubsub_configs: How this repository publishes a change in the repository through Cloud Pub/Sub.
               Keyed by the topic names.  Structure is documented below.
        :param pulumi.Input[float] size: The disk usage of the repo, in bytes.
        :param pulumi.Input[str] url: URL to clone the repository from Google Cloud Source Repositories.

        The **pubsub_configs** object supports the following:

          * `messageFormat` (`pulumi.Input[str]`) - The format of the Cloud Pub/Sub messages.
            - PROTOBUF: The message payload is a serialized protocol buffer of SourceRepoEvent.
            - JSON: The message payload is a JSON string of SourceRepoEvent.
          * `service_account_email` (`pulumi.Input[str]`) - Email address of the service account used for publishing Cloud Pub/Sub messages.
            This service account needs to be in the same project as the PubsubConfig. When added,
            the caller needs to have iam.serviceAccounts.actAs permission on this service account.
            If unspecified, it defaults to the compute engine default service account.
          * `topic` (`pulumi.Input[str]`) - The identifier for this object. Format specified above.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["name"] = name
        __props__["project"] = project
        __props__["pubsub_configs"] = pubsub_configs
        __props__["size"] = size
        __props__["url"] = url
        return Repository(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
