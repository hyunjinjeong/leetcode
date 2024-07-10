class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # deque로 만들고 0이 되면 append를 안하면 될 듯?
        deque_tickets = collections.deque(enumerate(tickets))

        time = 0
        while deque_tickets:
            i, ticket_count = deque_tickets.popleft()
            time += 1
            
            if i == k and ticket_count == 1:
                return time
            
            if ticket_count > 1:
                deque_tickets.append((i, ticket_count - 1))