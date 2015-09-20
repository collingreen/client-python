from unittest import skip
import stackhut_client
from .test_helpers import BaseTest


TEST_HOST_NOSCHEME = 'localhost:4001'


class SimpleConnectionTest(BaseTest):
    """
    This is an extremely basic test that connects to a demo stackhut server.

    Verifies that a connection can be made without issue or that the client
    throws the correct errors.
    """

    def test_create_client(self):
        """
        Test that create_client returns a non-None
        value without throwing an error.
        """
        client = self.create_client()
        self.assertNotEqual(client, None)

    def test_schemeless_host(self):
        """
        Verify host with no scheme throws a MissingSchema exception.
        """
        client = self.create_client(host=TEST_HOST_NOSCHEME)
        MissingSchema = \
            stackhut_client.client.requests.exceptions.MissingSchema
        with self.assertRaises(MissingSchema):
            client.Default.add(1, 2)

    @skip('not implemented')
    def test_invalid_host(self):
        # TODO: specify how invalid hostname should be handled
        self.fail('test not implemented')
