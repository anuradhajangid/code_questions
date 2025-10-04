# https://leetcode.com/problems/subdomain-visit-count/description/
from typing import List
from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)

        for data in cpdomains:
            count, name = data.split(" ")
            domains = name.split(".")
            for i in range(len(domains)):
                domain_name = ".".join(domains[i:len(domains)])
                counts[domain_name] += int(count)
        return [" ".join([str(value), key]) for key, value in counts.items()]

assert Solution().subdomainVisits(cpdomains = ["9001 discuss.leetcode.com"]) == ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
            