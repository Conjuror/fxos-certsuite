# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import sys
import argparse

def main(argv):
    webidl_dir = 'gecko/dom/webidl/'

    argparser = argparse.ArgumentParser()
    argparser.add_argument("output", help="file for the idl list")
    argparser.add_argument("b2g", help="Path to b2g directory (e.g. ~/B2G")
    args = argparser.parse_args(argv[1:])

    with open(args.output, 'w') as f:
        for fn in os.listdir(os.path.join(args.b2g, webidl_dir)):
            if fn[-6:] == 'webidl':
                f.write('"'+os.path.join(webidl_dir, fn)+'"\n')

if __name__ == '__main__':
    main(sys.argv) 