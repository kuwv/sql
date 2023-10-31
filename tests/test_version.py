# SPDX-FileCopyrightText: © 2022 Jesse P. Johnson <jpj6652@gmail.com>
# SPDX-License-Identifier: MIT
"""Provide versioning sanity check."""

from sql import __version__


def test_version() -> None:
    assert __version__ == '0.1.0a0'
