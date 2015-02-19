# -*- coding: utf-8 -*-

# Copyright (C) 2015 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from ..endpoints import EndpointsCommand

from hamcrest import assert_that, equal_to

from xivo_lib_rest_client.tests.command import HTTPCommandTestCase


class TestEndpoints(HTTPCommandTestCase):

    Command = EndpointsCommand

    def test_get(self):
        self.session.get.return_value = self.new_response(200, json={'return': 'value'})

        result = self.command.get(42)

        expected_url = '{base_url}/{endpoint_id}'.format(base_url=self.base_url, endpoint_id=42)
        self.session.get.assert_called_once_with(expected_url)
        assert_that(result, equal_to({'return': 'value'}))

    def test_get_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.get, 42)
