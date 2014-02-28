from django import template
import sys
register = template.Library()



from django import template
#@register.tag(name="check_magic")

@register.simple_tag
def tag1():
    return "tag1 no parameter"

@register.simple_tag
def tag2(p):
    return "tag2 one parameter: %s"  % p


@register.simple_tag
def check_magic(label, check, detail=None):
    if check is True:
        c="Checked"
    else:
        c=""

    st = ""
    #st = """<label class="control-label">%s</label> n/a<br>""" % label
    if check is True or detail:
        st = """ 
        <label class="control-label">%s</label>
        <input type="checkbox" disabled %s>
        %s
        <br>

        """ % (label, c, detail)
    return st



# this won't work, I guess you can't pass this many things to a template filter
@register.filter
def Xmy_check(label, check, detail):
    """ return pretty html which does the right thing in showing
        or hiding the label, checkbox, and detail text based on
        the values of the check and detail fields. If check is 
        True, or there is anything in detail then show it. """

    st = ""
    if (check is True) or detail:
        st="label, check, detail %s %s %s " % (label, check, detail)

    return st


# call this with something like this in the template:
# entry is a dictionary
# {{entry|get_item:'Name'}}
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
