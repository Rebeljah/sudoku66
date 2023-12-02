"""
Module for custom event subscription and publication.

This module provides functions to subscribe callback functions to specific event types
and to publish events to all subscribed callback functions.
"""

from typing import Hashable, Callable

event_subscribers = {}


def subscribe(event_type: Hashable, callback: Callable):
    """
    Subscribe a callback function to an event type.

    Args:
    - event_type (Hashable): The type of event to subscribe to.
    - callback (Callable): The function to be called when the event is published.
    """
    if event_type not in event_subscribers:
        event_subscribers[event_type] = []

    event_subscribers[event_type].append(callback)


def publish(event_type: Hashable, *args, **kwargs):
    """
    Publish an event to all subscribed callback functions.

    Args:
    - event_type (Hashable): The type of event to publish.
    - *args: Positional arguments to be passed to the callback functions.
    - **kwargs: Keyword arguments to be passed to the callback functions.
    """
    if event_type not in event_subscribers:
        return

    for callback in event_subscribers[event_type]:
        callback(*args, **kwargs)
