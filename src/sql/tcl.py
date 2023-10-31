"""Provide TCL capabilities."""


# class BEGIN:
#     """Begin transaction."""


class COMMIT:
    """Commit changes."""


class LOCK_TABLE:
    """Lock a table."""


# class RELEASE_SAVEPOINT:
#     """Release savepoint for transaction."""


class ROLLBACK:
    """Rollback changes."""


# class SAVEPOINT:
#     """Set new savepoint for transaction."""


# class SET_TRANSACTION:
#     """Begin either a read-only or read-write transaction."""


# class SET_CONSTRAINT:
#     ...


__all__ = [
    # 'BEGIN',
    'COMMIT',
    'LOCK_TABLE',
    # 'RELEASE_SAVEPOINT',
    'ROLLBACK',
    # 'SAVEPOINT',
    # 'SET_TRANSACTION',
]
