from PyQt4.QtGui import QPen
from PyQt4.Qt import Qt
from sloth.items import PolygonItemInserter


LABELS = (
    {
        'attributes': {
            'type': "poly",
            'class': 'vessel',
            'id': ['military', 'commercial', 'private', 'barge', 'sunken', 'no-id']
        },
        'inserter': 'sloth.items.PolygonItemInserter',
        'item':     'sloth.items.PolygonItem',  
        'text':     'Vessel',
    },
    {
        'attributes': {
            'class':      'vessel-point',
            'id': ['military', 'commercial'],
            'type': "point",
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     'sloth.items.PointItem',  
        'text':     'Boat - Point',
    },
    {
        'attributes': {
            'type': "poly",
            'class': 'cloud',
        },
        'inserter': 'sloth.items.PolygonItemInserter',
        'item':     'sloth.items.PolygonItem',  
        'text':     'Cloud',
    },
    {
        'attributes': {
            'class': 'plane-point',
            'id': ['military', 'commercial'],
            'type': "point",
        },
        'inserter': 'sloth.items.PointItemInserter',
        'item':     'sloth.items.PointItem',  
        'text':     'Plane - Point',
    },
)
