"""Mail support for twisted python.
"""

from twisted.protocols import protocol

def createDomainsFactory(protocol_handler, domains):
    '''create a factory with a given protocol handler and a domains attribute

    Return a Factory with a Protocol given as the first argument,
    and a 'domains' attribute given as the second.
    The 'domains' argument should have a [] operator and .has_key method.
    '''
    ret = protocol.Factory()
    ret.protocol = protocol_handler
    ret.domains = domains
    return ret

class DomainWithDefaultDict:

    '''Simulate a dictionary with a default value for non-existing keys.
    '''
    def __init__(self, domains, default):
        self.domains = domains
        self.default = default

    def has_key(self, name):
        return 1

    def __getitem__(self, name):
        return self.domains.get(name, self.default)


class BounceDomain:
    """A domain in which no user exists. 

    This can be used to block off certain domains.
    """
    def exists(self, name, domain):
        """No user exists in a BounceDomain -- always return 0
        """
        return 0
