# OpenStack clients smoke tests

I was missing a tool to check basic OpenStack installation functionality using
client executables so I wrote one.

Existing tests:

 * [devstack exercises](https://github.com/openstack-dev/devstack/tree/master/exercises)
are doing pretty much what I want but I had very bad experience debugging
them. I {blame,hate} bash. Also, they are ought to go away.
 * [Tempest](https://github.com/openstack/tempest) is using client libraries
directly.
 * [Torpedo](https://github.com/dprince/torpedo) is using Fog library.

As I don't think this is a proper task for bash, I rather attempted to write
my own solution. Although extending Tempest to use CLIs is an option, it is
rather heavy-weight and not very friendly to my use case.

## How do I use it

`clismoke` is a python module providing tests with required functionality.

Tests live in a `tests` directory and can be run by simply executing them.
`run_tests.sh` is just a crude script to execute all tests.
