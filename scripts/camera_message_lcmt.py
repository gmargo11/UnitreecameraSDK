"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class camera_message_lcmt(object):
    __slots__ = ["data"]

    __typenames__ = ["byte"]

    __dimensions__ = [[278400]]

    def __init__(self):
        self.data = ""

    def encode(self):
        buf = BytesIO()
        buf.write(camera_message_lcmt._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(bytearray(self.data[:278400]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != camera_message_lcmt._get_packed_fingerprint():
            raise ValueError("Decode error")
        return camera_message_lcmt._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = camera_message_lcmt()
        self.data = buf.read(278400)
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if camera_message_lcmt in parents: return 0
        tmphash = (0x1610a8a9f4d174b7) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if camera_message_lcmt._packed_fingerprint is None:
            camera_message_lcmt._packed_fingerprint = struct.pack(">Q", camera_message_lcmt._get_hash_recursive([]))
        return camera_message_lcmt._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

