from .test_helpers import BaseTest


class SimpleIntegrationTest(BaseTest):
    """
    This is a super simple integration test that goes through
    the entire lifecycle of connecting to an account, using a service,
    and ensuring it correctly returns the result (as the correct type).
    """

    def test_run_service(self):
        """
        Verify that running the add service correctly runs and returns the
        expected value.
        """
        for i in range(5):
            x, y = i, i * i
            result = self.client.Default.add(x, y)
            self.assertEqual(x + y, result)
