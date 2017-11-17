#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SessionManager(object):
    """
    Session manager class, used to manage the various session objects and talk with Redis.
    """

    @staticmethod
    def instance():
        if not hasattr(SessionManager, "_instance"):
            # New instance
            SessionManager._instance = SessionManager()
        return SessionManager._instance

a = SessionManager.instance()
b = SessionManager.instance()

print id(a)
print id(b)