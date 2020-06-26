# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marshmallow import fields
from marshmallow.validate import OneOf

from flowmachine.features import SubscriberLocations
from flowmachine.features.subscriber.unique_locations import UniqueLocations
from .custom_fields import EventTypes, SubscriberSubset, ISODateTime
from .aggregation_unit import AggregationUnitMixin
from .base_query_with_sampling import (
    BaseQueryWithSamplingSchema,
    BaseExposedQueryWithSampling,
)

__all__ = ["UniqueLocationsSchema", "UniqueLocationsExposed"]


class UniqueLocationsExposed(BaseExposedQueryWithSampling):
    def __init__(
        self,
        start_date,
        end_date,
        *,
        aggregation_unit,
        event_types,
        subscriber_subset=None,
        sampling=None
    ):
        # Note: all input parameters need to be defined as attributes on `self`
        # so that marshmallow can serialise the object correctly.
        self.start_date = start_date
        self.end_date = end_date
        self.aggregation_unit = aggregation_unit
        self.event_types = event_types
        self.subscriber_subset = subscriber_subset
        self.sampling = sampling

    @property
    def _unsampled_query_obj(self):
        """
        Return the underlying flowmachine unique locations object.

        Returns
        -------
        Query
        """
        return UniqueLocations(
            SubscriberLocations(
                self.start_date,
                self.end_date,
                spatial_unit=self.aggregation_unit,
                table=self.event_types,
                subscriber_subset=self.subscriber_subset,
            )
        )


class UniqueLocationsSchema(AggregationUnitMixin, BaseQueryWithSamplingSchema):
    # query_kind parameter is required here for claims validation
    query_kind = fields.String(validate=OneOf(["unique_locations"]))
    start_date = ISODateTime(required=True)
    end_date = ISODateTime(required=True)
    event_types = EventTypes()
    subscriber_subset = SubscriberSubset()

    __model__ = UniqueLocationsExposed
