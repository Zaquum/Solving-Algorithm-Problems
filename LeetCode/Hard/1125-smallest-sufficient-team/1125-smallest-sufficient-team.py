class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # DP

        skill2idx = {skill: i for i, skill in enumerate(req_skills)}
        n = len(req_skills)
        m = len(people)
        dp = [None] * (1 << n)  # Dynamic Programming Table
        dp[0] = []  # Base case, no skills required

        # print(len(dp))
        
        people_skills = [0] * m  # Convert people skills to bitmask
        for i in range(m):
            for skill in people[i]:
                if skill in skill2idx:
                    people_skills[i] |= 1 << skill2idx[skill]
                    
        for i in range(1 << n):  # Iterate through all combinations of skills
            if dp[i] is None: continue
            for j in range(m):  # Try to add a new person
                combined_skills = i | people_skills[j]
                if dp[combined_skills] is None or len(dp[combined_skills]) > len(dp[i]):
                    dp[combined_skills] = dp[i] + [j]
                    
        # print(dp)
        return dp[(1 << n) - 1]  # Return the team for the full skill set