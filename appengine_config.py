# Created by olala7846@gmail.com
# appengine_config` gets loaded when starting a new application instance.

import vendor

# insert `lib` as a site directory so our `main` module can load
# third-party libraries, and override built-ins with newer
# versions.
vendor.add('lib')
vendor.add('venv/lib/python2.7/site-packages/')
