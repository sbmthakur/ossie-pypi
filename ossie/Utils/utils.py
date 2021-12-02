def parse_url(url:str) -> dict:
    try:
        if not url:
            return None
        import six
        if six.PY2:
            from urlparse import urlparse
        elif six.PY3:
            from urllib.parse import urlparse
        parsed_uri = urlparse(url)
        return {
            'scheme'   : parsed_uri.scheme,
            'netloc'   : parsed_uri.netloc,
            'path'     : parsed_uri.path,
            'params'   : parsed_uri.params,
            'query'    : parsed_uri.query,
            'fragment' : parsed_uri.fragment,
        }
    except ImportError as e:
        raise Exception("'urllib' module not available. Please install.")
        exit(1)
    except Exception as e:
        raise Exception("Failed to extract domain from url %s: %s" % (url, str(e)))
