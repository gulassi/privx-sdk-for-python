from http import HTTPStatus
from typing import Optional

from privx_api.base import BasePrivXAPI
from privx_api.enums import UrlEnum
from privx_api.response import PrivXAPIResponse


class TrailIndexAPI(BasePrivXAPI):
    def get_trail_index_service_status(self) -> PrivXAPIResponse:
        """
        Get microservice status.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(UrlEnum.TRAIL_INDEX.STATUS)
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def get_indexing_status(self, conn_id: str) -> PrivXAPIResponse:
        """
        Get indexing status of the connection.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_get(
            UrlEnum.TRAIL_INDEX.CONNECTION_INDEXING_STATUS,
            path_params={"connection_id": conn_id},
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def resolve_indexing_statuses(self, conn_ids: list) -> PrivXAPIResponse:
        """
        Gets the statuses of the specified connections.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.TRAIL_INDEX.CONNECTIONS_INDEXING_STATUSES,
            body=conn_ids,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def start_indexing(self, conn_ids: list) -> PrivXAPIResponse:
        """
        Starts indexing of the specified connections.

        Returns:
            PrivXAPIResponse
        """
        response_status, data = self._http_post(
            UrlEnum.TRAIL_INDEX.START_INDEXING,
            body=conn_ids,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)

    def search_index(
        self,
        trails_params: dict,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_dir: Optional[str] = None,
    ) -> PrivXAPIResponse:
        """
        Search for the content based on the search parameters defined.

        Returns:
            PrivXAPIResponse
        """
        search_params = self._get_search_params(
            offset=offset,
            limit=limit,
            sortdir=sort_dir,
        )
        response_status, data = self._http_post(
            UrlEnum.TRAIL_INDEX.SEARCH,
            query_params=search_params,
            body=trails_params,
        )
        return PrivXAPIResponse(response_status, HTTPStatus.OK, data)
