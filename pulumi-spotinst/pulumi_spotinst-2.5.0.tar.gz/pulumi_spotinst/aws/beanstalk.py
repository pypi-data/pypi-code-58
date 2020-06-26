# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Beanstalk(pulumi.CustomResource):
    beanstalk_environment_id: pulumi.Output[str]
    """
    The id of an existing Beanstalk environment. 
    """
    beanstalk_environment_name: pulumi.Output[str]
    """
    The name of an existing Beanstalk environment.
    """
    deployment_preferences: pulumi.Output[dict]
    """
    Preferences when performing a roll

      * `automaticRoll` (`bool`) - Should roll perform automatically
      * `batchSizePercentage` (`float`) - Percent size of each batch
      * `grace_period` (`float`) - Amount of time to wait between batches
      * `strategies` (`list`) - Strategy parameters
        * `action` (`str`) - Action to take
        * `shouldDrainInstances` (`bool`) - Bool value if to wait to drain instance 
    """
    desired_capacity: pulumi.Output[float]
    """
    The desired number of instances the group should have at any time.
    """
    instance_types_spots: pulumi.Output[list]
    """
    One or more instance types. To maximize the availability of Spot instances, select as many instance types as possible.
    """
    maintenance: pulumi.Output[str]
    managed_actions: pulumi.Output[dict]
    """
    Managed Actions parameters

      * `platformUpdate` (`dict`) - Platform Update parameters
        * `performAt` (`str`) - Actions to perform (options: timeWindow, never)
        * `timeWindow` (`str`) - Time Window for when action occurs ex. Mon:23:50-Tue:00:20
        * `updateLevel` (`str`) - - Level to update
    """
    max_size: pulumi.Output[float]
    """
    The maximum number of instances the group should have at any time.
    """
    min_size: pulumi.Output[float]
    """
    The minimum number of instances the group should have at any time.
    """
    name: pulumi.Output[str]
    """
    The group name.
    """
    product: pulumi.Output[str]
    """
    Operation system type. Valid values: `"Linux/UNIX"`, `"SUSE Linux"`, `"Windows"`.
    For EC2 Classic instances:  `"Linux/UNIX (Amazon VPC)"`, `"SUSE Linux (Amazon VPC)"`, `"Windows (Amazon VPC)"`.
    """
    region: pulumi.Output[str]
    """
    The AWS region your group will be created in. Cannot be changed after the group has been created.
    """
    scheduled_tasks: pulumi.Output[list]
    def __init__(__self__, resource_name, opts=None, beanstalk_environment_id=None, beanstalk_environment_name=None, deployment_preferences=None, desired_capacity=None, instance_types_spots=None, maintenance=None, managed_actions=None, max_size=None, min_size=None, name=None, product=None, region=None, scheduled_tasks=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Spotinst AWS group resource using Elastic Beanstalk.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_spotinst as spotinst

        elastigoup_aws_beanstalk = spotinst.aws.Beanstalk("elastigoup-aws-beanstalk",
            beanstalk_environment_id="e-example",
            beanstalk_environment_name="example-env",
            deployment_preferences={
                "automaticRoll": True,
                "batchSizePercentage": 100,
                "grace_period": 90,
                "strategy": [{
                    "action": "REPLACE_SERVER",
                    "shouldDrainInstances": True,
                }],
            },
            desired_capacity=0,
            instance_types_spots=[
                "t2.micro",
                "t2.medium",
                "t2.large",
            ],
            managed_actions={
                "platformUpdate": {
                    "performAt": "timeWindow",
                    "timeWindow": "Mon:23:50-Tue:00:20",
                    "updateLevel": "minorAndPatch",
                },
            },
            max_size=1,
            min_size=0,
            product="Linux/UNIX",
            region="us-west-2")
        ```

        ## Scheduled Tasks

        Each `scheduled_task` supports the following:

        * `task_type` - (Required) The task type to run. Supported task types are: `"scale"`, `"backup_ami"`, `"roll"`, `"scaleUp"`, `"percentageScaleUp"`, `"scaleDown"`, `"percentageScaleDown"`, `"statefulUpdateCapacity"`.
        * `cron_expression` - (Optional; Required if not using `frequency`) A valid cron expression. The cron is running in UTC time zone and is in [Unix cron format](https://en.wikipedia.org/wiki/Cron).
        * `start_time` - (Optional; Format: ISO 8601) Set a start time for one time tasks.
        * `frequency` - (Optional; Required if not using `cron_expression`) The recurrence frequency to run this task. Supported values are `"hourly"`, `"daily"`, `"weekly"` and `"continuous"`.
        * `scale_target_capacity` - (Optional) The desired number of instances the group should have.
        * `scale_min_capacity` - (Optional) The minimum number of instances the group should have.
        * `scale_max_capacity` - (Optional) The maximum number of instances the group should have.
        * `is_enabled` - (Optional, Default: `true`) Setting the task to being enabled or disabled.
        * `target_capacity` - (Optional; Only valid for statefulUpdateCapacity) The desired number of instances the group should have.
        * `min_capacity` - (Optional; Only valid for statefulUpdateCapacity) The minimum number of instances the group should have.
        * `max_capacity` - (Optional; Only valid for statefulUpdateCapacity) The maximum number of instances the group should have.
        * `batch_size_percentage` - (Optional; Required when the `task_type` is `"roll"`.) The percentage size of each batch in the scheduled deployment roll.
        * `grace_period` - (Optional) The period of time (seconds) to wait before checking a batch's health after it's deployment.
        * `adjustment` - (Optional; Min 1) The number of instances to add or remove.
        * `adjustment_percentage` - (Optional; Min 1) The percentage of instances to add or remove.

        Usage:

        ```python
        import pulumi
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] beanstalk_environment_id: The id of an existing Beanstalk environment. 
        :param pulumi.Input[str] beanstalk_environment_name: The name of an existing Beanstalk environment.
        :param pulumi.Input[dict] deployment_preferences: Preferences when performing a roll
        :param pulumi.Input[float] desired_capacity: The desired number of instances the group should have at any time.
        :param pulumi.Input[list] instance_types_spots: One or more instance types. To maximize the availability of Spot instances, select as many instance types as possible.
        :param pulumi.Input[dict] managed_actions: Managed Actions parameters
        :param pulumi.Input[float] max_size: The maximum number of instances the group should have at any time.
        :param pulumi.Input[float] min_size: The minimum number of instances the group should have at any time.
        :param pulumi.Input[str] name: The group name.
        :param pulumi.Input[str] product: Operation system type. Valid values: `"Linux/UNIX"`, `"SUSE Linux"`, `"Windows"`.
               For EC2 Classic instances:  `"Linux/UNIX (Amazon VPC)"`, `"SUSE Linux (Amazon VPC)"`, `"Windows (Amazon VPC)"`.
        :param pulumi.Input[str] region: The AWS region your group will be created in. Cannot be changed after the group has been created.

        The **deployment_preferences** object supports the following:

          * `automaticRoll` (`pulumi.Input[bool]`) - Should roll perform automatically
          * `batchSizePercentage` (`pulumi.Input[float]`) - Percent size of each batch
          * `grace_period` (`pulumi.Input[float]`) - Amount of time to wait between batches
          * `strategies` (`pulumi.Input[list]`) - Strategy parameters
            * `action` (`pulumi.Input[str]`) - Action to take
            * `shouldDrainInstances` (`pulumi.Input[bool]`) - Bool value if to wait to drain instance 

        The **managed_actions** object supports the following:

          * `platformUpdate` (`pulumi.Input[dict]`) - Platform Update parameters
            * `performAt` (`pulumi.Input[str]`) - Actions to perform (options: timeWindow, never)
            * `timeWindow` (`pulumi.Input[str]`) - Time Window for when action occurs ex. Mon:23:50-Tue:00:20
            * `updateLevel` (`pulumi.Input[str]`) - - Level to update

        The **scheduled_tasks** object supports the following:

          * `adjustment` (`pulumi.Input[str]`)
          * `adjustmentPercentage` (`pulumi.Input[str]`)
          * `batchSizePercentage` (`pulumi.Input[str]`) - Percent size of each batch
          * `cronExpression` (`pulumi.Input[str]`)
          * `frequency` (`pulumi.Input[str]`)
          * `grace_period` (`pulumi.Input[str]`) - Amount of time to wait between batches
          * `isEnabled` (`pulumi.Input[bool]`)
          * `maxCapacity` (`pulumi.Input[str]`)
          * `minCapacity` (`pulumi.Input[str]`)
          * `scaleMaxCapacity` (`pulumi.Input[str]`)
          * `scaleMinCapacity` (`pulumi.Input[str]`)
          * `scaleTargetCapacity` (`pulumi.Input[str]`)
          * `startTime` (`pulumi.Input[str]`)
          * `targetCapacity` (`pulumi.Input[str]`)
          * `taskType` (`pulumi.Input[str]`)
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

            __props__['beanstalk_environment_id'] = beanstalk_environment_id
            __props__['beanstalk_environment_name'] = beanstalk_environment_name
            __props__['deployment_preferences'] = deployment_preferences
            if desired_capacity is None:
                raise TypeError("Missing required property 'desired_capacity'")
            __props__['desired_capacity'] = desired_capacity
            if instance_types_spots is None:
                raise TypeError("Missing required property 'instance_types_spots'")
            __props__['instance_types_spots'] = instance_types_spots
            __props__['maintenance'] = maintenance
            __props__['managed_actions'] = managed_actions
            if max_size is None:
                raise TypeError("Missing required property 'max_size'")
            __props__['max_size'] = max_size
            if min_size is None:
                raise TypeError("Missing required property 'min_size'")
            __props__['min_size'] = min_size
            __props__['name'] = name
            if product is None:
                raise TypeError("Missing required property 'product'")
            __props__['product'] = product
            if region is None:
                raise TypeError("Missing required property 'region'")
            __props__['region'] = region
            __props__['scheduled_tasks'] = scheduled_tasks
        super(Beanstalk, __self__).__init__(
            'spotinst:aws/beanstalk:Beanstalk',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, beanstalk_environment_id=None, beanstalk_environment_name=None, deployment_preferences=None, desired_capacity=None, instance_types_spots=None, maintenance=None, managed_actions=None, max_size=None, min_size=None, name=None, product=None, region=None, scheduled_tasks=None):
        """
        Get an existing Beanstalk resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] beanstalk_environment_id: The id of an existing Beanstalk environment. 
        :param pulumi.Input[str] beanstalk_environment_name: The name of an existing Beanstalk environment.
        :param pulumi.Input[dict] deployment_preferences: Preferences when performing a roll
        :param pulumi.Input[float] desired_capacity: The desired number of instances the group should have at any time.
        :param pulumi.Input[list] instance_types_spots: One or more instance types. To maximize the availability of Spot instances, select as many instance types as possible.
        :param pulumi.Input[dict] managed_actions: Managed Actions parameters
        :param pulumi.Input[float] max_size: The maximum number of instances the group should have at any time.
        :param pulumi.Input[float] min_size: The minimum number of instances the group should have at any time.
        :param pulumi.Input[str] name: The group name.
        :param pulumi.Input[str] product: Operation system type. Valid values: `"Linux/UNIX"`, `"SUSE Linux"`, `"Windows"`.
               For EC2 Classic instances:  `"Linux/UNIX (Amazon VPC)"`, `"SUSE Linux (Amazon VPC)"`, `"Windows (Amazon VPC)"`.
        :param pulumi.Input[str] region: The AWS region your group will be created in. Cannot be changed after the group has been created.

        The **deployment_preferences** object supports the following:

          * `automaticRoll` (`pulumi.Input[bool]`) - Should roll perform automatically
          * `batchSizePercentage` (`pulumi.Input[float]`) - Percent size of each batch
          * `grace_period` (`pulumi.Input[float]`) - Amount of time to wait between batches
          * `strategies` (`pulumi.Input[list]`) - Strategy parameters
            * `action` (`pulumi.Input[str]`) - Action to take
            * `shouldDrainInstances` (`pulumi.Input[bool]`) - Bool value if to wait to drain instance 

        The **managed_actions** object supports the following:

          * `platformUpdate` (`pulumi.Input[dict]`) - Platform Update parameters
            * `performAt` (`pulumi.Input[str]`) - Actions to perform (options: timeWindow, never)
            * `timeWindow` (`pulumi.Input[str]`) - Time Window for when action occurs ex. Mon:23:50-Tue:00:20
            * `updateLevel` (`pulumi.Input[str]`) - - Level to update

        The **scheduled_tasks** object supports the following:

          * `adjustment` (`pulumi.Input[str]`)
          * `adjustmentPercentage` (`pulumi.Input[str]`)
          * `batchSizePercentage` (`pulumi.Input[str]`) - Percent size of each batch
          * `cronExpression` (`pulumi.Input[str]`)
          * `frequency` (`pulumi.Input[str]`)
          * `grace_period` (`pulumi.Input[str]`) - Amount of time to wait between batches
          * `isEnabled` (`pulumi.Input[bool]`)
          * `maxCapacity` (`pulumi.Input[str]`)
          * `minCapacity` (`pulumi.Input[str]`)
          * `scaleMaxCapacity` (`pulumi.Input[str]`)
          * `scaleMinCapacity` (`pulumi.Input[str]`)
          * `scaleTargetCapacity` (`pulumi.Input[str]`)
          * `startTime` (`pulumi.Input[str]`)
          * `targetCapacity` (`pulumi.Input[str]`)
          * `taskType` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["beanstalk_environment_id"] = beanstalk_environment_id
        __props__["beanstalk_environment_name"] = beanstalk_environment_name
        __props__["deployment_preferences"] = deployment_preferences
        __props__["desired_capacity"] = desired_capacity
        __props__["instance_types_spots"] = instance_types_spots
        __props__["maintenance"] = maintenance
        __props__["managed_actions"] = managed_actions
        __props__["max_size"] = max_size
        __props__["min_size"] = min_size
        __props__["name"] = name
        __props__["product"] = product
        __props__["region"] = region
        __props__["scheduled_tasks"] = scheduled_tasks
        return Beanstalk(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

