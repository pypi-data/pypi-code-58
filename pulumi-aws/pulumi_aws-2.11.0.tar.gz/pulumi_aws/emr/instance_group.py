# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class InstanceGroup(pulumi.CustomResource):
    autoscaling_policy: pulumi.Output[str]
    """
    The autoscaling policy document. This is a JSON formatted string. See [EMR Auto Scaling](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html)
    """
    bid_price: pulumi.Output[str]
    """
    If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.
    """
    cluster_id: pulumi.Output[str]
    """
    ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.
    """
    configurations_json: pulumi.Output[str]
    """
    A JSON string for supplying list of configurations specific to the EMR instance group. Note that this can only be changed when using EMR release 5.21 or later.
    """
    ebs_configs: pulumi.Output[list]
    """
    One or more `ebs_config` blocks as defined below. Changing this forces a new resource to be created.

      * `iops` (`float`) - The number of I/O operations per second (IOPS) that the volume supports.
      * `size` (`float`) - The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
      * `type` (`str`) - The volume type. Valid options are 'gp2', 'io1' and 'standard'.
      * `volumesPerInstance` (`float`) - The number of EBS Volumes to attach per instance.
    """
    ebs_optimized: pulumi.Output[bool]
    """
    Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.
    """
    instance_count: pulumi.Output[float]
    """
    target number of instances for the instance group. defaults to 0.
    """
    instance_type: pulumi.Output[str]
    """
    The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Human friendly name given to the instance group. Changing this forces a new resource to be created.
    """
    running_instance_count: pulumi.Output[float]
    status: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, autoscaling_policy=None, bid_price=None, cluster_id=None, configurations_json=None, ebs_configs=None, ebs_optimized=None, instance_count=None, instance_type=None, name=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides an Elastic MapReduce Cluster Instance Group configuration.
        See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/emr/) for more information.

        > **NOTE:** At this time, Instance Groups cannot be destroyed through the API nor
        web interface. Instance Groups are destroyed when the EMR Cluster is destroyed.
        this provider will resize any Instance Group to zero when destroying the resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        task = aws.emr.InstanceGroup("task",
            cluster_id=aws_emr_cluster["tf-test-cluster"]["id"],
            instance_count=1,
            instance_type="m5.xlarge")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] autoscaling_policy: The autoscaling policy document. This is a JSON formatted string. See [EMR Auto Scaling](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html)
        :param pulumi.Input[str] bid_price: If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.
        :param pulumi.Input[str] cluster_id: ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] configurations_json: A JSON string for supplying list of configurations specific to the EMR instance group. Note that this can only be changed when using EMR release 5.21 or later.
        :param pulumi.Input[list] ebs_configs: One or more `ebs_config` blocks as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] ebs_optimized: Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.
        :param pulumi.Input[float] instance_count: target number of instances for the instance group. defaults to 0.
        :param pulumi.Input[str] instance_type: The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Human friendly name given to the instance group. Changing this forces a new resource to be created.

        The **ebs_configs** object supports the following:

          * `iops` (`pulumi.Input[float]`) - The number of I/O operations per second (IOPS) that the volume supports.
          * `size` (`pulumi.Input[float]`) - The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
          * `type` (`pulumi.Input[str]`) - The volume type. Valid options are 'gp2', 'io1' and 'standard'.
          * `volumesPerInstance` (`pulumi.Input[float]`) - The number of EBS Volumes to attach per instance.
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

            __props__['autoscaling_policy'] = autoscaling_policy
            __props__['bid_price'] = bid_price
            if cluster_id is None:
                raise TypeError("Missing required property 'cluster_id'")
            __props__['cluster_id'] = cluster_id
            __props__['configurations_json'] = configurations_json
            __props__['ebs_configs'] = ebs_configs
            __props__['ebs_optimized'] = ebs_optimized
            __props__['instance_count'] = instance_count
            if instance_type is None:
                raise TypeError("Missing required property 'instance_type'")
            __props__['instance_type'] = instance_type
            __props__['name'] = name
            __props__['running_instance_count'] = None
            __props__['status'] = None
        super(InstanceGroup, __self__).__init__(
            'aws:emr/instanceGroup:InstanceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, autoscaling_policy=None, bid_price=None, cluster_id=None, configurations_json=None, ebs_configs=None, ebs_optimized=None, instance_count=None, instance_type=None, name=None, running_instance_count=None, status=None):
        """
        Get an existing InstanceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] autoscaling_policy: The autoscaling policy document. This is a JSON formatted string. See [EMR Auto Scaling](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html)
        :param pulumi.Input[str] bid_price: If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.
        :param pulumi.Input[str] cluster_id: ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.
        :param pulumi.Input[str] configurations_json: A JSON string for supplying list of configurations specific to the EMR instance group. Note that this can only be changed when using EMR release 5.21 or later.
        :param pulumi.Input[list] ebs_configs: One or more `ebs_config` blocks as defined below. Changing this forces a new resource to be created.
        :param pulumi.Input[bool] ebs_optimized: Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.
        :param pulumi.Input[float] instance_count: target number of instances for the instance group. defaults to 0.
        :param pulumi.Input[str] instance_type: The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Human friendly name given to the instance group. Changing this forces a new resource to be created.

        The **ebs_configs** object supports the following:

          * `iops` (`pulumi.Input[float]`) - The number of I/O operations per second (IOPS) that the volume supports.
          * `size` (`pulumi.Input[float]`) - The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
          * `type` (`pulumi.Input[str]`) - The volume type. Valid options are 'gp2', 'io1' and 'standard'.
          * `volumesPerInstance` (`pulumi.Input[float]`) - The number of EBS Volumes to attach per instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["autoscaling_policy"] = autoscaling_policy
        __props__["bid_price"] = bid_price
        __props__["cluster_id"] = cluster_id
        __props__["configurations_json"] = configurations_json
        __props__["ebs_configs"] = ebs_configs
        __props__["ebs_optimized"] = ebs_optimized
        __props__["instance_count"] = instance_count
        __props__["instance_type"] = instance_type
        __props__["name"] = name
        __props__["running_instance_count"] = running_instance_count
        __props__["status"] = status
        return InstanceGroup(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
