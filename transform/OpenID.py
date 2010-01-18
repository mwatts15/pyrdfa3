# -*- coding: utf-8 -*-
"""
Simple transfomer: handle OpenID elements. Ie: an openid namespace is added and the usual
'link' elements for openid are exchanged against a namespaced version.

@summary: OpenID transformer module.
@requires: U{RDFLib package<http://rdflib.net>}
@organization: U{World Wide Web Consortium<http://www.w3.org>}
@author: U{Ivan Herman<a href="http://www.w3.org/People/Ivan/">}
@license: This software is available for use under the
U{W3C® SOFTWARE NOTICE AND LICENSE<href="http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231">}
@contact: Ivan Herman, ivan@w3.org
@var OPENID_NS: the OpenID URI used in the package
"""

"""
$Id: OpenID.py,v 1.1 2010-01-18 13:42:38 ivan Exp $
$Date: 2010-01-18 13:42:38 $
"""

OPENID_NS = "http://xmlns.openid.net/auth#"
def OpenID_transform(html, options) :
	"""
	Replace C{openid.XXX} type C{@rel} attribute values in C{<link>} elements by C{openid:XXX}. The openid URI is also
	added to the top level namespaces with the C{openid:} local name.

	@param html: a DOM node for the top level html element
	@param options: invocation options
	@type options: L{Options<pyRdfa.Options>}
	"""

	# the head element is necessary; to be sure, the namespaces are set
	# on that level only
	head = None
	try :
		head = html.getElementsByTagName("head")[0]
	except :
		# no head....
		return

	foundOpenId = False
	for link in html.getElementsByTagName("link") :
		if link.hasAttribute("rel") :
			rel = link.getAttribute("rel")
			newProp = ""
			for n in rel.strip().split() :
				if n.startswith("openid.") :
					newProp += " " + n.replace("openid.","openid:")
					foundOpenId = True
				else :
					newProp += " " + n
			link.setAttribute("rel",newProp.strip())

	# Add the OpenId namespace if necessary
	if foundOpenId and not head.hasAttribute("xmlns:openid") :
		head.setAttributeNS("", "xmlns:openid", OPENID_NS)

