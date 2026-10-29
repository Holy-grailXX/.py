def get(self, position):
        if position < 1 or position > self.size:
            raise IndexError(f"Invalid position: {position}")

        h = self.head
        count = 1
        while count < position:
            assert h is not None
            h = h.next
            count += 1
        return h.data # type: ignore