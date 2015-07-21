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

from xivo_lib_rest_client import RESTCommand


class EndpointsCommand(RESTCommand):

    resource = 'endpoints'

    def get(self, endpoint_id):
        url = '{base_url}/{endpoint_id}'.format(base_url=self.base_url, endpoint_id=endpoint_id)

        r = self.session.get(url)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()
