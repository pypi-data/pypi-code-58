import ssl


class Ssl:

    @staticmethod
    def disable_ssl_check():
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context


if __name__ == '__main__':
    exit(0)
