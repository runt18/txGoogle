from txGoogle.service import Service


class TimeseriesDescriptors(Service):
    def __init__(self, conn, *args, **kwargs):
        super(TimeseriesDescriptors, self).__init__(conn, *args, **kwargs)

    def list(self, project, metric, youngest, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, count=None, timespan=None, labels=None, pageToken=None, oldest=None, kind=None):
        '''List the descriptors of the time series that match the metric and labels values and that have data points in the interval. Large responses are paginated; use the nextPageToken returned in the response to request subsequent pages of results by setting the pageToken query parameter to the value of the nextPageToken.'''
        queryParams = {
            'url': 'https://www.googleapis.com/cloudmonitoring/v2beta1/projects/{project}/timeseriesDescriptors/{metric}',
            'method': 'GET',
            'resultType': 'ListTimeseriesDescriptorsRequest',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'count': count,
                'project': project,
                'timespan': timespan,
                'metric': metric,
                'labels': labels,
                'youngest': youngest,
                'pageToken': pageToken,
                'oldest': oldest,
            },
            'httpBodyParams': {
                'kind': kind,
            },
        }
        return self._request(queryParams)


class Timeseries(Service):
    def __init__(self, conn, *args, **kwargs):
        super(Timeseries, self).__init__(conn, *args, **kwargs)

    def list(self, project, metric, youngest, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, count=None, timespan=None, labels=None, pageToken=None, oldest=None, kind=None):
        '''List the data points of the time series that match the metric and labels values and that have data points in the interval. Large responses are paginated; use the nextPageToken returned in the response to request subsequent pages of results by setting the pageToken query parameter to the value of the nextPageToken.'''
        queryParams = {
            'url': 'https://www.googleapis.com/cloudmonitoring/v2beta1/projects/{project}/timeseries/{metric}',
            'method': 'GET',
            'resultType': 'ListTimeseriesRequest',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'count': count,
                'project': project,
                'timespan': timespan,
                'metric': metric,
                'labels': labels,
                'youngest': youngest,
                'pageToken': pageToken,
                'oldest': oldest,
            },
            'httpBodyParams': {
                'kind': kind,
            },
        }
        return self._request(queryParams)


class MetricDescriptors(Service):
    def __init__(self, conn, *args, **kwargs):
        super(MetricDescriptors, self).__init__(conn, *args, **kwargs)

    def list(self, project, prettyPrint=None, fields=None, quotaUser=None, oauth_token=None, key=None, userIp=None, alt=None, count=None, pageToken=None, query=None, kind=None):
        '''List metric descriptors that match the query. If the query is not set, then all of the metric descriptors will be returned. Large responses will be paginated, use the nextPageToken returned in the response to request subsequent pages of results by setting the pageToken query parameter to the value of the nextPageToken.'''
        queryParams = {
            'url': 'https://www.googleapis.com/cloudmonitoring/v2beta1/projects/{project}/metricDescriptors',
            'method': 'GET',
            'resultType': 'ListMetricDescriptorsRequest',
            'httpUrlParams': {
                'prettyPrint': prettyPrint,
                'fields': fields,
                'quotaUser': quotaUser,
                'oauth_token': oauth_token,
                'key': key,
                'userIp': userIp,
                'alt': alt,
                'count': count,
                'pageToken': pageToken,
                'project': project,
                'query': query,
            },
            'httpBodyParams': {
                'kind': kind,
            },
        }
        return self._request(queryParams)


class Cloudmonitoring(Service):
    '''API for accessing Google Cloud and API monitoring data.'''
    _DEFAULT_SCOPES = [u'https://www.googleapis.com/auth/monitoring.readonly']

    def __init__(self, conn=None, scopes=None, *args, **kwargs):
        if scopes is not None:
            self._scopes = scopes
        else:
            self._scopes = self._DEFAULT_SCOPES
        conn.registerScopes(self._scopes)
        super(Cloudmonitoring, self).__init__(conn, *args, **kwargs)
        self.timeseriesDescriptors = TimeseriesDescriptors(conn, *args, **kwargs)
        self.timeseries = Timeseries(conn, *args, **kwargs)
        self.metricDescriptors = MetricDescriptors(conn, *args, **kwargs)
