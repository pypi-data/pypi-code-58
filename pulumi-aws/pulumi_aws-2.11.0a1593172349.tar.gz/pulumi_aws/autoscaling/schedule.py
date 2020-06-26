# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class Schedule(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN assigned by AWS to the autoscaling schedule.
    """
    autoscaling_group_name: pulumi.Output[str]
    """
    The name or Amazon Resource Name (ARN) of the Auto Scaling group.
    """
    desired_capacity: pulumi.Output[float]
    """
    The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.
    """
    end_time: pulumi.Output[str]
    """
    The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
    If you try to schedule your action in the past, Auto Scaling returns an error message.
    """
    max_size: pulumi.Output[float]
    """
    The maximum size for the Auto Scaling group. Default 0.
    Set to -1 if you don't want to change the maximum size at the scheduled time.
    """
    min_size: pulumi.Output[float]
    """
    The minimum size for the Auto Scaling group. Default 0.
    Set to -1 if you don't want to change the minimum size at the scheduled time.
    """
    recurrence: pulumi.Output[str]
    """
    The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
    """
    scheduled_action_name: pulumi.Output[str]
    """
    The name of this scaling action.
    """
    start_time: pulumi.Output[str]
    """
    The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
    If you try to schedule your action in the past, Auto Scaling returns an error message.
    """
    def __init__(__self__, resource_name, opts=None, autoscaling_group_name=None, desired_capacity=None, end_time=None, max_size=None, min_size=None, recurrence=None, scheduled_action_name=None, start_time=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an AutoScaling Schedule resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foobar_group = aws.autoscaling.Group("foobarGroup",
            availability_zones=["us-west-2a"],
            force_delete=True,
            health_check_grace_period=300,
            health_check_type="ELB",
            max_size=1,
            min_size=1,
            termination_policies=["OldestInstance"])
        foobar_schedule = aws.autoscaling.Schedule("foobarSchedule",
            autoscaling_group_name=foobar_group.name,
            desired_capacity=0,
            end_time="2016-12-12T06:00:00Z",
            max_size=1,
            min_size=0,
            scheduled_action_name="foobar",
            start_time="2016-12-11T18:00:00Z")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] autoscaling_group_name: The name or Amazon Resource Name (ARN) of the Auto Scaling group.
        :param pulumi.Input[float] desired_capacity: The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.
        :param pulumi.Input[str] end_time: The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
               If you try to schedule your action in the past, Auto Scaling returns an error message.
        :param pulumi.Input[float] max_size: The maximum size for the Auto Scaling group. Default 0.
               Set to -1 if you don't want to change the maximum size at the scheduled time.
        :param pulumi.Input[float] min_size: The minimum size for the Auto Scaling group. Default 0.
               Set to -1 if you don't want to change the minimum size at the scheduled time.
        :param pulumi.Input[str] recurrence: The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
        :param pulumi.Input[str] scheduled_action_name: The name of this scaling action.
        :param pulumi.Input[str] start_time: The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
               If you try to schedule your action in the past, Auto Scaling returns an error message.
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

            if autoscaling_group_name is None:
                raise TypeError("Missing required property 'autoscaling_group_name'")
            __props__['autoscaling_group_name'] = autoscaling_group_name
            __props__['desired_capacity'] = desired_capacity
            __props__['end_time'] = end_time
            __props__['max_size'] = max_size
            __props__['min_size'] = min_size
            __props__['recurrence'] = recurrence
            if scheduled_action_name is None:
                raise TypeError("Missing required property 'scheduled_action_name'")
            __props__['scheduled_action_name'] = scheduled_action_name
            __props__['start_time'] = start_time
            __props__['arn'] = None
        super(Schedule, __self__).__init__(
            'aws:autoscaling/schedule:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, arn=None, autoscaling_group_name=None, desired_capacity=None, end_time=None, max_size=None, min_size=None, recurrence=None, scheduled_action_name=None, start_time=None):
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN assigned by AWS to the autoscaling schedule.
        :param pulumi.Input[str] autoscaling_group_name: The name or Amazon Resource Name (ARN) of the Auto Scaling group.
        :param pulumi.Input[float] desired_capacity: The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don't want to change the desired capacity at the scheduled time.
        :param pulumi.Input[str] end_time: The time for this action to end, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
               If you try to schedule your action in the past, Auto Scaling returns an error message.
        :param pulumi.Input[float] max_size: The maximum size for the Auto Scaling group. Default 0.
               Set to -1 if you don't want to change the maximum size at the scheduled time.
        :param pulumi.Input[float] min_size: The minimum size for the Auto Scaling group. Default 0.
               Set to -1 if you don't want to change the minimum size at the scheduled time.
        :param pulumi.Input[str] recurrence: The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.
        :param pulumi.Input[str] scheduled_action_name: The name of this scaling action.
        :param pulumi.Input[str] start_time: The time for this action to start, in "YYYY-MM-DDThh:mm:ssZ" format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
               If you try to schedule your action in the past, Auto Scaling returns an error message.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["autoscaling_group_name"] = autoscaling_group_name
        __props__["desired_capacity"] = desired_capacity
        __props__["end_time"] = end_time
        __props__["max_size"] = max_size
        __props__["min_size"] = min_size
        __props__["recurrence"] = recurrence
        __props__["scheduled_action_name"] = scheduled_action_name
        __props__["start_time"] = start_time
        return Schedule(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
