from manifesto import Manifest

class StaticManifest(Manifest):
    def cache(self):
	  return [
	  '/static/my_style.css',
	  '/static/bootstrap/css/bootstrap.css',
	  '/static/bootstrap/css/bootstrap-responsive.css',
	  '/static/images/art4.png',
	  '/static/js/jquery-1.7.2.js',
	  '/static/bootstrap/js/bootstrap.min.js',
	  ] 