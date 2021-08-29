from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        tasks = sorted(tasks, reverse=True)

        def can_fill(sessions, t):
            if t == n:
                return True

            task = tasks[t]
            last_task = tasks[t - 1] if t > 0 else None
            visited_session = set()
            for i, session in enumerate(sessions):
                if last_task == task and session in visited_session:
                    continue
                if session + task <= sessionTime:
                    sessions[i] = session + task
                    if can_fill(sessions, t + 1):
                        return True
                    sessions[i] = session
                visited_session.add(session)
            return False

        l, r = 1, n
        while l < r:
            mid = (l + r) >> 1
            if can_fill([0] * mid, 0):
                r = mid
            else:
                l = mid + 1
        return r


if __name__ == '__main__':
    print(Solution().minSessions([1,1,2,2,2,2,3,3,6,6,6,6], 10))
