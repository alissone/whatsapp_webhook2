# Boilerplate for Selenium

This repository should serve as a base to new Selenium GUI projects, providing functions to allow using selenium interactively with a single session.

You can inherit and instantiate the `GenericBot` from `selenium_login.py` class only once, and connect any script to this window using `selenium_session.py`, instead of having to start a fresh session with every script.
