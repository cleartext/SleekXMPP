from . import base
from .. xmlstream.handler.callback import Callback
from .. xmlstream.stanzabase import ElementBase, ET
from .. xmlstream.matcher.xmlmask import MatchXMLMask
from .. stanza.iq import Iq

class vCard(ElementBase):
	namespace = 'vcard-temp'
	name = 'vCard'
	plugin_attrib = 'vcard'
	interfaces = set(('vcard'))
	plugin_attrib_map = set()
	plugin_xml_map = set()


class xep_0054(base.base_plugin):
	"""
	XEP-0054 vcard-temp
	"""
	def plugin_init(self):
		self.description = "vcard-temp"
		self.xep = "0054"
		self.ns = 'vcard-temp'
	
	def post_init(self):
		base.base_plugin.post_init(self)
		self.xmpp.plugin['xep_0030'].add_feature('vcard-temp')
		self.xmpp.stanzaPlugin(Iq, vCard)
		ns = 'jabber:component:accept'
		self.xmpp.registerHandler(
			Callback(
				'IQvCard',
				MatchXMLMask("<iq xmlns='%s' type='get'><vCard xmlns='vcard-temp' /></iq>" % self.xmpp.default_ns),
				self._handle_vcard_get
			)
		)

	def _handle_vcard_get(self, msg):
		self.xmpp.event('get_vcard', msg)

	def get_vcard(self, jid=None):
		iq = self.xmpp.makeIqGet()
		if jid is not None:
			iq.attrib['to'] = jid
		vcard = ET.Element("{%s}vCard" % self.ns)
		iq.append(vcard)
		id = iq.get('id')
		result = send.xmpp.send(iq, "<iq id='%s'/>" % id)
		if result and result is not None and result.get('type', 'error') != 'error':
			xmlvcard = result.find("{%s}vCard" % self.ns)
			return xmlvcard
		return False

	def set_vcard(self, vcard, mfrom):
		iq = self.xmpp.makeIqSet()
		iq['from'] = mfrom
		iq['to'] = mfrom
		iq.setPayload(vcard)
		result = self.xmpp.send(iq)
		if result and result is not None and result.get('type', 'error') != 'error':
			return True
		return False

	def return_vcard(self, iq, vcard):
		""" Sends reply to the Iq with type=get. """
		iq.reply()
		iq.setPayload(vcard)
		iq.send()



	def make_vcard(self, **subelements):
		""" Recursive vCard fabric.
			Example:

			vcard = make_vcard(
				NICKNAME = 'svetlyak40wt',
				PHOTO = dict(
					TYPE = 'image/jpeg',
					BINVAL = base64_encoded_value,
				)
			)
		"""
		def make_subelements(data_dict, root_element):
			for key, value in data_dict.iteritems():
				el = ET.SubElement(root_element, key)
				if isinstance(value, dict):
					make_subelements(value, el)
				else:
					el.text = unicode(value)

		vcard = ET.Element("{%s}vCard" % self.ns)
		make_subelements(subelements, vcard)
		return vcard
