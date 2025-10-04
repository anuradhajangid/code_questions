import hashlib


class Codec:
    hashmap = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        short = hashlib.sha256(longUrl.encode('utf-8')).hexdigest()
        Codec().hashmap[short] = longUrl
        return 'http://tinyurl.com/' + short
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in Codec.hashmap:
            return Codec().hashmap[shortUrl]
        else:
            raise ValueError("This shortURL is not encoded")
        

#Your Codec object will be instantiated and called as such:
codec = Codec()
assert codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")) == "https://leetcode.com/problems/design-tinyurl"