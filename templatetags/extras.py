from django import template
import sys
register = template.Library()

@register.filter
def get_item(dictionary, key):
    print >>sys.stderr, "----------------------"
    print >>sys.stderr, "key?",key
    key=key.encode('ascii','ignore')
    print >>sys.stderr, "type key?",type(key)

    st = dictionary.get(key)
    print >>sys.stderr, "value?",st
    #print >>sys.stderr, "dictionary?",dictionary
    print >>sys.stderr, dictionary.keys()
    for k in dictionary.keys():
        print >>sys.stderr, "k  :%s" % k
        print >>sys.stderr, "key:%s:" %key
        #print >>sys.stderr, dictionary[k].value
        #print >>sys.stderr, dictionary[key].value
        #print >>sys.stderr, dir(dictionary[k])
 
    #return dictionary[key].value
    return dictionary.get(key)
    #return dictionary.get(key).value
