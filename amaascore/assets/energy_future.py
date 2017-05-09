from __future__ import absolute_import, division, print_function, unicode_literals

from datetime import date
from decimal import Decimal

from amaascore.assets.future import Future


class EnergyFuture(Future):

    def __init__(self, asset_manager_id, asset_id, settlement_type, contract_size, point_value, tick_size,
                 quote_unit=None, asset_issuer_id=None, asset_status='Active', issue_date=date.min,
                 expiry_date=date.max, currency=None,
                 display_name='', description='', country_id=None, venue_id=None,
                 links=None, references=None, *args, **kwargs):
        """

        :param asset_manager_id: The asset manager who owns the data for this EnergyFuture
        :param asset_id: The owning asset manager's identifier for this EnergyFuture
        :param expiry_date: The date on which this EnergyFuture will expire
        :param asset_issuer_id: The owning asset manager's identifier for the issuer of this future
        :param asset_status: The status of this EnergyFuture
        :param issue_date: The date on which this EnergyFuture was created
        :param display_name: A human-readable name for this EnergyFuture
        :param description: A human-readable description of this EnergyFuture
        :param country_id: The ISO 3166-1 alpha-3 code for the country that this EnergyFuture was issued in
        :param venue_id: The ISO-10383 identifier for the venue on which this EnergyFuture trades
        :param references: A dictionary of additional References for this EnergyFuture
        :param args:
        :param kwargs:
        """
        super(EnergyFuture, self).__init__(asset_manager_id=asset_manager_id, asset_id=asset_id,
                                           settlement_type=settlement_type, contract_size=contract_size,
                                           point_value=point_value, tick_size=tick_size, quote_unit=quote_unit,
                                           asset_issuer_id=asset_issuer_id, asset_status=asset_status,
                                           display_name=display_name, currency=currency,
                                           description=description, country_id=country_id, venue_id=venue_id,
                                           links=links, references=references, issue_date=issue_date,
                                           expiry_date=expiry_date,
                                           *args, **kwargs)
