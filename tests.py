import os
import unittest
from eventdispatcher import EventDispatcher
from event import Event

PRE_FOO = 'pre.foo'
POST_FOO = 'post.foo'
PRE_BAR = 'pre.bar'
POAST_BAR = 'post.bar'

class TestEventListener():
    def __init__(self):
        self.preFooFired = False
        self.postFooFired = False

    def preFoo(self, event):
        self.preFooFired = True

    def postFoo(self, event):
        self.postFooFired = True

class TestCase(unittest.TestCase):

    

    def setUp(self):
        self.dispatcher = EventDispatcher()

    def tearDown(self):
        return

    def testInitialState(self):
        self.assertEqual({}, self.dispatcher.getListeners())
        self.assertFalse(self.dispatcher.hasListener(PRE_FOO))
        self.assertFalse(self.dispatcher.hasListener(POST_FOO))
    
    def testAddListener(self):
        listener = TestEventListener()
        self.dispatcher.addListener(PRE_FOO, listener, 'preFoo')
        self.dispatcher.addListener(POST_FOO, listener, 'postFoo')
        self.dispatcher.hasListener(PRE_FOO)
        self.dispatcher.hasListener(POST_FOO)

    def testDispatch(self):
        listener = TestEventListener()
        self.dispatcher.addListener(PRE_FOO, listener, 'preFoo')
        self.dispatcher.addListener(POST_FOO, listener, 'postFoo')

        event = Event()
        self.dispatcher.dispatch(eventName=PRE_FOO, event=event)
        self.assertTrue(listener.preFooFired)

if __name__ == '__main__':
    unittest.main()
