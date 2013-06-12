import sys
import urllib
import urllib2
import simplejson

def geocodetor(address):
    proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8118'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    vals = {'address': address, 'sensor': 'false'}
    qstr = urllib.urlencode(vals)
    response = simplejson.loads(urllib2.urlopen("http://maps.google.com/maps/api/geocode/json?%s" % qstr).read()) # address=Los+Angeles&sensor=false").read()
    return response

def main(argv):
    if len(argv) != 2:
        print "Usage:\n\t> python geocodetor.py <address>"
        return

    _json = geocodetor(argv[1])

    if _json['status'] == 'OK':
        fulladdress = _json['results'][0]['formatted_address']
        lat = _json['results'][0]['geometry']['location']['lat']
        lng = _json['results'][0]['geometry']['location']['lng']
        zipcode = ""
        for comp in _json['results'][0]['address_components']:
            if comp['types'][0] == "postal_code":
                zipcode = comp['long_name']
                break
        print "Decoded:\n"
        print "\tFull Address: {0}".format(fulladdress)
        print "\tLat: {0}".format(lat)
        print "\tLng: {0}".format(lng)
        print "\tZipcode: {0}".format(zipcode)
        print ""
    else:
        print "ERRZOR!"

if __name__ == '__main__': sys.exit(main(sys.argv))
