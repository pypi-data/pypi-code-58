# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Account(pulumi.CustomResource):
    endpoint: pulumi.Output[str]
    """
    The endpoint used to connect to the Cognitive Service Account.
    """
    kind: pulumi.Output[str]
    """
    Specifies the type of Cognitive Service Account that should be created. Possible values are `Academic`, `Bing.Autosuggest`, `Bing.Autosuggest.v7`, `Bing.CustomSearch`, `Bing.Search`, `Bing.Search.v7`, `Bing.Speech`, `Bing.SpellCheck`, `Bing.SpellCheck.v7`, `CognitiveServices`, `ComputerVision`, `ContentModerator`, `CustomSpeech`, `CustomVision.Prediction`, `CustomVision.Training`, `Emotion`, `Face`,`FormRecognizer`, `ImmersiveReader`, `LUIS`, `LUIS.Authoring`, `QnAMaker`, `Recommendations`, `SpeakerRecognition`, `Speech`, `SpeechServices`, `SpeechTranslation`, `TextAnalytics`, `TextTranslation` and `WebLM`. Changing this forces a new resource to be created.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.
    """
    primary_access_key: pulumi.Output[str]
    """
    A primary access key which can be used to connect to the Cognitive Service Account.
    """
    qna_runtime_endpoint: pulumi.Output[str]
    """
    A URL to link a QnAMaker cognitive account to a QnA runtime.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.
    """
    secondary_access_key: pulumi.Output[str]
    """
    The secondary access key which can be used to connect to the Cognitive Service Account.
    """
    sku_name: pulumi.Output[str]
    """
    Specifies the SKU Name for this Cognitive Service Account. Possible values are `F0`, `F1`, `S0`, `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `P0`, `P1`, and `P2`.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, resource_name, opts=None, kind=None, location=None, name=None, qna_runtime_endpoint=None, resource_group_name=None, sku_name=None, tags=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a Cognitive Services Account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_azure as azure

        example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")
        example_account = azure.cognitive.Account("exampleAccount",
            location=example_resource_group.location,
            resource_group_name=example_resource_group.name,
            kind="Face",
            sku_name="S0",
            tags={
                "Acceptance": "Test",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kind: Specifies the type of Cognitive Service Account that should be created. Possible values are `Academic`, `Bing.Autosuggest`, `Bing.Autosuggest.v7`, `Bing.CustomSearch`, `Bing.Search`, `Bing.Search.v7`, `Bing.Speech`, `Bing.SpellCheck`, `Bing.SpellCheck.v7`, `CognitiveServices`, `ComputerVision`, `ContentModerator`, `CustomSpeech`, `CustomVision.Prediction`, `CustomVision.Training`, `Emotion`, `Face`,`FormRecognizer`, `ImmersiveReader`, `LUIS`, `LUIS.Authoring`, `QnAMaker`, `Recommendations`, `SpeakerRecognition`, `Speech`, `SpeechServices`, `SpeechTranslation`, `TextAnalytics`, `TextTranslation` and `WebLM`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.
        :param pulumi.Input[str] qna_runtime_endpoint: A URL to link a QnAMaker cognitive account to a QnA runtime.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] sku_name: Specifies the SKU Name for this Cognitive Service Account. Possible values are `F0`, `F1`, `S0`, `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `P0`, `P1`, and `P2`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
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

            if kind is None:
                raise TypeError("Missing required property 'kind'")
            __props__['kind'] = kind
            __props__['location'] = location
            __props__['name'] = name
            __props__['qna_runtime_endpoint'] = qna_runtime_endpoint
            if resource_group_name is None:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__['resource_group_name'] = resource_group_name
            if sku_name is None:
                raise TypeError("Missing required property 'sku_name'")
            __props__['sku_name'] = sku_name
            __props__['tags'] = tags
            __props__['endpoint'] = None
            __props__['primary_access_key'] = None
            __props__['secondary_access_key'] = None
        super(Account, __self__).__init__(
            'azure:cognitive/account:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, endpoint=None, kind=None, location=None, name=None, primary_access_key=None, qna_runtime_endpoint=None, resource_group_name=None, secondary_access_key=None, sku_name=None, tags=None):
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint: The endpoint used to connect to the Cognitive Service Account.
        :param pulumi.Input[str] kind: Specifies the type of Cognitive Service Account that should be created. Possible values are `Academic`, `Bing.Autosuggest`, `Bing.Autosuggest.v7`, `Bing.CustomSearch`, `Bing.Search`, `Bing.Search.v7`, `Bing.Speech`, `Bing.SpellCheck`, `Bing.SpellCheck.v7`, `CognitiveServices`, `ComputerVision`, `ContentModerator`, `CustomSpeech`, `CustomVision.Prediction`, `CustomVision.Training`, `Emotion`, `Face`,`FormRecognizer`, `ImmersiveReader`, `LUIS`, `LUIS.Authoring`, `QnAMaker`, `Recommendations`, `SpeakerRecognition`, `Speech`, `SpeechServices`, `SpeechTranslation`, `TextAnalytics`, `TextTranslation` and `WebLM`. Changing this forces a new resource to be created.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Cognitive Service Account. Changing this forces a new resource to be created.
        :param pulumi.Input[str] primary_access_key: A primary access key which can be used to connect to the Cognitive Service Account.
        :param pulumi.Input[str] qna_runtime_endpoint: A URL to link a QnAMaker cognitive account to a QnA runtime.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which the Cognitive Service Account is created. Changing this forces a new resource to be created.
        :param pulumi.Input[str] secondary_access_key: The secondary access key which can be used to connect to the Cognitive Service Account.
        :param pulumi.Input[str] sku_name: Specifies the SKU Name for this Cognitive Service Account. Possible values are `F0`, `F1`, `S0`, `S1`, `S2`, `S3`, `S4`, `S5`, `S6`, `P0`, `P1`, and `P2`.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["endpoint"] = endpoint
        __props__["kind"] = kind
        __props__["location"] = location
        __props__["name"] = name
        __props__["primary_access_key"] = primary_access_key
        __props__["qna_runtime_endpoint"] = qna_runtime_endpoint
        __props__["resource_group_name"] = resource_group_name
        __props__["secondary_access_key"] = secondary_access_key
        __props__["sku_name"] = sku_name
        __props__["tags"] = tags
        return Account(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
