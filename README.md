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

## Requirements

Software requirements:

 * python (developed on 2.7)
 * `blessings` module - colours are a must

You also need working OpenStack installation and client credentials set using
environment variables.

## How do I use it

`clismoke` is a python module providing required functionality.

Tests live in a `tests` directory and can be run by simply executing them:

    ./tests/nova.py

To select specific tests to run, supply them as arguments, optionally
without `test_` prefix. For example

    ./tests/nova.py boot

will run `test_boot()` test from `nova.py` test module.

## Future

Tests are currently designed for interactive per-client use, that's why there
is no "run all tests" functionality.

Should they prove useful to someone else or even worthy of inclusion in
Tempest, I'd be happy to help. Until then, I keep em simple and specialised
for my use case.

Should you be interested in extending/porting these tests, please do drop me
an email: jruzicka _at_ redhat _dot_ com
