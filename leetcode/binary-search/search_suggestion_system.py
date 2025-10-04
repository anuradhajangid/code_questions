# https://leetcode.com/problems/search-suggestions-system/

from typing import List
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()
        for position, character in enumerate(searchWord):
            products = [ product for product in products if len(product) > position and product[position] == character ]
            result.append(products[:3])
        return result

assert Solution().suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse") == [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
assert Solution().suggestedProducts(products = ["havana"], searchWord = "havana") == [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]