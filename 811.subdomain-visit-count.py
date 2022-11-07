#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        new_domains = {}
        for i in cpdomains:
            websites = i.split(" ")
            new_domains[websites[1]] = websites[0]
            domains = websites[1].split(".")
            if len(domains) == 3:
                full_domain = domains[1] + "." + domains[2]
                new_domains[full_domain] = websites[0]
            new_domains[domains[-1]] = websites[0]

        result = []
        for i, j in new_domains.items():
            result.append(j + " " + i)

        return result
        # @lc code=end
