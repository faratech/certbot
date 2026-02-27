"""A simple wrapper around certbot.ocsp until it is internalized."""
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", "certbot.ocsp is deprecated")
    # ruff: disable[F403]
    from certbot.ocsp import *  # pylint: disable=wildcard-import,unused-wildcard-import
