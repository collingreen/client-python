from unittest import TestCase
import logging
import stackhut_client


# uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.DEBUG)


TEST_USERNAME = 'stackhut'
TEST_SERVICE = 'demo-python'
TEST_HOST = None  # falls back to official server
INVALID_HOST = 'not a valid hostname'

use_local_server = False
if use_local_server:
    TEST_USERNAME = 'your-stackhut-username'
    TEST_SERVICE = 'your-server-name'
    TEST_HOST = 'http://localhost:4001'


def create_client(username=None, service=None, host=None):
    """
    Creates a new client connection. Uses the given parameters or
    falls back to the constants at this file.

    Returns a new SHService
    """

    target_username = username or TEST_USERNAME
    target_service = service or TEST_SERVICE
    target_host = host or TEST_HOST

    logging.debug(
        'creating stackhut connection for %s %s at %s' % (
            target_username,
            target_service,
            target_host
        )
    )

    if target_host:
        return stackhut_client.SHService(
            target_username,
            target_service,
            host=target_host
        )

    return stackhut_client.SHService(
        target_username,
        target_service
    )


class BaseTest(TestCase):
    """
    A base test class to help reduce boilerplate connection code.

    Includes a single `client` property that is created only once, then shared
    across all tests. Subclasses of this test case can simply use `self.client`
    without having to create a new connection every time.

    Note that because all your tests can share the same connection you must
    take care to ensure your tests do not rely on test ordering (or other tests
    at all).

    If a new connection is important to the test, the class also includes a
    `create_client` method that accepts optional username, service, and host
    and returns a new connection.

    """

    def create_client(self, username=None, service=None, host=None):
        """
        Returns a client created with the create_client function. Accepts
        optional username, service, and host. If any are left out, the
        test defaults from test_helpers.py will be used.
        """
        return create_client(username, service, host)

    @property
    def client(self):
        return self.get_client()

    def get_client(self):
        if not hasattr(self, '_client'):
            self._client = self.create_client()
        return self._client
