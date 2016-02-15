#!/usr/bin/env python

import os
import sys

def usage():
    """ Display program usage """

    print """
    Cyanotype startup helper program
    ---------------------------------

    usage: %s [build|run] <configfile.cfg>

    build:
        compile and render markdown and templates, generate static
        site.

    run:
        Run in development mode (live)

    configfile.cfg:
        Path to the configuration file to override defaults from.

    NOTE: Config file may also be specified using the
    CYANOTYPE_CONFIGURATION environment variable.
    """ % (sys.argv[0])

def run():
    """ Entry point for development server """

    print "Cyanotype Development Server"
    print "Copyright (c) Alexandre Gauthier 2016-2017"
    print "------------------------------------------"

    print "INIT: using configuration file %s" %\
            (os.environ["CYANOTYPE_CONFIGURATION"])

    print "Connect to http://127.0.0.1:5000 to access."

    from cyanotype import app
    app.run(debug=True)

def build():
    """ Entry point for site generation and build """

    from cyanotype import app, freezer
    print "INIT: using configuration file %s" %\
            (os.environ["CYANOTYPE_CONFIGURATION"])
    print "Rendering to: %s" % (freezer.root)
    freezer.freeze()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if not os.environ.has_key('CYANOTYPE_CONFIGURATION'):
            os.environ['CYANOTYPE_CONFIGURATION'] = \
                    os.path.abspath('cyanotype.cfg')
    elif len(sys.argv) == 3:
        if os.environ.has_key('CYANOTYPE_CONFIGURATION'):
            print "Warning! Overriding environment value for config file!"

        os.environ['CYANOTYPE_CONFIGURATION'] = sys.argv[2]

    else:
        usage()
        sys.exit(1)

    # Quick sanity check, maybe ensure the configuration file specified
    # exists?
    if not os.path.isfile(os.environ['CYANOTYPE_CONFIGURATION']):
        print "Critical: specified configuration file %s doesn't exist." %\
                (os.environ['CYANOTYPE_CONFIGURATION'])
        sys.exit(1)

    if sys.argv[1] == "build":
        build()
    elif sys.argv[1] == "run":
        run()
    else:
        usage()
        sys.exit(1)


