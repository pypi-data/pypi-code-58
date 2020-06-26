# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from spaceone.api.monitoring.plugin import metric_pb2 as spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2


class MetricStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.list = channel.unary_stream(
                '/spaceone.api.monitoring.plugin.Metric/list',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.PluginMetricsResponse.FromString,
                )
        self.get_data = channel.unary_stream(
                '/spaceone.api.monitoring.plugin.Metric/get_data',
                request_serializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricDataRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.PluginMetricDataResponse.FromString,
                )


class MetricServicer(object):
    """Missing associated documentation comment in .proto file."""

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_data(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetricServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'list': grpc.unary_stream_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.PluginMetricsResponse.SerializeToString,
            ),
            'get_data': grpc.unary_stream_rpc_method_handler(
                    servicer.get_data,
                    request_deserializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricDataRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.PluginMetricDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.monitoring.plugin.Metric', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Metric(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spaceone.api.monitoring.plugin.Metric/list',
            spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.PluginMetricsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spaceone.api.monitoring.plugin.Metric/get_data',
            spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.MetricDataRequest.SerializeToString,
            spaceone_dot_api_dot_monitoring_dot_plugin_dot_metric__pb2.PluginMetricDataResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
