"""
All of the classes related to how data is controlled in the application.
"""


"""
Query Layering System
The query layer system is used for optimizing the ability to drastically improve database querying
by making a modular component system that can be altered as need be, retaining functionality,
but perhaps, making quicker and simpler as needed.

The main classes
QueryIOC
All classes that use queries will use the QueryIOC for getting access to the current query layer.

QueryLayer
A class that is based around the decorator pattern. It provides the interface for handling queries.
Each App will call the QueryLayer using its specific app's queries. Each app needs a QueryLayer
that decorates another QueryLayer with it's Apps queries.

As peed, reliability, or decoupling is needed, these layers can be hotswapped out, so long as they retain
the previous queries needed by existing code.
"""



class QueryLayerDecorator:
    """
    The base query layer that all query layers will decorate the functionality to.
    """
    QueryLayer = None

    def __init__(self, queryLayer):
        self.QueryLayer = queryLayer


class QueryLayer(QueryLayerDecorator):
    """
    The query layer that should be inherited for nearly every single use
    of the Query Layering system.
    """

    def __init__(self, queryLayer):
        QueryLayerDecorator.__init__(self, queryLayer)


